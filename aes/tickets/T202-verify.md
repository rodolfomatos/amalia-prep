---
ticket: T202
title: Ilhas com múltiplos tipos de relação (≥3 tipos)
phase: verify
tier: AES-standard
---

# T202 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| Tipos distintos de relação no dataset | ✅ PASS | 5 tipos distintos (AGREGADO_EM, COMPLEMENTA, CONTRADIZ, DERIVA_DE, RELATED_TO) |
| ≥ 3 tipos diferentes | ✅ PASS | 5 ≥ 3 |
| Inclui RELATED_TO, CONTRADIZ, COMPLEMENTA | ✅ PASS | todos os 3 presentes |
| Gerador define os mesmos tipos | ✅ PASS | `RELATION_TYPES` tem os 5 tipos |

## Critério AC T202
- [x] Pelo menos 3 tipos diferentes de relação — SATISFEITO (5)
- [x] Inclui RELATED_TO, CONTRADIZ, COMPLEMENTA — SATISFEITO

## Novas falhas introduzidas
Nenhuma (ticket só-leitura, sem alteração de ficheiros).

## Conclusão Phase 4
T202 passa no Acceptance Criteria completo. O dataset e o gerador contêm 5 tipos de relação, satisfazendo o requisito de ≥3 incluindo os 3 nomeados. Pronto para Phase 5 (Critical Review).
