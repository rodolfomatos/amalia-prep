---
ticket: T401
title: Teste de abdução (acurácia > 0.3)
phase: learn
tier: AES-standard
---

# T401 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Executei `eval/test_abduction.py::test_abduction_accuracy` contra o modelo `amalia` no Ollama. O resultado: acurácia 0.00 (0/20), alvo > 0.3 → FALHOU. Também falhou `test_no_verbose_output` (resposta verbosa, 871 caracteres > 100). Passaram `test_model_available` e `test_mechanism_not_philosophical`.

## O que correu bem
- A avaliação foi executada de fato (não assumida), gerando evidência real (0.00/20).
- O resultado não foi mascarado, respeitando "se não é testado, está quebrado" e "não yes-men".
- A causa-raiz foi identificada: `amalia:latest` não é dos fine-tunes T301/T302.

## O que correu mal / pode melhorar
- O modelo `amalia` não atende ao critério de abdução (0.00 acurácia) nem à saída curta (verboso).
- Causa: `convert_to_gguf.py` quebrado (14 bytes) → não dá para registar os fine-tunes T301/T302 como `amalia`.
- Sem um `amalia` fine-tunado registrado, M4 e M5 não podem validar o modelo treinado.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Avaliação contra modelo errado
> **Insight**: Executar avaliação de fine-tune contra um modelo que NÃO é o fine-tunado produz resultados inválidos (0.00 acurácia) que não refletem a qualidade do treino. O gap é de infra (convert_to_gguf.py), não de qualidade do fine-tune (que convergiu com loss < 2.0 em T301).
> **Origem**: T401 (execução real da avaliação).
> **Impacto**: M4 não pode validar o modelo treinado até que convert_to_gguf.py seja corrigido e o modelo re-registrado como `amalia`.
> **Aplicado a**: T401; relevante para T402, T403, M4, M5.
> **Data**: 2026-11-07

## Próximo ticket na sequência
T402 (teste de saliência relacional, acurácia > 0.5) — já executado no `make eval` anterior (0.00/20, falhou por mesma causa-raiz). Depois T403 (repeat limit, 3/100 falhas).
