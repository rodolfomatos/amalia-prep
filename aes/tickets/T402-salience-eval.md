---
ticket: T402
title: Teste de saliência relacional (acurácia > 0.5)
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T203, T303
---

# T402 — Teste de saliência relacional offline (acurácia > 0.5) — M4

## Context
M4 milestone. Depende de T203 (dataset saliência válido) e T303 (`amalia` no Ollama). Executa `eval/test_salience.py` contra `amalia`. AC: acurácia de saliência > 0.5.

## Acceptance Criteria
- [ ] `eval/test_salience.py::test_novidade_diferenciacao` passa (acurácia > 0.5)

## Scope
**In scope:** Executar teste de saliência contra `amalia`; medir acurácia; documentar resultado.
**Out of scope:** Corrigir o modelo, re-treinar, re-registrar no Ollama.

## Dependencies
- T203 concluído (data/salience_training.jsonl válido e versionado)
- T303 concluído (`amalia` no Ollama)
- `eval/test_salience.py` (existe)

## Rollback
- Nenhum (avaliação only-read)

## Known Risks
- `amalia:latest` não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado). Espera-se acurácia baixa/zerada, confirmado pela execução (0.00).
- `test_isolado_mais_novo_que_conectado` é pulado (sem exemplos isolados no dataset, nota de T201) — não é parte do AC de T402.

## Notes
- Execução real (`make eval`): acurácia de saliência 0.00 (0/20), alvo > 0.5 → FALHOU.
- `test_isolado_mais_novo_que_conectado`: PULADO (0 exemplos isolados no dataset, todos conectados).
