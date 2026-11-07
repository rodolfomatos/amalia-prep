---
ticket: T403
title: Teste de repeat limit (0 falhas em 100 calls)
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T303
---

# T403 — Teste de repeat limit (0 falhas em 100 chamadas) — M4

## Context
M4 milestone. Depende de T303 (`amalia` no Ollama). Executa `eval/test_repeat_limit.py` contra `amalia`. AC: 0 falhas de repeat limit em 100 chamadas.

## Acceptance Criteria
- [ ] `eval/test_repeat_limit.py::test_no_repeat_limit` passa (0 falhas em 100 calls)

## Scope
**In scope:** Executar teste de repeat limit contra `amalia`; medir falhas; documentar resultado.
**Out of scope:** Corrigir o modelo, re-treinar, re-registrar no Ollama.

## Dependencies
- T303 concluído (`amalia` no Ollama)
- `eval/test_repeat_limit.py` (existe)

## Rollback
- Nenhum (avaliação only-read)

## Known Risks
- `amalia:latest` não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado). Espera-se falhas de repeat limit, confirmado pela execução (3/100).

## Notes
- Execução real (`make eval`): 3/100 chamadas falharam com repeat limit, alvo 0 → FALHOU.
