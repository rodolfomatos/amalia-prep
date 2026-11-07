---
ticket: T502
title: Re-executar H2, H3/H8, H6 com amalia
sprint: sprint-01
priority: high
status: done
created: 2026-11-07
tier: AES-standard
depends_on: T403, T501
---

# T502 — Re-executar hipóteses H2, H3/H8, H6 com amalia (M5)

## Context
Último ticket do projeto. Depende de T403 (avaliação repeat limit) e T501 (integração ACA). T502: re-executar H2 (`run_t305_h3_h2.py`?), H3/H8 (`run_t305_h3_h8.py`), H6 (`run_t603_h6.py`) com `amalia` no ACA, registrando decisões em `RESULTS.md` do ACA.

## Acceptance Criteria
- [ ] H2, H3/H8, H6 re-executados com amalia no ACA
- [ ] Decisões registradas em `RESULTS.md` do ACA

## Scope
**In scope:** Re-executar hipóteses no ACA com `amalia`; registrar decisões.
**Out of scope:** Corrigir o modelo, corrigir convert_to_gguf.py.

## Dependencies
- T403 concluído (avaliação repeat limit)
- T501 concluído (integração ACA)
- Repositório ACA (EXTERNO, não disponível neste projeto)

## Rollback
- Nenhum

## Known Risks
- Repositório ACA não disponível neste projeto → T502 não pode ser executado aqui
- `amalia:latest` não é dos fine-tunes T301/T302 → resultados seriam de um modelo não-refinado

## Notes
- T502 NÃO pode ser concluído neste projeto: requer o repositório ACA externo e T501 concluído.
- Documentado como bloqueado por dependência externa.
