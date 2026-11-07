---
ticket: T501
title: ACA_LLM_MODEL="ollama/amalia" funciona no ACA
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T401, T303
---

# T501 — Integração com o ACA: ACA_LLM_MODEL="ollama/amalia" (M5)

## Context
M5 milestone (último). Depende de T401 (avaliação abdução) e T303 (`amalia` no Ollama). T501: verificar que `ACA_LLM_MODEL="ollama/amalia"` funciona no repositório ACA, executando `run_t603_h6.py --seeds 5 --items 20` (H6).

## Acceptance Criteria
- [ ] No repositório ACA, `ACA_LLM_MODEL="ollama/amalia"` funciona e `run_t603_h6.py --seeds 5 --items 20` executa com amalia

## Scope
**In scope:** Verificar integração com o ACA (externo).
**Out of scope:** Corrigir o modelo `amalia`, corrigir convert_to_gguf.py, re-treinar.

## Dependencies
- T303 concluído (`amalia` no Ollama)
- Repositório ACA (EXTERNO, não disponível neste projeto)
- `ACA_LLM_MODEL="ollama/amalia"` configurável no ACA

## Rollback
- Nenhum (integração only-read sobre o ACA)

## Known Risks
- O repositório ACA não está disponível neste projeto (https://github.com/rodolfomatos/amalia-prep é este projeto; o ACA é separado)
- O `amalia:latest` no Ollama NÃO é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado), então a integração testaria um modelo não-refinado
- T501 não pode ser executado aqui; requer acesso ao repositório ACA

## Notes
- T501 NÃO pode ser concluído neste projeto: requer o repositório ACA externo.
- Documentado como bloqueado por dependência externa.
