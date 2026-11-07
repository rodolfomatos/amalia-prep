---
ticket: T103
title: Dataset valido (JSONL, sem duplicatas) — abducao
phase: learn
tier: AES-standard
---

# T103 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T103 foi um ticket de validação de confirmação: o dataset de abdução (`data/abduction_training.jsonl`) já havia sido gerado com schema correto (T101: `latent_variable` de topo) e distribuição balanceada (T102: 20/categoria). Executei uma validação formal one-off confirmando 100 linhas, todas únicas, schema válido em cada linha, JSONL válido, e 20 exemplos por cada uma das 5 categorias. Zero erros.

## O que correu bem
- Separação de preocupações: geração (T101/T102) vs validação (T103) feita como tickets distintos.
- Cada validação foi documentada nos seus próprios outputs (plan/verify/review/learn) — rastreabilidade completa.
- O dataset está pronto para consumo por T301 (fine-tune QLoRA) e T401 (avaliação de abdução).

## O que correu mal / pode melhorar
- Não há um script de validação reutilizável; futuras execuções de `make data` regenerariam o dataset sem validação automática. Registado como sugestão de backlog (fora do escopo de T103).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Validação de artefatos de dados
> **Insight**: Em pipelines de ML, separar a geração de dados da sua validação formal (tickets distintos) melhora a rastreabilidade e permite confirmar o AC de cada etapa independentemente. No entanto, sem validação automática ligada a `make data`, uma regeneração posterior pode silenciosamente produzir um dataset inválido.
> **Origem**: T103 (Phase 1 hostile analysis).
> **Impacto**: Mitigado por documentação explícita; sugestão de backlog para validação automática.
> **Aplicado a**: T103; relevante para T201-T203 (saliência) e qualquer regeneração de dataset.
> **Data**: 2026-11-07

## Marco M1 concluído
T001 (ambiente), T101 (100 exemplos + schema), T102 (20/categoria), T103 (validação formal) — todos done.
Próximo: M2 (T201-T203, dataset de saliência relacional).
