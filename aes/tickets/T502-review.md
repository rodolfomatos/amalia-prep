---
ticket: T502
title: Re-executar H2, H3/H8, H6 com amalia
phase: review
tier: AES-standard
---

# T502 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Documentação de bloqueio por dependência externa. |
| Está correto para todos os inputs identificados? | Sim | Sem ACA nem T501, T502 não pode ser executado. |
| Introduz dívida técnica? | Não | Sem alteração de código. |
| Um colega entende sem perguntar? | Sim | O bloqueio está documentado com causa (ACA externo, T501 bloqueado). |
| Qual insight vai para o registo de aprendizagem? | - | Tickets em cadeia (T502 depende de T501) herdam bloqueios; documentar cada um é importante para rastreabilidade. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (documentação de bloqueio).

## Decisão de revisão
❌ NÃO PODE SER EXECUTADO — T502 está bloqueado por dependência externa (repositório ACA) e por T501 (também bloqueado). Não mascarado.

## Acompanhamento (bloqueia conclusão do projeto)
- Para concluir M5: acessar o repositório ACA, concluir T501, depois executar T502 (re-executar H2/H3/H8/H6 com amalia, registar em RESULTS.md do ACA).
- Recomendado: corrigir convert_to_gguf.py para que o `amalia` usado no ACA seja o modelo fine-tunado (T301/T302).
