"""
Testes de abdução para o modelo Amália.

Testa se o modelo consegue adivinhar variáveis latentes a partir de
observações incompletas, sem explicações filosóficas abstratas.
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

DATA_PATH = Path("data/abduction_training.jsonl")
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
    """Carrega exemplos do dataset de abdução."""
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


def test_abduction_accuracy():
    """Testa se o modelo consegue adivinhar variáveis latentes."""
    examples = load_examples()
    assert len(examples) > 0, "Nenhum exemplo de abdução encontrado"

    correct = 0
    total = 0

    for example in examples:
        observation = example.get("observation", "")
        latent = example.get("ground_truth", {}).get("latent_variable", "")

        prompt = (
            f"Observação: {observation}\n"
            f"Tarefa: Adivinhe a variável latente escondida.\n"
            f"Responda APENAS com a variável latente, nada mais.\n"
        )
        response = run_llm(prompt)

        if latent.lower() in response.lower():
            correct += 1
        total += 1

    accuracy = correct / total if total > 0 else 0.0
    print(f"\nAcurácia de abdução: {accuracy:.2f} ({correct}/{total})")
    assert accuracy > 0.3, f"Acurácia muito baixa: {accuracy:.2f} (alvo: > 0.3)"


def test_no_verbose_output():
    """Testa que o modelo não produz chain-of-thought verboso."""
    examples = load_examples(max_n=5)
    for example in examples:
        observation = example.get("observation", "")
        prompt = (
            f"Observação: {observation}\n"
            f"Tarefa: Adivinhe a variável latente escondida.\n"
            f"Responda APENAS com a variável latente, nada mais.\n"
        )
        response = run_llm(prompt)
        # A resposta deve ser curta (menos de 100 caracteres)
        assert len(response) < 100, f"Resposta muito verbosa: {response[:200]}"
        # Não deve conter indicadores de chain-of-thought
        assert "/think" not in response.lower()
        assert "pensando" not in response.lower()
        assert "vamos ver" not in response.lower()


def test_mechanism_not_philosophical():
    """Testa que o mecanismo não é uma explicação filosófica abstrata."""
    examples = load_examples(max_n=5)
    abstract_words = [
        "alma", "espírito", "destino", "fate", "koan", "zen",
        "essência", "mistério do universo", "significado da vida"
    ]
    for example in examples:
        observation = example.get("observation", "")
        prompt = (
            f"Observação: {observation}\n"
            f"Tarefa: Adivinhe a variável latente escondida.\n"
            f"Responda APENAS com a variável latente, nada mais.\n"
        )
        response = run_llm(prompt)
        for word in abstract_words:
            assert word not in response.lower(), (
                f"Resposta contém termo filosófico '{word}': {response}"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
