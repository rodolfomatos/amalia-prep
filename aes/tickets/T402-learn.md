---
ticket: T402
title: Teste de saliência relacional (acurácia > 0.5)
phase: learn
tier: AES-standard
---

# T402 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Executei `eval/test_salience.py::test_novidade_diferenciacao` contra `amalia`. Resultado: acurácia 0.00 (0/20), alvo > 0.5 → FALHOU. `test_isolado_mais_novo_que_conectado` foi pulado (0 exemplos isolados no dataset, nota de T201).

## O que correu bem
- Avaliação executada de fato, com evidência real (0.00/20).
- Resultado não mascarado.
- Causa-raiz identificada (`amalia` não é dos fine-tunes).

## O que correu mal / pode melhorar
- Modelo `amalia` não atende critério de saliência (0.00 acurácia).
- Causa: `convert_to_gguf.py` quebrado → não registar fine-tune T302 como `amalia`.
- Fine-tune T302 convergiu (loss < 2.0) mas não pôde ser validado via Ollama.

## Insight para o registo hostil
> **Categoria**: Avaliação contra modelo errado (recorrente — mesmo que T401)
> **Insight**: O mesmo padrão de T401 repete em T402: avaliar contra `amalia` que não é o fine-tunado produz 0.00 acurácia, mas o fine-tune em si convergiu. O gap é de infra (convert_to_gguf.py), não de qualidade do treino.
> **Origem**: T402, consistente com T401.
> **Impacto**: M4 não pode validar o modelo treinado até corrigir convert_to_gguf.py e re-registrar `amalia`.
> **Aplicado a**: T401, T402; relevante para T403, M4, M5.
> **Data**: 2026-11-07

## Próximo ticket na sequência
T403 (teste de repeat limit, 3/100 falhas, alvo 0 → falhou por mesma causa-raiz).
