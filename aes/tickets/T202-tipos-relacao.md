---
ticket: T202
title: Ilhas com múltiplos tipos de relação (≥3 tipos)
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T201
---

# T202 — Ilhas com múltiplos tipos de relação (≥3 tipos diferentes)

## Context
M2 milestone. Depende de T201 (dataset com 50 exemplos, schema com `relacoes` de topo). T202 AC: pelo menos 3 tipos diferentes de relação entre os exemplos (RELATED_TO, CONTRADIZ, COMPLEMENTA). O gerador já define `RELATION_TYPES` com 5 tipos e o dataset já contém todos os 5 (verificado no T201). Trata-se de confirmação formal.

## Acceptance Criteria
- [ ] Pelo menos 3 tipos diferentes de relação entre os exemplos
- [ ] Os tipos incluem RELATED_TO, CONTRADIZ, COMPLEMENTA (como no PLAN.md)

## Scope
**In scope:** Confirmação formal de que o dataset `data/salience_training.jsonl` e o gerador `scripts/generate_salience_data.py` contêm ≥3 tipos de relação, incluindo os 3 exigidos.
**Out of scope:** Alterar o dataset ou o gerador (já satisfazem o AC), T203 (validação de validade/unicidade).

## Dependencies
- T201 concluído (dataset com `relacoes` de topo, 5 tipos de relação)

## Rollback
- Nenhum (confirmação apenas, sem alteração de ficheiros)

## Known Risks
- Nenhum (confirmação apenas). Risco seria o dataset ter <3 tipos, o que bloquearia T402 — já verificado que não é o caso.

## Notes
- RELATION_TYPES no gerador: ["RELATED_TO", "CONTRADIZ", "COMPLEMENTA", "DERIVA_DE", "AGREGADO_EM"] (5 tipos)
- Dataset: todos os 5 tipos presentes (AGREGADO_EM 97, COMPLEMENTA 88, CONTRADIZ 106, DERIVA_DE 105, RELATED_TO 106 — contagem total de relações, verificado no T201)
