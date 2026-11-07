---
ticket: T203
title: Dataset valido (JSONL, sem duplicatas) — saliencia
phase: learn
tier: AES-standard
---

# T203 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T203 foi um ticket de validação de confirmação: o dataset de saliência (`data/salience_training.jsonl`) já havia sido gerado com schema correto (T201: `relacoes` de topo) e diversidade de tipos de relação (T202: 5 tipos). Executei uma validação formal one-off confirmando 50 linhas, todas únicas, schema válido em cada linha, JSONL válido. Zero erros.

## O que correu bem
- Separação de preocupações: geração (T201/T202) vs validação (T203) feita como tickets distintos.
- Cada validação documentada nos seus próprios outputs (plan/verify/review/learn) — rastreabilidade completa.
- O dataset está pronto para consumo por T302 (fine-tune QLoRA de saliência) e T402 (avaliação de saliência relacional).

## O que correu mal / pode melhorar
- Não há um script de validação reutilizável; futuras execuções de `make data` regenerariam o dataset sem validação automática. Registado como sugestão de backlog (fora do escopo de T203).
- Observação de T201: todos os 50 exemplos são "conectados" (nenhum isolado). Isso afeta o teste `test_isolado_mais_novo_que_conectado` (faria `pytest.skip`) e deve ser observado em T402.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Validação de artefatos de dados (padrão recorrente — mesmo que T103)
> **Insight**: Em pipelines de ML, separar a geração de dados da sua validação formal (tickets distintos) melhora a rastreabilidade e permite confirmar o AC de cada etapa independentemente. Sem validação automática ligada a `make data`, uma regeneração posterior pode silenciosamente produzir um dataset inválido.
> **Origem**: T203 (Phase 1 hostile analysis), consistente com T103.
> **Impacto**: Mitigado por documentação explícita; sugestão de backlog para validação automática.
> **Aplicado a**: T103 e T203; relevante para qualquer regeneração de dataset no projeto.
> **Data**: 2026-11-07

## Marco M2 concluído
T201 (50 exemplos + schema `relacoes` de topo), T202 (≥3 tipos de relação), T203 (validação formal) — todos done.
Próximo: M3 (T301-T303, fine-tune QLoRA do qwen3:8b), que requer GPU NVIDIA e tempo de treino.
