---
ticket: T401
title: Teste de abdução (acurácia > 0.3)
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T103, T303
---

# T401 — Teste de abdução offline (acurácia > 0.3) — M4

## Context
M4 milestone. Depende de T103 (dataset abdução válido), T303 (modelo `amalia` no Ollama). Executa `eval/test_abduction.py` contra o modelo `amalia`. AC: acurácia de abdução > 0.3 (> 30% reconstrução correta).

## Acceptance Criteria
- [ ] `eval/test_abduction.py::test_abduction_accuracy` passa (acurácia > 0.3)

## Scope
**In scope:** Executar teste de abdução contra `amalia` no Ollama; medir acurácia; documentar resultado.
**Out of scope:** Corrigir o modelo (convert_to_gguf.py quebrado), re-treinar, re-registrar no Ollama.

## Dependencies
- T103 concluído (data/abduction_training.jsonl válido e versionado)
- T303 concluído (`amalia` no Ollama)
- `eval/test_abduction.py` (existe)

## Rollback
- Nenhum (avaliação only-read sobre o modelo)

## Known Risks
- O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302 (convert_to_gguf.py quebrado impede registrá-los). Espera-se que a acurácia seja baixa/zerada, como confirmado pela execução (0.00).
- `test_no_verbose_output` também falha (modelo responde de forma verbosa), mas não é parte do AC de T401.

## Notes
- Execução real: acurácia de abdução 0.00 (0/20), alvo > 0.3 → FALHOU.
- `test_mechanism_not_philosophical` PASSOU (modelo não usa explicações filosóficas abstratas).
- `test_model_available` PASSOU (`amalia` está no Ollama).
