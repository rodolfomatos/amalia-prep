---
ticket: T103
title: Dataset valido (JSONL, sem duplicatas) — abducao
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T102
---

# T103 — Dataset válido (JSONL, sem duplicatas, schema válido) — abdução

## Context
Último ticket de M1. Depende de T102 (distribuição 20/categoria) e T101 (schema com `latent_variable` de topo). T103 AC: 100 linhas, todas únicas, schema válido. Nesta fase trata-se de validação formal do artefato já produzido por T101/T102.

## Acceptance Criteria
- [ ] 100 linhas no `data/abduction_training.jsonl`
- [ ] Todas as linhas únicas (sem duplicatas de id/conteúdo)
- [ ] Schema válido em cada linha: `id`, `category`, `observation`, `latent_variable` (top-level), `context`, `ground_truth{latent_variable, mechanism}`
- [ ] JSONL válido (todas as linhas parseáveis como JSON)

## Scope
**In scope:** Validação formal do dataset `data/abduction_training.jsonl` contra o AC acima; documentar o resultado.
**Out of scope:** Alterar o dataset (já válido por T101/T102), criar scripts de validação reutilizáveis (escopo separado), fine-tune (T301).

## Dependencies
- T102 concluído (dataset com 20/categoria, schema T101)

## Rollback
- Nenhum (validação apenas, sem alteração de ficheiros)

## Known Risks
- Nenhum risco de alteração (ticket só-leitura sobre o dataset). Risco seria o dataset estar inválido, o que bloquearia T301/T401.

## Notes
- T101/T102 já verificaram: 100 linhas, IDs únicos, 20/categoria, schema completo, `ground_truth.latent_variable` preservado
- T103 consolida isso numa validação formal única
