---
ticket: T101
title: 100 exemplos de observação → mecanismo latente
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T001
---

# T101 — 100 exemplos de observação → mecanismo latente (dataset abdução)

## Context
M1 milestone. Depende de T001 (ambiente de treino pronto). Gera o dataset sintético de abdução usado para fine-tune (T301) e avaliação (T401). O gerador já existe em `scripts/generate_abduction_data.py` e o dataset já tem 100 linhas, mas há uma contradição de schema a resolver (ver Phase 1).

## Acceptance Criteria
- [ ] 100 exemplos, cada um com `observation`, `latent_variable`, `context` (AC literal do PLAN.md T101)
- [ ] 5 categorias de latente (como dataset do ACA), 20 exemplos por categoria (T102 — escopo separado, mas schema deve permitir)
- [ ] Dataset válido (JSONL, sem duplicatas): 100 linhas, todas únicas, schema válido (T103 — escopo separado)

## Scope
**In scope:** Garantir que `data/abduction_training.jsonl` satisfaça o AC literal de T101 (top-level `latent_variable` em cada exemplo), sem quebrar o contrato executável dos testes (`eval/test_abduction.py` lê `ground_truth.latent_variable`).
**Out of scope:** T102 (contagem por categoria), T103 (validação de duplicatas/schema formal), fine-tune (T301), avaliação (T401).

## Dependencies
- T001 concluído (ambiente com Python + deps)
- `scripts/generate_abduction_data.py` existente
- `eval/test_abduction.py` lê `ground_truth.latent_variable` — não pode quebrar

## Rollback
- Restaurar `data/abduction_training.jsonl` e `scripts/generate_abduction_data.py` do commit anterior

## Known Risks
- Adicionar campo redundante (`latent_variable` top-level espelhando `ground_truth.latent_variable`) — duplicação de dados, mas necessário para satisfazer o AC literal sem quebrar testes
- Regenerar o dataset pode alterar conteúdo se o gerador mudar; usar mesma seed para manter exemplos idênticos + novo campo

## Notes
- Dados já existem: 100 linhas, geradas com seeds 0-99
- Schema atual: `id, category, observation, context, ground_truth{latent_variable, mechanism}`
- Falta para AC literal: top-level `latent_variable`
