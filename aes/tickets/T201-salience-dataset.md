---
ticket: T201
title: 50 exemplos de ilha → conteúdo conectado/isolado
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T001
---

# T201 — 50 exemplos de ilha → conteúdo conectado/isolado (dataset saliência)

## Context
M2 milestone. Depende de T001 (ambiente). Gera o dataset sintético de saliência relacional usado para fine-tune (T302) e avaliação (T402). O gerador já existe em `scripts/generate_salience_data.py` e o dataset já tem 50 linhas, mas há uma contradição de schema a resolver (ver Phase 1), idêntica em natureza à de T101.

## Acceptance Criteria
- [ ] 50 exemplos, cada um com `ilhas`, `relacoes` (top-level), `conteudo`, `novidade_esperada` (AC literal do PLAN.md T201)
- [ ] Ilhas com múltiplos tipos de relação: pelo menos 3 tipos diferentes (RELATED_TO, CONTRADIZ, COMPLEMENTA) — T202 (escopo separado, mas schema deve permitir)
- [ ] Dataset válido (JSONL, sem duplicatas): 50 linhas, todas únicas, schema válido — T203 (escopo separado)

## Scope
**In scope:** Garantir que `data/salience_training.jsonl` satisfaça o AC literal de T201 (top-level `relacoes` em cada exemplo), sem quebrar o contrato executável dos testes (`eval/test_salience.py` lê `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`, não top-level `relacoes`).
**Out of scope:** T202 (contagem de tipos de relação), T203 (validação de duplicatas/schema formal), fine-tune (T302), avaliação (T402).

## Dependencies
- T001 concluído (ambiente com Python + deps)
- `scripts/generate_salience_data.py` existente
- `eval/test_salience.py` (contrato executável — não quebrar)

## Rollback
- Restaurar `data/salience_training.jsonl` e `scripts/generate_salience_data.py` do commit anterior (6f8d3b75)

## Known Risks
- Adicionar campo `relacoes` top-level (lista achatada de todas as relações do exemplo) — espelha `total_relacoes`/`tipos_relacao` já existentes; necessário para satisfazer o AC literal sem quebrar testes
- Regenerar o dataset altera conteúdo (mesmas seeds → mesmo conteúdo + novo campo)

## Notes
- Dados já existem: 50 linhas, geradas com seeds 0-49
- Schema atual: `id, conteudo, ilhas[].{id,nome,descricao,relacoes[]}, novidade_esperada, total_relacoes, tipos_relacao, ilhas_conectadas`
- Falta para AC literal: top-level `relacoes`
- Todos os 50 exemplos são "conectados" (ilhas_conectadas > 0); nenhum isolado — observação para T402 (o teste `test_isolado_mais_novo_que_conectado` faria `pytest.skip` sem isolados)
