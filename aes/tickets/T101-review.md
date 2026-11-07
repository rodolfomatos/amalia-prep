---
ticket: T101
title: 100 exemplos de observação → mecanismo latente
phase: review
tier: AES-standard
---

# T101 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim o suficiente | Alteração mínima: 1 linha no gerador (`"latent_variable": latent`) + regeneração do dataset. Sem abstrações especulativas. |
| Está correto para todos os inputs identificados? | Sim | Todas as 100 linhas têm os 3 campos top-level; `ground_truth.latent_variable` preservado; testes não quebram. |
| Introduz dívida técnica? | Não | Campo espelhado é pequena redundância justificada por satisfazer o AC literal do PLAN.md. Os 2 erros de ruff são pré-existentes. |
| Um colega entende sem perguntar? | Sim | O campo `latent_variable` top-level fica ao lado de `observation` e `context`, espelhando o que já existe em `ground_truth`. |
| Qual insight vai para o registo de aprendizagem? | - | Contradição entre PLAN.md (schema top-level) e código/testes (schema nested `ground_truth`); resolvida espelhando o campo nos dois níveis sem quebrar o contrato executável. |

## Difstory (resumo da alteração)

Ficheiros alterados: 2
1. `scripts/generate_abduction_data.py` (+1 linha): `generate_example` devolve agora `"latent_variable": latent` no nível superior do dict.
2. `data/abduction_training.jsonl` (regenerado): 100 linhas, mesmo conteúdo (seeds 0-99) + campo `latent_variable` top-level.

O que foi intencionalmente não tocado:
- `eval/test_abduction.py` (contrato executável, lê `ground_truth.latent_variable`)
- `PLAN.md` (a contradição de schema fica documentada na hostile analysis do ticket)
- Outros campos (`mechanism`, `category`, `id`) — inalterados

Riscos restantes: campo duplicado (pequena redundância); 2 erros de ruff pré-existentes no gerador.

## Decisão de revisão
✅ APROVADO — T101 cumpre o AC literal (top-level `observation`/`latent_variable`/`context` nas 100 linhas, sem duplicatas, JSONL válido) e preserva o contrato executável dos testes.

## Acompanhamento (não bloqueia T101)
- Os 2 erros de ruff em `scripts/generate_abduction_data.py` podem entrar como tech debt separado.
- T102 (20 exemplos por categoria) e T103 (validação formal de duplicatas/schema) são os próximos tickets de M1 e herdam este schema.
