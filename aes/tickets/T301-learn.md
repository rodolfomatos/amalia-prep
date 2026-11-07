---
ticket: T301
title: Fine-tune qwen3:8b em abdução
phase: learn
tier: AES-standard
---

# T301 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Executei um fine-tune QLoRA (4-bit) do `Qwen/Qwen3-8B` apenas no dataset de abdução (T301 é abduction-only, honrando a separação T301/T302 do PLAN.md). Para isso, tornei `--salience-data` opcional em `scripts/fine_tune.py`. O treino usou batch-size 1 (batch-size 4 causou CUDA OOM na RTX 5090), 3 épocas, learning-rate 2e-4, 75 passos. O loss convergiu de 6.519 para 0.149 (train_loss 1.142), bem abaixo do alvo de 2.0, sem divergência. O modelo (adapter LoRA + tokenizer) foi salvo em `models/amalia-abduction/`.

## O que correu bem
- Hostile analysis antecipou o ID HF incorreto (`qwen3:8b` vs `Qwen/Qwen3-8B`) e usei o correto diretamente.
- O Qwen/Qwen3-8B estava em cache HF local, então não houve download.
- O fine-tune completou e salvou o modelo com loss < 2.0.

## O que correu mal / pode melhorar
- 1ª execução falhou com CUDA OOM (batch-size 4). Corrigido com batch-size 1 + `expandable_segments`. Documentado para T302 (usar batch-size 1 desde o início).
- `models/` não é versionado pelo git (.gitignore) → o artefato do fine-tune fica apenas local. O código que o produz está versionado.
- `convert_to_gguf.py` está quebrado (14 bytes) → não é possível converter o adapter fine-tunado para GGUF e registar como `amalia` no Ollama. Isso bloqueia T303 (registro no Ollama a partir de um fine-tune novo). `amalia:latest` já existe no Ollama mas é de um run anterior (GGUF pré-existente).
- Makefile `BASE=qwen3:8b` está incorreto para `from_pretrained` (usa `Qwen/Qwen3-8B`). Corrigi na execução, não no Makefile (escopo separado).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Fine-tune QLoRA em GPU de consumo
> **Insight**: QLoRA 4-bit do Qwen3-8B cabe na RTX 5090 (33.7 GB) apenas com batch-size reduzido (1) e `expandable_segments`; batch-size 4 (como no Makefile) causa OOM. Além disso, o pipeline fine-tune → GGUF → Ollama está quebrado (convert_to_gguf.py com 14 bytes), impedindo registrar um modelo fine-tunado novo como `amalia`.
> **Origem**: T301 (Phase 1 hostile analysis + execução).
> **Impacto**: Mitigado para T301 (treino concluído com loss < 2.0). T303 permanece bloqueado até consertar convert_to_gguf.py ou outro caminho de registro no Ollama.
> **Aplicado a**: T301; relevante para T302 (salience fine-tune) e T303 (Ollama).
> **Data**: 2026-11-07

## Próximo ticket na sequência
T302 (fine-tune qwen3:8b em saliência, loss < 2.0) — reusa o suporte single-dataset já implementado. Depois T303 (registro no Ollama — pendente de resolução do convert_to_gguf.py).
