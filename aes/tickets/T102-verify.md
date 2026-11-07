---
ticket: T102
title: 5 categorias de latente, 20 exemplos por categoria
phase: verify
tier: AES-standard
---

# T102 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| 100 linhas JSONL | ✅ PASS | `wc -l = 100` |
| Exatamente 20 exemplos por cada uma das 5 categorias | ✅ PASS | amor_proibido 20, ausência 20, evento_trágico 20, objeto_infancia 20, pessoa_proibida 20 |
| 5 categorias de latente presentes | ✅ PASS | mesmo conjunto de T101 |
| Cada linha com schema T101 (observation, latent_variable top-level, context) | ✅ PASS | verificado em todas as 100 linhas |
| `ground_truth.latent_variable` preservado (testes não quebram) | ✅ PASS | todas as linhas têm o campo nested |
| IDs únicos (sem duplicatas) | ✅ PASS | 100 IDs sequenciais `abduction_0000`..`abduction_0099` |
| JSONL válido | ✅ PASS | todas as linhas fazem `json.loads` |

## Critério AC T102
- [x] 5 categorias de latente — SATISFEITO
- [x] Exatamente 20 exemplos por categoria (total 100) — SATISFEITO

## Novas falhas introduzidas por esta alteração
Nenhuma. O diff funcional é a lógica de distribuição por categoria no gerador + regeneração do dataset.

## Falhas pré-existentes (reportadas, não bloqueantes)
- 2 erros de ruff em `scripts/generate_abduction_data.py` (`EXE001` shebang, `F401` `import sys` não usado) — pré-existentes, não introduzidos por T102, fora do escopo do AC.

## Verificação de regressão
- Schema T101 (`latent_variable` de topo) mantido em todas as linhas.
- Contrato dos testes (`ground_truth.latent_variable`) mantido.
- IDs únicos preservados.

## Conclusão Phase 4
T102 passa no Acceptance Criteria (5 categorias × 20 exemplos = 100, schema completo, sem duplicatas, JSONL válido). Pronto para Phase 5 (Critical Review).
