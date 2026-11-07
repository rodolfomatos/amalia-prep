---
ticket: T302
title: Fine-tune qwen3:8b em saliência
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T203, T301
---

# T302 — Fine-tune qwen3:8b em saliência relacional (M3)

## Context
M3 milestone. Depende de T203 (dataset de saliência válido) e T301 (suporte single-dataset em fine_tune.py). Fine-tune QLoRA do qwen3:8b no dataset de saliência. AC: modelo salva, não diverge (loss < 2.0).

## Acceptance Criteria
- [ ] Fine-tune executa e produz modelo salvo (adapter + tokenizer)
- [ ] Loss final < 2.0 (não diverge)
- [ ] Modelo salvo em models/ (não versionado no git — 16 GB+, ver .gitignore)

## Scope
**In scope:** Executar fine-tune QLoRA apenas no dataset de saliência (T302 é salience-only). Verificar loss < 2.0. Salvar modelo.
**Out of scope:** T303 (registro no Ollama — convert_to_gguf.py quebrado), avaliação (T402).

## Dependencies
- T203 concluído (data/salience_training.jsonl válido e versionado)
- T301 concluído (fine_tune.py suporta single-dataset via --salience-data opcional)
- Qwen/Qwen3-8B em cache HF local; RTX 5090 + CUDA

## Rollback
- Remover models/amalia-salience/ se criado; reprodutível

## Known Risks
- Batch-size 4 causou CUDA OOM em T301 → usar batch-size 1 + expandable_segments desde o início.
- make train usa BASE=qwen3:8b (incorreto para from_pretrained) → usar ID HF Qwen/Qwen3-8B diretamente.
- convert_to_gguf.py quebrado → não registra no Ollama (afeta T303, não T302).
- amalia:latest ja existe no Ollama (run anterior) — nao e produto deste fine-tune.

## Notes
- T302 produz adapter LoRA em models/amalia-salience/ (nao versionado, models/ ignorado)
