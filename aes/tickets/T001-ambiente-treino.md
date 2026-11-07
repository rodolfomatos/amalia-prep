---
ticket: T001
title: Ambiente de treino (Ollama + Python + deps)
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
---

# T001 — Ambiente de treino (Ollama + Python + deps)

## Context
M0 milestone. Pré-requisito de todos os tickets seguintes (T101 precisa do ambiente para gerar dados; T301 precisa do ambiente para treinar). O `Makefile` target `setup` deve criar o virtualenv, instalar dependências e verificar que o Ollama está rodando.

## Acceptance Criteria
- [ ] `make setup` roda sem erros (exit code 0)
- [ ] `.venv` criado com Python 3.12+
- [ ] `pip install -r requirements.txt` instala torch, transformers, peft, bitsandbytes, datasets, accelerate, ruff, pytest
- [ ] Ollama responde a `ollama list` (servidor rodando)

## Scope
**In scope:** Corrigir/verificar o target `make setup` do Makefile para que rode limpo e deixe o ambiente pronto.
**Out of scope:** Gerar datasets (T101-T103), executar fine-tune (T301-T303), publicar modelo (push).

## Dependencies
- Python 3.12+ disponível no sistema
- Ollama instalado e com `ollama serve` rodando
- Conexão à internet para pip install (ou cache no .venv)

## Rollback
- Remover `.venv` e recriar; desinstalar pacotes pip problemáticos

## Known Risks
- `bitsandbytes` pode falhar na compilação sem CUDA/GPU drivers
- Ollama pode não estar rodando (target falha na verificação `ollama list`)
- requirements.txt sem versões fixas → builds não reprodutíveis

## Notes
- .venv já existe no working tree (criado anteriormente). Verificar se está funcional.
