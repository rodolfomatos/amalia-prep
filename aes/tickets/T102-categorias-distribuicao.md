---
ticket: T102
title: Ilhas com múltiplos tipos de relação  [sic: M1 — 5 categorias × 20 exemplos]
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T101
---

# T102 — 5 categorias de latente, 20 exemplos por categoria (dataset abdução)

## Context
M1 milestone. Depende de T101 (dataset com 100 exemplos e schema com `latent_variable` de topo). T102 AC exige exatamente 20 exemplos por cada uma das 5 categorias de variável latente (total 100). A distribuição atual é 23/19/17/20/21 — não satisfeita.

## Acceptance Criteria
- [ ] 5 categorias de latente (como dataset do ACA)
- [ ] Exatamente 20 exemplos por categoria (total 100)
- [ ] Cada exemplo mantém schema T101: `observation`, `latent_variable` (top-level), `context`, `ground_truth.latent_variable`
- [ ] Dataset válido (JSONL, sem duplicatas de id) — complementa T103

## Scope
**In scope:** Modificar `scripts/generate_abduction_data.py` para distribuir `--count` igualmente pelas categorias; regenerar `data/abduction_training.jsonl` com 20/categoria.
**Out of scope:** T103 (validação formal de duplicatas/schema), T201+ (saliência), T301+ (fine-tune).

## Dependencies
- T101 concluído (schema com `latent_variable` de topo)
- `scripts/generate_abduction_data.py`

## Rollback
- Restaurar `scripts/generate_abduction_data.py` e `data/abduction_training.jsonl` do commit anterior (e0b327f5)

## Known Risks
- Regenerar o dataset altera o conteúdo dos exemplos (distribuição controlada por categoria em vez de aleatória) — esperado e desejado para T102.
- IDs devem continuar únicos (contador sequencial).
- Não quebrar o campo `latent_variable` de topo adicionado em T101 nem `ground_truth.latent_variable` (contrato dos testes).

## Notes
- Categorias: amor_proibido, ausência, evento_trágico, objeto_infancia, pessoa_proibida
- Distribuição atual (pré-T102): 23/19/17/20/21
- Alvo: 20/20/20/20/20
