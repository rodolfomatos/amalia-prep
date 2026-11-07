---
ticket: T101
title: 100 exemplos de observação → mecanismo latente
phase: verify
tier: AES-standard
---

# T101 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| 100 linhas JSONL | ✅ PASS | `wc -l = 100` |
| Cada linha com top-level `observation`, `latent_variable`, `context` | ✅ PASS | verificado em todas as 100 linhas |
| 100 IDs únicos (sem duplicatas) | ✅ PASS | ids `abduction_0000`..`abduction_0099`, nenhum duplicado |
| JSONL válido (todas as linhas parseáveis) | ✅ PASS | todas as 100 linhas fazem `json.loads` com sucesso |
| `ground_truth.latent_variable` preservado (testes não quebram) | ✅ PASS | `eval/test_abduction.py:61` ainda lê o campo nested |
| 5 categorias de latente presentes | ✅ PASS | amor_proibido, ausência, evento_trágico, objeto_infancia, pessoa_proibida |
| Gerador emitirá `latent_variable` top-level em regenerações futuras | ✅ PASS | `scripts/generate_abduction_data.py` atualizado |

## Critério AC T101
- [x] 100 exemplos, cada um com `observation`, `latent_variable`, `context` (top-level) — SATISFEITO

## Novas falhas introduzidas por esta alteração
Nenhuma. O único diff funcional é a adição do campo top-level `latent_variable` (espelhando `ground_truth.latent_variable`) no gerador e no dataset.

## Falhas pré-existentes (reportadas, não bloqueantes)
- 2 erros de ruff em `scripts/generate_abduction_data.py` (`EXE001` shebang, `F401` `import sys` não usado) — pré-existentes, não introduzidos por T101, fora do escopo do AC do ticket.

## Verificação de regressão
- Contrato executável dos testes (`ground_truth.latent_variable`) mantido intacto.
- IDs e conteúdo dos exemplos preservados (mesmas seeds 0-99); apenas acrescido o campo `latent_variable`.

## Conclusão Phase 4
T101 passa no Acceptance Criteria literal (top-level `observation`/`latent_variable`/`context` em cada uma das 100 linhas, sem duplicatas, JSONL válido). Pronto para Phase 5 (Critical Review).
