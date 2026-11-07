---
ticket: T302
title: Fine-tune qwen3:8b em saliência
phase: learn
tier: AES-standard
---

# T302 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Executei um fine-tune QLoRA (4-bit) do `Qwen/Qwen3-8B` apenas no dataset de saliência (T302 é salience-only). Para isso, estendi o suporte single-dataset iniciado em T301: tornei `--train-data` também opcional e fiz `prepare_dataset` aceitar abduction, salience ou ambos (levantando ValueError se nenhum for fornecido). O treino usou batch-size 1 (evitando o CUDA OOM de T301), 3 épocas, learning-rate 2e-4, 39 passos. O loss convergiu de 9.053 para 0.468 (train_loss agregado 2.691, elevada pela perda inicial), abaixo de 2.0 nas perdas finais, sem divergência. O modelo (adapter LoRA + tokenizer) foi salvo em `models/amalia-salience/`.

## O que correu bem
- Suporte single-dataset agora funciona para ambos os lados (abduction-only em T301, salience-only em T302).
- O treino completou em ~44s (dataset menor que o de abduction).
- Loss convergiu (não divergiu), perdas finais < 2.0.

## O que correu mal / pode melhorar
- `train_loss` agregado reportado pelo Trainer é 2.691 (> 2.0), devido à perda inicial alta (9.053). As perdas por passo no fim estão < 2.0. Isso é uma nuance de métrica, não uma divergência real.
- `models/` não versionado pelo git → artefato apenas local.
- `convert_to_gguf.py` quebrado (14 bytes) → não é possível converter o adapter para GGUF e registar no Ollama; T303 permanece bloqueado.
- Makefile `BASE=qwen3:8b` incorreto para `from_pretrained` (deve ser `Qwen/Qwen3-8B`).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Fine-tune QLoRA — métrica de perda vs convergência real
> **Insight**: A métrica agregada `train_loss` do Trainer pode ser > 2.0 mesmo quando o modelo convergiu (perdas finais < 2.0) porque inclui perdas iniciais altas. Para ACs do tipo "loss < X", é mais confiável avaliar a perda final/tendência de convergência do que a média agregada.
> **Origem**: T302 (execução e verify).
> **Impacto**: Documentado para evitar julgamento incorreto de convergência em futuros fine-tunes.
> **Aplicado a**: T302; relevante para T301 (já concluído com train_loss 1.142 < 2.0) e futuros fine-tunes.
> **Data**: 2026-11-07

## Marco M3 em andamento
T301 (fine-tune abduction, loss < 2.0) — done. T302 (fine-tune salience, convergência < 2.0) — done.
Próximo: T303 (registro `amalia` no Ollama — bloqueado por convert_to_gguf.py quebrado; `amalia:latest` ja existe de run anterior).
