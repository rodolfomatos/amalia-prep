---
ticket: T301
title: Fine-tune qwen3:8b em abdução
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T103
---

# T301 — Fine-tune qwen3:8b em abdução (M3)

## Context
M3 milestone. Depende de T103 (dataset de abdução válido e versionado). Fine-tune QLoRA do qwen3:8b no dataset de abdução. AC: modelo salva, não diverge (loss < 2.0).

## Acceptance Criteria
- [ ] Fine-tune executa e produz modelo salvo (adapter + tokenizer)
- [ ] Loss final < 2.0 (não diverge)
- [ ] Modelo salvo em models/ (não versionado no git — 16 GB+, ver .gitignore)

## Scope
**In scope:** Executar fine-tune QLoRA apenas no dataset de abdução (T301 é abduction-only). Verificar loss < 2.0. Salvar modelo.
**Out of scope:** T302 (salience fine-tune), T303 (registro no Ollama — requer conversão GGUF, convert_to_gguf.py quebrado), avaliação (T401).

## Dependencies
- T103 concluído (data/abduction_training.jsonl válido e versionado)
- Qwen/Qwen3-8B em cache HF local (verificado)
- RTX 5090 + CUDA (verificado)
- scripts/fine_tune.py (existe; precisa de adaptação para single-dataset — ver Phase 1)

## Rollback
- Remover models/amalia-abduction/ se criado; o fine-tune é reprodutível

## Known Risks
- Makefile `BASE=qwen3:8b` está incorreto para `from_pretrained` (espera `Qwen/Qwen3-8B`). Vou passar o ID HF correto diretamente no fine_tune.py, não via `make train` (que faz treino combinado + BASE errada).
- `fine_tune.py` exige ambos `--train-data` e `--salience-data`. Vou torná-lo compatível com single-dataset (fazer salience opcional) para honrar a separação T301/T302 do PLAN.md.
- `convert_to_gguf.py` está quebrado (14 bytes) → não é possível converter o fine-tune para GGUF e registar como `amalia` no Ollama via `make train`/`Modelfile`. Isso afeta T303, não T301. Registrado como gap.
- `amalia:latest` já existe no Ollama (de um run anterior) — não é produto deste fine-tune. T301 produz um adapter próprio.

## Notes
- T301 produz um adapter LoRA em models/amalia-abduction/ (não versionado, .gitignore ignora models/)
- Loss é reportado pelo Trainer (transformers) e verificável nos logs
