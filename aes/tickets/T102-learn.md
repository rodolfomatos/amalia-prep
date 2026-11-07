---
ticket: T102
title: 5 categorias de latente, 20 exemplos por categoria
phase: learn
tier: AES-standard
---

# T102 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
O dataset de abdução tinha 100 exemplos mas distribuição desbalanceada (23/19/17/20/21), violando o AC de T102 (20 exemplos por cada uma das 5 categorias). Modifiquei `scripts/generate_abduction_data.py` para distribuir `--count` igualmente pelas categorias ordenadas (`divmod` + resto nas primeiras) e regenerei o dataset com `--count 100` → exatamente 20/categoria. Preservei o schema de T101 (`latent_variable` de topo) e o contrato dos testes (`ground_truth.latent_variable`).

## O que correu bem
- Hostile analysis antecipou que geração aleatória por seed não garante cotas por categoria.
- Alteração cirúrgica e determinística (mesma seed → mesmo exemplo; distribuição controlada).
- Sem regressões: schema T101 e contrato de testes preservados; nenhum erro de lint novo.

## O que correu mal / pode melhorar
- 2 erros de ruff pré-existentes no gerador (shebang não-executável, `import sys` não usado). Tech debt separado.
- O conteúdo do dataset mudou em relação a T101 — esperado, mas deve-se notar que re-executar `make data` agora produz distribuição balanceada (comportamento intencional).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Geração de dados sintéticos / cotas por categoria
> **Insight**: Para datasets de fine-tune com exigência de equilíbrio entre classes/categorias, a geração aleatória por seed não é suficiente; é necessário controle explícito de distribuição (contagem por categoria) no gerador, senão o fine-tune (T301) e a avaliação (T401) ficam desbalanceados.
> **Origem**: Hostile analysis de T102 (Phase 1).
> **Impacto**: Mitigado distribuindo `--count` igualmente pelas categorias no gerador.
> **Aplicado a**: T102; relevante para T201-T203 (saliência, que também exige tipos de relação balanceados) e T301/T401.
> **Data**: 2026-11-07

## Próximo ticket na sequência
T103 (validação formal: JSONL válido, 100 linhas únicas, schema válido), depois M2 (T201-T203, saliência relacional).
