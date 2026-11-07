---
ticket: T203
title: Dataset valido (JSONL, sem duplicatas) — saliencia
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T202
---

# T203 — Dataset válido (JSONL, sem duplicatas, schema válido) — saliência

## Context
Último ticket de M2. Depende de T202 (diversidade de tipos de relação) e T201 (50 exemplos, schema com `relacoes` de topo). T203 AC: 50 linhas, todas únicas, schema válido. Confirmação formal do artefato já produzido por T201/T202.

## Acceptance Criteria
- [ ] 50 linhas no `data/salience_training.jsonl`
- [ ] Todas as linhas únicas (sem duplicatas de id/conteúdo)
- [ ] Schema válido em cada linha: `id`, `conteudo`, `ilhas`, `relacoes` (top-level), `novidade_esperada`, `total_relacoes`, `tipos_relacao`, `ilhas_conectadas`, `ilhas[i].{id,nome,descricao,relacoes[]}`
- [ ] JSONL válido (todas as linhas parseáveis como JSON)

## Scope
**In scope:** Validação formal do dataset `data/salience_training.jsonl` contra o AC acima; documentar o resultado.
**Out of scope:** Alterar o dataset (já válido por T201/T202), criar scripts de validação reutilizáveis (escopo separado), fine-tune (T302).

## Dependencies
- T202 concluído (dataset com 5 tipos de relação)

## Rollback
- Nenhum (validação apenas, sem alteração de ficheiros)

## Known Risks
- Nenhum risco de alteração (ticket só-leitura sobre o dataset). Risco seria o dataset estar inválido, o que bloquearia T302/T402 — já verificado que não é o caso.

## Notes
- T201/T202 já verificaram: 50 linhas, IDs únicos, 5 tipos de relação, schema completo com `relacoes` de topo, JSONL válido
- T203 consolida isso numa validação formal única
