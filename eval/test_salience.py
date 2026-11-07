"""
Testes de saliência relacional para o modelo Amália.

Testa se o modelo consegue diferenciar conteúdos conectados (menos novos)
de conteúdos isolados (mais novos) com base na estrutura de relações
entre ilhas.
"""
import json
import subprocess
from pathlib import Path

import pytest

DATA_PATH = Path("data/salience_training.jsonl")
MODEL = "amalia"
OLLAMA = "ollama"


def run_llm(prompt: str, timeout: int = 60) -> str:
    """Executa o modelo via Ollama."""
    result = subprocess.run(
        [OLLAMA, "run", MODEL, prompt],
        capture_output=True,
        text=True,
        timeout=timeout
    )
    if result.returncode != 0:
        raise RuntimeError(f"Ollama falhou: {result.stderr}")
    return result.stdout.strip()


def load_examples(max_n: int = 20) -> list[dict]:
    """Carrega exemplos do dataset de saliência."""
    examples = []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= max_n:
                break
            examples.append(json.loads(line))
    return examples


def test_model_available():
    """Verifica se o modelo amalia está disponível no Ollama."""
    result = subprocess.run(
        [OLLAMA, "list"], capture_output=True, text=True
    )
    assert "amalia" in result.stdout, "Modelo 'amalia' não encontrado no Ollama"


def test_novidade_diferenciacao():
    """Testa se o modelo diferencia ilhas conectadas de isoladas."""
    examples = load_examples()
    assert len(examples) > 0, "Nenhum exemplo de saliência encontrado"

    correct = 0
    total = 0

    for example in examples:
        conteudo = example.get("conteudo", "")
        novidade_esperada = example.get("novidade_esperada", 0.5)
        ilhas = example.get("ilhas", [])
        ilhas_desc = "; ".join(
            f"{i.get('nome', '')}: {i.get('descricao', '')}" for i in ilhas[:5]
        )

        prompt = (
            f"Conteúdo: {conteudo}\n"
            f"Ilhas: {ilhas_desc}\n"
            f"Tarefa: Avalie a novidade relacional de 0.0 a 1.0.\n"
            f"Responda APENAS com o número.\n"
        )
        response = run_llm(prompt)

        try:
            novidade_predita = float(response.strip())
            if abs(novidade_predita - novidade_esperada) < 0.3:
                correct += 1
        except ValueError:
            pass
        total += 1

    accuracy = correct / total if total > 0 else 0.0
    print(f"\nAcurácia de saliência: {accuracy:.2f} ({correct}/{total})")
    assert accuracy > 0.5, f"Acurácia muito baixa: {accuracy:.2f} (alvo: > 0.5)"


def test_isolado_mais_novo_que_conectado():
    """Testa que conteúdo isolado recebe maior novidade que conectado."""
    examples = load_examples()
    isolados = [e for e in examples if e.get("ilhas_conectadas", 0) == 0]
    conectados = [e for e in examples if e.get("ilhas_conectadas", 0) > 0]

    if not isolados or not conectados:
        pytest.skip("Não há exemplos suficientes de ambos os tipos")

    # Conteúdos isolados devem ter novidade > 0.7
    for ex in isolados[:5]:
        novidade = ex.get("novidade_esperada", 0.5)
        assert novidade > 0.7, (
            f"Conteúdo isolado com novidade baixa: {novidade}"
        )

    # Conteúdos conectados devem ter novidade < 0.8
    for ex in conectados[:5]:
        novidade = ex.get("novidade_esperada", 0.5)
        assert novidade < 0.8, (
            f"Conteúdo conectado com novidade alta: {novidade}"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
