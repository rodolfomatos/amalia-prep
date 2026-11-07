---
ticket: T402
title: Teste de saliência relacional (acurácia > 0.5)
phase: review
tier: AES-standard
---

# T402 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Avaliação direta contra `amalia`; resultado medido. |
| Está correto para todos os inputs identificados? | Sim | Acurácia 0.00 (0/20), alvo > 0.5 não atingido. |
| Introduz dívida técnica? | Não | Sem alteração de código. Dívida é `convert_to_gguf.py` quebrado (pré-existente). |
| Um colega entende sem perguntar? | Sim | Resultado (0.00/20) e causa-raiz documentados. |
| Qual insight vai para o registo de aprendizagem? | - | Avaliar fine-tune contra modelo não-fine-tunado produz resultados inválidos; gap é de infra, não de treino (T302 convergiu com loss < 2.0). |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (avaliação only-read).

## Decisão de revisão
❌ NÃO PASSA NO AC — resultado honesto e documentado. T402 não atinge acurácia > 0.5 porque o `amalia` avaliado não incorpora os fine-tunes T301/T302.

## Acompanhamento
- Gap crítico: `convert_to_gguf.py` quebrado. Sem corrigir, M4/M5 não validam o modelo treinado. Ação: corrigir convert_to_gguf.py, registar modelo fine-tunado como `amalia`, re-executar T401-T403.
