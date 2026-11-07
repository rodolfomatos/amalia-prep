"""
Teste de repeat limit para o modelo Amália.

Verifica se o modelo não entra em loop de repetição durante chamadas
sequenciais, especialmente no step cost_ensation do ITERReasoner.
"""
import subprocess

import pytest

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


def test_model_available():
    """Verifica se o modelo amalia está disponível no Ollama."""
    result = subprocess.run(
        [OLLAMA, "list"], capture_output=True, text=True
    )
    assert "amalia" in result.stdout, "Modelo 'amalia' não encontrado no Ollama"


def test_no_repeat_limit():
    """Testa que o modelo não entra em loop de repetição em 100 chamadas."""
    failures = 0
    for i in range(100):
        response = run_llm(f"Responda apenas com o número: {i}")
        if "repeat" in response.lower() or "limit" in response.lower() or "Error" in response:
            failures += 1

    assert failures == 0, (
        f"{failures}/100 chamadas falharam com repeat limit"
    )


def test_cost_estimation_no_repeat():
    """Testa especificamente o step cost_ensation do ITERReasoner."""
    prompt = (
        "Estima o custo computacional deste mecanismo em bits.\n"
        "Responda apenas com um número float.\n"
        "Mecanismo: reconstrução de variável latente por abductão.\n"
    )
    response = run_llm(prompt)
    # Deve conter um número, não entrar em loop
    assert "repeat" not in response.lower()
    assert "limit" not in response.lower()
    assert "Error" not in response


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
