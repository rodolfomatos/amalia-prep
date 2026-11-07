---
ticket: T401
title: Teste de abdução (acurácia > 0.3)
phase: review
tier: AES-standard
---

# T401 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Avaliação direta contra `amalia`; resultado medido e reportado. |
| Está correto para todos os inputs identificados? | Sim | Acurácia 0.00 (0/20) é a medição real; alvo > 0.3 não atingido. |
| Introduz dívida técnica? | Não | Sem alteração de código. A dívida é o `convert_to_gguf.py` quebrado (pré-existente, documentado). |
| Um colega entende sem perguntar? | Sim | O resultado (0.00/20) e a causa-raiz (modelo não é dos fine-tunes) estão documentados. |
| Qual insight vai para o registo de aprendizagem? | - | Avaliar contra um modelo que não é o fine-tunado produz resultados inválidos para medir o progresso do fine-tune. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (avaliação only-read). Artefato avaliado: `amalia:latest` no Ollama.

## Decisão de revisão
❌ NÃO PASSA NO AC — mas o resultado é honesto e documentado. T401 não atinge acurácia > 0.3 porque o `amalia` avaliado não incorpora os fine-tunes T301/T302 (convert_to_gguf.py quebrado). Isso não é mascarado.

## Acompanhamento (bloqueia progresso de M4/M5)
- Gap crítico: `convert_to_gguf.py` quebrado impede registar modelos fine-tunados como `amalia`. Sem isso, M4 (avaliação) e M5 (integração ACA) não podem validar o modelo treinado.
- Ação recomendada: corrigir `convert_to_gguf.py` (conversão adapter → GGUF), registar o modelo fine-tunado como `amalia`, re-executar T401-T403.
