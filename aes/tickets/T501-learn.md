---
ticket: T501
title: ACA_LLM_MODEL="ollama/amalia" funciona no ACA
phase: learn
tier: AES-standard
---

# T501 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T501 é um ticket de integração com o repositório ACA (externo). Verifiquei que o ACA não está disponível neste projeto (amalia-prep é separado do ACA), então T501 não pode ser executado aqui. Documentei o bloqueio com evidência.

## O que correu bem
- O bloqueio foi identificado e documentado honestamente, não mascarado.
- Ficou claro que M5 depende de acesso externo (repositório ACA).

## O que correu mal / pode melhorar
- T501 não pode ser concluído sem o repositório ACA.
- O `amalia:latest` disponível não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado), então mesmo com o ACA, a integraria testaria um modelo não-refinado.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Integração com repositório externo
> **Insight**: Tickets que dependem de repositórios/serviços externos não podem ser concluídos sem acesso prévio a esses recursos. O bloqueio deve ser documentado com evidência, não assumido ou mascarado.
> **Origem**: T501 (Phase 1 hostile analysis).
> **Impacto**: M5 não pode ser concluído sem o repositório ACA.
> **Aplicado a**: T501, T502; relevante para qualquer integração externa futura.
> **Data**: 2026-11-07

## Próximo ticket na sequência
T502 (re-executar H2, H3/H8, H6 com amalia no ACA) — também bloqueado pela mesma dependência externa e por T501.
