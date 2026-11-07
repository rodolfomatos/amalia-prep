---
ticket: T501
title: ACA_LLM_MODEL="ollama/amalia" funciona no ACA
phase: review
tier: AES-standard
---

# T501 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Documentação de bloqueio por dependência externa. |
| Está correto para todos os inputs identificados? | Sim | Sem acesso ao ACA, T501 não pode ser executado. |
| Introduz dívida técnica? | Não | Sem alteração de código. Bloqueio é de dependência externa. |
| Um colega entende sem perguntar? | Sim | O bloqueio (ACA não disponível) e a causa (projeto separado) estão documentados. |
| Qual insight vai para o registo de aprendizagem? | - | Tickets de integração com repositórios externos requerem acesso prévio; documentar bloqueios é mais honesto que mascarar. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (documentação de bloqueio).

## Decisão de revisão
❌ NÃO PODE SER EXECUTADO — T501 está bloqueado por dependência externa (repositório ACA não disponível). O AC não pode ser verificado aqui. Não mascarado.

## Acompanhamento (bloqueia conclusão do projeto)
- Para concluir M5: acessar o repositório ACA, configurar `ACA_LLM_MODEL="ollama/amalia"`, executar `run_t603_h6.py --seeds 5 --items 20`, depois T502.
- Também recomendado: corrigir `convert_to_gguf.py` para que o `amalia` no ACA seja o modelo fine-tunado (T301/T302), não um run anterior.
