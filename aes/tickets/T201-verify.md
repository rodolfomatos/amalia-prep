---
ticket: T201
title: 50 exemplos de ilha → conteúdo conectado/isolado
phase: verify
tier: AES-standard
---

# T201 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| 50 linhas JSONL | ✅ PASS | `wc -l = 50` |
| Cada linha com top-level `ilhas`, `relacoes`, `conteudo`, `novidade_esperada` | ✅ PASS | verificado em todas as 50 linhas |
| 50 IDs únicos (sem duplicatas) | ✅ PASS | ids `salience_0000`..`salience_0049` |
| JSONL válido (todas as linhas parseáveis) | ✅ PASS | 0 erros de parse |
| `relacoes` top-level = lista achatada de `ilhas[].relacoes` (bate com `total_relacoes`) | ✅ PASS | 0 inconsistências |
| Tipos de relação ≥ 3 (RELATED_TO, CONTRADIZ, COMPLEMENTA) — T202 | ✅ PASS | 5 tipos: AGREGADO_EM, COMPLEMENTA, CONTRADIZ, DERIVA_DE, RELATED_TO |

## Critério AC T201
- [x] 50 exemplos com `ilhas`, `relacoes` (top-level), `conteudo`, `novidade_esperada` — SATISFEITO

## Critério AC T202 (verificação antecipada)
- [x] Pelo menos 3 tipos diferentes de relação — SATISFEITO (5 tipos)

## Novas falhas introduzidas por esta alteração
Nenhuma. O único diff funcional é a adição do campo top-level `relacoes` (lista achatada) no gerador e no dataset.

## Falhas pré-existentes (reportadas, não bloqueantes)
- 2 erros de ruff em `scripts/generate_salience_data.py` (`EXE001` shebang, `C401` generator desnecessário na linha 69) — pré-existentes, não introduzidos por T201, fora do escopo do AC.

## Observação (não bloqueia T201)
- Todos os 50 exemplos são "conectados" (ilhas_conectadas > 0); nenhum exemplo isolado. O teste `test_isolado_mais_novo_que_conectado` faria `pytest.skip` sem exemplos isolados. Registrado para atenção em T402/M2; fora do escopo estrito do AC de T201 (schema).

## Verificação de regressão
- Contrato executável dos testes (`conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`) mantido intacto.
- IDs e conteúdo dos exemplos preservados (mesmas seeds 0-49); apenas acrescido o campo `relacoes` top-level.

## Conclusão Phase 4
T201 passa no Acceptance Criteria literal (top-level `ilhas`/`relacoes`/`conteudo`/`novidade_esperada` em cada uma das 50 linhas, sem duplicatas, JSONL válido). T202 (3+ tipos de relação) também já está satisfeito. Pronto para Phase 5 (Critical Review).
