---
ticket: T103
title: Dataset valido (JSONL, sem duplicatas) — abducao
phase: verify
tier: AES-standard
---

# T103 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| 100 linhas | ✅ PASS | `len(lines) == 100` |
| Todas as linhas únicas (id e conteúdo) | ✅ PASS | 100 IDs únicos, 100 conteúdos únicos |
| Schema válido em cada linha (id, category, observation, latent_variable top-level, context, ground_truth{latent_variable, mechanism}) | ✅ PASS | 0 campos faltando em todas as 100 linhas |
| JSONL válido (todas as linhas parseáveis) | ✅ PASS | 0 erros de parse |
| Distribuição 20/categoria × 5 categorias | ✅ PASS | amor_proibido/ausência/evento_trágico/objeto_infancia/pessoa_proibida = 20 cada |

## Critério AC T103
- [x] 100 linhas — SATISFEITO
- [x] Todas as linhas únicas — SATISFEITO
- [x] Schema válido — SATISFEITO

## Novas falhas introduzidas
Nenhuma (ticket só-leitura, sem alteração de ficheiros).

## Falhas pré-existentes
Nenhuma relevante (dataset já válido por T101/T102).

## Conclusão Phase 4
T103 passa no Acceptance Criteria completo. O artefato `data/abduction_training.jsonl` está válido e pronto para consumo por T301 (fine-tune) e T401 (avaliação). Pronto para Phase 5 (Critical Review).
