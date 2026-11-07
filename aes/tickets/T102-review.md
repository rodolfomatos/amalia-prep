---
ticket: T102
title: 5 categorias de latente, 20 exemplos por categoria
phase: review
tier: AES-standard
---

# T102 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim o suficiente | Lógica de distribuição pequena (`divmod` + loop categoria×contador). Sem abstrações especulativas. |
| Está correto para todos os inputs identificados? | Sim | Para `--count` divisível por 5 (100) dá exatamente 20/categoria. Para não divisíveis, distribui o resto nas primeiras categorias ordenadas (documentado no plano). |
| Introduz dívida técnica? | Não | O `import sys` não usado e shebang não-executável são dívida pré-existente, não introduzida por T102. |
| Um colega entende sem perguntar? | Sim | A distribuição é explícita no código (`cat_counts`) e o comentário explica o tratamento do resto. |
| Qual insight vai para o registo de aprendizagem? | - | Distribuição balanceada por categoria exige controle explícito; geração aleatória por seed não garante cotas por categoria. |

## Difstory (resumo da alteração)

Ficheiros alterados: 2
1. `scripts/generate_abduction_data.py`:
   - `generate_example(seed, category=None)`: categoria agora opcional (preserva uso aleatório quando não especificada).
   - `main()`: distribui `args.count` igualmente pelas 5 categorias ordenadas (`divmod` + resto nas primeiras); itera categoria×contador com seed sequencial global.
2. `data/abduction_training.jsonl` (regenerado): 100 linhas, 20/categoria, mesmo schema T101.

O que foi intencionalmente não tocado:
- `eval/test_abduction.py` (contrato executável)
- Campo `latent_variable` de topo (T101) e `ground_truth.latent_variable` (testes)
- `PLAN.md`

Riscos restantes: conteúdo do dataset mudou (exemplos diferentes de T101) — esperado e desejado; 2 erros de ruff pré-existentes.

## Decisão de revisão
✅ APROVADO — T102 cumpre o AC (5 categorias × 20 exemplos = 100, distribuição exata, schema completo, sem duplicatas) e não introduz regressões nem novos erros de lint.

## Acompanhamento (não bloqueia T102)
- T103 (validação formal de JSONL/sem duplicatas) é o próximo de M1; herda este schema e distribuição.
