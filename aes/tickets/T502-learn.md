---
ticket: T502
title: Re-executar H2, H3/H8, H6 com amalia
phase: learn
tier: AES-standard
---

# T502 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T502 é o último ticket do projeto (M5). Verifiquei que depende do repositório ACA (externo, não disponível) e de T501 (também bloqueado), então T502 não pode ser executado aqui. Documentei o bloqueio com evidência.

## O que correu bem
- O bloqueio foi identificado e documentado em ambos os tickets de M5 (T501 e T502).
- A cadeia de dependência (T502 → T501 → ACA externo) está clara.

## O que correu mal / pode melhorar
- M5 não pode ser concluído sem o repositório ACA.
- Mesmo com o ACA, o `amalia:latest` não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado).

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Dependência externa não resolvida
> **Insight**: O último marco de um projeto pode ficar bloqueado por dependências externas (repositórios, serviços, credenciais) que estão fora do controle do projeto. Documentar o bloqueio com evidência, em vez de assumir ou mascarar, preserva a integridade do rastreamento.
> **Origem**: T502 (Phase 1 hostile analysis).
> **Impacto**: M5 não pode ser concluído sem o repositório ACA.
> **Aplicado a**: T501, T502; relevante para qualquer projeto com integrações externas.
> **Data**: 2026-11-07

## Marco M5 e projeto — resultado final
T501 (integração ACA) — BLOQUEADO (repositório ACA externo não disponível).
T502 (re-executar hipóteses com amalia) — BLOQUEADO (depende de T501 e do ACA).
O projeto Amália-prep chega ao fim dos tickets que podem ser executados localmente. M5 requer acesso ao repositório ACA externo.
