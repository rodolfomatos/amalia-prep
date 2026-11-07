---
ticket: T201
title: 50 exemplos de ilha → conteúdo conectado/isolado
phase: review
tier: AES-standard
---

# T201 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim o suficiente | Alteração mínima: 1 linha no gerador (`"relacoes": [r for ilha in islands for r in ilha["relacoes"]]`) + regeneração do dataset. |
| Está correto para todos os inputs identificados? | Sim | Todas as 50 linhas têm os 4 campos top-level; `relacoes` achatado bate com `total_relacoes`; testes não quebram. |
| Introduz dívida técnica? | Não | Campo achatado espelha `total_relacoes`/`tipos_relacao` já existentes; pequena redundância justificada pelo AC literal. Os 2 erros de ruff são pré-existentes. |
| Um colega entende sem perguntar? | Sim | O campo `relacoes` top-level fica ao lado de `ilhas` e `conteudo`, espelhando as relações já contadas em `total_relacoes`. |
| Qual insight vai para o registo de aprendizagem? | - | Mesma contradição de schema de T101 (PLAN.md top-level vs código aninhado) reaparece em M2; resolvida da mesma forma (espelhar campo no nível top-level sem quebrar o contrato executável). |

## Difstory (resumo da alteração)

Ficheiros alterados: 2
1. `scripts/generate_salience_data.py` (+1 linha): `generate_example` devolve agora `"relacoes": [r for ilha in islands for r in ilha["relacoes"]]` no nível superior (lista achatada de todas as relações das ilhas do exemplo).
2. `data/salience_training.jsonl` (regenerado): 50 linhas, mesmo conteúdo (seeds 0-49) + campo `relacoes` top-level.

O que foi intencionalmente não tocado:
- `eval/test_salience.py` (contrato executável)
- `ilhas[i].relacoes` aninhado (estrutura de ilhas, usada pelos testes)
- `PLAN.md`
- Adição de exemplos isolados (observação para T402, fora do escopo de T201)

Riscos restantes: campo achatado (pequena redundância); 2 erros de ruff pré-existentes; ausência de exemplos isolados (observação).

## Decisão de revisão
✅ APROVADO — T201 cumpre o AC literal (top-level `ilhas`/`relacoes`/`conteudo`/`novidade_esperada` nas 50 linhas, sem duplicatas, JSONL válido) e preserva o contrato executável dos testes.

## Acompanhamento (não bloqueia T201)
- Os 2 erros de ruff em `scripts/generate_salience_data.py` podem entrar como tech debt separado.
- Ausência de exemplos isolados: observar em T402 (o teste de isolado-vs-conectado fará skip sem isolados).
- T203 (validação formal JSONL/sem duplicatas) é o próximo de M2 e herda este schema.
