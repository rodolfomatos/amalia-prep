---
ticket: T403
title: Teste de repeat limit (0 falhas em 100 calls)
phase: verify
tier: AES-standard
---

# T403 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| `eval/test_repeat_limit.py::test_no_repeat_limit` executado | ✅ EXECUTADO | 100 chamadas, contra `amalia` no Ollama |
| Falhas de repeat limit | ❌ FALHOU | 3/100 chamadas falharam, alvo 0 |

## Critério AC T403
- [x] `test_no_repeat_limit` passa (0 falhas em 100 calls) — NÃO SATISFEITO (3/100)

## Causa-raiz (documentada com evidência)
O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302. `convert_to_gguf.py` está quebrado (14 bytes), impedindo registo de modelos fine-tunados. O fine-tune T301 convergiu (loss < 2.0) e reduziria a repetição, mas não foi registado como `amalia`.

## Novas falhas introduzidas
Nenhuma (ticket só-leitura).

## Conclusão Phase 4
T403 NÃO passa no AC (3/100 falhas, alvo 0). Falha real e documentada, com causa-raiz. Não mascarado. Pronto para Phase 5.
