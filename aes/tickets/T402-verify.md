---
ticket: T402
title: Teste de saliência relacional (acurácia > 0.5)
phase: verify
tier: AES-standard
---

# T402 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| `eval/test_salience.py::test_novidade_diferenciacao` executado | ✅ EXECUTADO | 20 exemplos, contra `amalia` no Ollama |
| Acurácia de saliência | ❌ FALHOU | 0.00 (0/20), alvo > 0.5 |
| `test_isolado_mais_novo_que_conectado` | ⏭️ PULADO | 0 exemplos isolados no dataset (todos conectados, nota de T201) |

## Critério AC T402
- [x] `test_novidade_diferenciacao` passa (acurácia > 0.5) — NÃO SATISFEITO (0.00 / 20)

## Causa-raiz (documentada com evidência)
O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302. `convert_to_gguf.py` está quebrado (14 bytes), impedindo registo de modelos fine-tunados como `amalia`. A avaliação mede um modelo de run anterior.

## Novas falhas introduzidas
Nenhuma (ticket só-leitura).

## Conclusão Phase 4
T402 NÃO passa no AC (acurácia 0.00 < 0.5). Falha real e documentada, com causa-raiz (convert_to_gguf.py quebrado). Não mascarado. Pronto para Phase 5.
