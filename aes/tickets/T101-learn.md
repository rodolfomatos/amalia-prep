---
ticket: T101
title: 100 exemplos de observação → mecanismo latente
phase: learn
tier: AES-standard
---

# T101 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
O dataset de abdução já existia com 100 exemplos, mas não satisfazia o AC literal do PLAN.md T101 (cada exemplo deve ter top-level `latent_variable`, `observation`, `context`): o `latent_variable` estava apenas aninhado em `ground_truth`. Adicionei o campo top-level `latent_variable` (espelhando `ground_truth.latent_variable`) ao gerador e regenerei o dataset (mesmas seeds → mesmo conteúdo + novo campo), para que o dataset satisfaça o AC literal sem quebrar o contrato executável dos testes (`eval/test_abduction.py` lê `ground_truth.latent_variable`).

## O que correu bem
- Hostile analysis surfou a contradição de schema (PLAN.md vs código vs testes) antes de qualquer alteração.
- Alteração cirúrgica: 1 linha no gerador + regeneração do dataset; nenhum outro ficheiro tocado.
- Contrato executável preservado: testes continuam a ler `ground_truth.latent_variable`.

## O que correu mal / pode melhorar
- 2 erros de ruff pré-existentes em `scripts/generate_abduction_data.py` (`EXE001` shebang, `F401` `import sys` não usado). Não são da responsabilidade de T101, mas deixam o gerador sem `make lint` verde.
- Não há validação formal de schema/unicidade automatizada (será T103).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Consistência de schema / contrato documento-vs-código
> **Insight**: Em projetos de ML, o AC da documentação (PLAN.md) pode divergir do schema que o código e os testes realmente usam. Nunca "consertar silenciosamente" um dos lados; surfear a contradição na hostile analysis e escolher a opção que preserva o contrato executável (testes) enquanto satisfaz o AC documentado (adicionando o campo faltante nos dois níveis).
> **Origem**: Hostile analysis de T101 (Phase 1).
> **Impacto**: Mitigado espelhando `latent_variable` em nível top-level e em `ground_truth`.
> **Aplicado a**: T101; relevante para T102/T103 (mesmo schema) e T301/T401 (consumem o dataset).
> **Data**: 2026-11-07

## Próximo ticket na sequência
T102 (5 categorias, 20 exemplos por categoria — validação de distribuição no dataset existente), depois T103 (validação formal JSONL/sem duplicatas), depois M2 (T201-T203, saliência relacional).
