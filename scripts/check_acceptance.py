#!/usr/bin/env python3
"""
Verifica os critérios de aceitação para o modelo Amália.

Critérios:
1. Latência < 3s por chamada
2. Sem repeat limit em 100 chamadas
3. Acurácia de abdução > 0.3
4. Novidade relacional diferenciante
5. Saída curta (< 200 tokens média)
"""
import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

MODEL = "amalia"
OLLAMA = "ollama"


def run_llm(prompt: str, timeout: int = 60) -> tuple[str, float]:
    """Executa uma chamada ao modelo via Ollama e retorna (resposta, tempo_s)."""
    start = time.time()
    try:
        result = subprocess.run(
            [OLLAMA, "run", MODEL, prompt],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start
        if result.returncode != 0:
            return f"ERROR: {result.stderr}", elapsed
        return result.stdout.strip(), elapsed
    except subprocess.TimeoutExpired:
        return "ERROR: timeout", time.time() - start


def test_latency() -> tuple[bool, str]:
    """Critério: latência < 3s por chamada."""
    times = []
    for i in range(5):
        _, elapsed = run_llm("Responda apenas: OK")
        times.append(elapsed)
    avg = statistics.mean(times)
    ok = avg < 3.0
    return ok, f"Latência média: {avg:.2f}s (alvo: < 3.0s)"


def test_repeat_limit() -> tuple[bool, str]:
    """Critério: sem repeat limit em 100 chamadas."""
    failures = 0
    for i in range(100):
        response, _ = run_llm(f"Responda apenas com o número: {i}")
        if "repeat" in response.lower() or "limit" in response.lower() or "Error" in response:
            failures += 1
    ok = failures == 0
    return ok, f"Falhas de repeat limit: {failures}/100 (alvo: 0)"


def test_abduction_accuracy() -> tuple[bool, str]:
    """Critério: acurácia de abdução > 0.3."""
    # Usar exemplos do dataset de treino como teste simples
    data_path = Path("data/abduction_training.jsonl")
    if not data_path.exists():
        return False, "Dataset de abdução não encontrado"

    correct = 0
    total = 0
    with open(data_path, "r", encoding="utf-8") as f:
        for line in f:
            if total >= 20:  # Limite para não demorar muito
                break
            example = json.loads(line)
            observation = example.get("observation", "")
            latent = example.get("ground_truth", {}).get("latent_variable", "")

            prompt = (
                f"Observação: {observation}\n"
                f"Tarefa: Adivinhe a variável latente escondida.\n"
                f"Responda APENAS com a variável latente, nada mais.\n"
            )
            response, _ = run_llm(prompt)
            if latent.lower() in response.lower():
                correct += 1
            total += 1

    accuracy = correct / total if total > 0 else 0.0
    ok = accuracy > 0.3
    return ok, f"Acurácia de abdução: {accuracy:.2f} ({correct}/{total}, alvo: > 0.3)"


def test_salience_differentiation() -> tuple[bool, str]:
    """Critério: o modelo diferencia ilhas conectadas vs isoladas."""
    data_path = Path("data/salience_training.jsonl")
    if not data_path.exists():
        return False, "Dataset de saliência não encontrado"

    correct = 0
    total = 0
    with open(data_path, "r", encoding="utf-8") as f:
        for line in f:
            if total >= 20:
                break
            example = json.loads(line)
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
            response, _ = run_llm(prompt)
            try:
                novidade_predita = float(response.strip())
                # Aceitar se estiver dentro de 0.3 do esperado
                if abs(novidade_predita - novidade_esperada) < 0.3:
                    correct += 1
            except ValueError:
                pass
            total += 1

    accuracy = correct / total if total > 0 else 0.0
    ok = accuracy > 0.5
    return ok, f"Acurácia de saliência: {accuracy:.2f} ({correct}/{total}, alvo: > 0.5)"


def test_output_verbosity() -> tuple[bool, str]:
    """Critério: saída média < 200 tokens (aproximado por caracteres)."""
    responses = []
    for i in range(5):
        response, _ = run_llm("Responda de forma curta e direta.")
        responses.append(len(response))
    avg_chars = statistics.mean(responses) if responses else 0
    # Aproximação: 1 token ≈ 4 caracteres
    avg_tokens = avg_chars / 4
    ok = avg_tokens < 200
    return ok, f"Tokens médios por resposta: {avg_tokens:.0f} (alvo: < 200)"


def main():
    tests = [
        ("Latência < 3s", test_latency),
        ("Sem repeat limit", test_repeat_limit),
        ("Acurácia abdução > 0.3", test_abduction_accuracy),
        ("Saliência relacional > 0.5", test_salience_differentiation),
        ("Saída curta < 200 tokens", test_output_verbosity),
    ]

    print("=== Critérios de Aceitação - Amália ===\n")
    all_passed = True
    for name, test_fn in tests:
        try:
            ok, message = test_fn()
            status = "✓" if ok else "✗"
            print(f"{status} {name}: {message}")
            if not ok:
                all_passed = False
        except Exception as e:
            print(f"✗ {name}: ERRO - {e}")
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("✓ TODOS OS CRITÉRIOS DE ACEITAÇÃO ATENDIDOS")
        sys.exit(0)
    else:
        print("✗ ALGUNS CRITÉRIOS NÃO FORAM ATENDIDOS")
        sys.exit(1)


if __name__ == "__main__":
    main()
