---
ticket: T401
title: Teste de abdução (acurácia > 0.3)
phase: verify
tier: AES-standard
---

# T401 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| `eval/test_abduction.py::test_abduction_accuracy` executado | ✅ EXECUTADO | 20 exemplos, contra `amalia` no Ollama |
| Acurácia de abdução | ❌ FALHOU | 0.00 (0/20), alvo > 0.3 |
| `test_model_available` | ✅ PASSOU | `amalia` está no Ollama |
| `test_mechanism_not_philosophical` | ✅ PASSOU | Modelo não usa explicações filosóficas abstratas |
| `test_no_verbose_output` | ❌ FALHOU | Modelo responde de forma verbosa (não é parte do AC de T401, mas relevante) |

## Critério AC T401
- [x] `test_abduction_accuracy` passa (acurácia > 0.3) — NÃO SATISFEITO (0.00 / 20)

## Causa-raiz (documentada com evidência)
O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302. Esses produziram adapters LoRA locais (`models/amalia-abduction/`, `models/amalia-salience/`), mas `convert_to_gguf.py` está quebrado (14 bytes), impedindo a conversão para GGUF e o registo como `amalia` no Ollama. Logo, a avaliação de T401 mede um modelo de um run anterior, não o modelo fine-tunado.

## Novas falhas introduzidas
Nenhuma (ticket só-leitura sobre o modelo).

## Verificação de regressão
N/A (avaliação only-read; não houve alteração de código nem de modelo).

## Conclusão Phase 4
T401 NÃO passa no Acceptance Criteria (acurácia 0.00 < 0.3). A falha é real e documentada, com causa-raiz identificada (convert_to_gguf.py quebrado → `amalia` não reflete os fine-tunes). Não se deve mascarar o resultado. Pronto para Phase 5 (Critical Review).
