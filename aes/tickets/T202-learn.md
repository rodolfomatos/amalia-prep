---
ticket: T202
title: Ilhas com múltiplos tipos de relação (≥3 tipos)
phase: learn
tier: AES-standard
---

# T202 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T202 foi um ticket de confirmação: o gerador `scripts/generate_salience_data.py` já definia 5 tipos de relação (`RELATION_TYPES` com RELATED_TO, CONTRADIZ, COMPLEMENTA, DERIVA_DE, AGREGADO_EM) e o dataset `data/salience_training.jsonl` já continha todos os 5 (verificado no T201). Executei uma confirmação formal contando os tipos distintos no dataset: 5 tipos, satisfazendo o AC de ≥3 incluindo os 3 nomeados. Zero alterações de código.

## O que correu bem
- T202 confirmou que a diversidade de tipos de relação exigida por M2 já está presente no gerador e no dataset.
- Confirmação documentada com evidência empírica (contagem por tipo).

## O que correu mal / pode melhorar
- Não há validação automática de tipos ligada a `make check`/`make data`; uma regeneração futura poderia, em tese, perder diversidade (improvável com 5 tipos e múltiplas relações por exemplo). Registrado como observação.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Diversidade de classes em dados sintéticos
> **Insight**: Para tarefas de classificação/relação (saliência), é importante confirmar que o dataset sintético cobre todas as classes exigidas pelo AC, não apenas assumir que o gerador as produz. A confirmação empírica (contagem real) é mais confiável que a suposição.
> **Origem**: T202 (Phase 1 hostile analysis).
> **Impacto**: Mitigado por contagem empírica dos 5 tipos.
> **Aplicado a**: T202; relevante para T402 (avaliação de saliência) e qualquer dataset sintético futuro.
> **Data**: 2026-11-07

## Marco M2 em andamento
T201 (dataset com schema `relacoes` de topo) — done. T202 (≥3 tipos de relação) — done.
Próximo: T203 (validação formal: 50 linhas únicas, JSONL válido, schema válido) — conclui M2.
