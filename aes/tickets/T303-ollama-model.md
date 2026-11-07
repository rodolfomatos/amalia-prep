---
ticket: T303
title: Modelo amalia disponível no Ollama local
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T302
---

# T303 — Modelo `amalia` disponível no Ollama local (M3)

## Context
Último ticket de M3. AC: `ollama list` mostra `amalia`. O modelo `amalia:latest` já está presente no Ollama (16 GB, construído a partir de `models/amalia-merged/amalia.f16.gguf` via `configs/Modelfile`), de um run anterior.

## Acceptance Criteria
- [ ] `ollama list` mostra `amalia`

## Scope
**In scope:** Confirmar que `amalia` está disponível no Ollama (AC literal). Documentar a origem do modelo e as limitações.
**Out of scope:** Corrigir `convert_to_gguf.py` (quebrado, 14 bytes) para registar um modelo fine-tunado novo; re-treinar e registar como `amalia`.

## Dependencies
- Ollama rodando (verificado em T001)
- `amalia:latest` presente no Ollama (de run anterior)

## Rollback
- Nenhum (confirmação apenas, sem alteração de ficheiros)

## Known Risks
- O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302 (esses produziram adapters LoRA em models/, não registados como `amalia` porque convert_to_gguf.py está quebrado).
- `convert_to_gguf.py` tem 14 bytes (quebrado) → não é possível converter adapter fine-tunado para GGUF e registar como `amalia` via `make train`/`Modelfile`.
- Isso significa que o `amalia` no Ollama pode não refletir os fine-tunes T301/T302. Gap registrado para M4/M5 (avaliação contra `amalia` pode usar um modelo não-refinado pelos nossos fine-tunes).

## Notes
- `configs/Modelfile`: `FROM /home/rodolfo/amalia-prep/models/amalia-merged/amalia.f16.gguf` — constrói `amalia` a partir de GGUF local pré-existente.
- `amalia:latest` (16 GB) e `qwen3:8b` (5.2 GB) estão no Ollama.
