---
ticket: T303
title: Modelo amalia disponível no Ollama local
phase: review
tier: AES-standard
---

# T303 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Confirmação only-read de `ollama list`. |
| Está correto para todos os inputs identificados? | Sim | `amalia:latest` está no Ollama; AC literal satisfeito. |
| Introduz dívida técnica? | Não | Sem alteração de código. A limitação (convert_to_gguf.py quebrado) é pré-existente e documentada. |
| Um colega entende sem perguntar? | Sim | O output de `ollama list` e a documentação da origem/limitação são claros. |
| Qual insight vai para o registo de aprendizagem? | - | O AC literal pode estar satisfeito enquanto o modelo subjacente não reflete os fine-tunes recentes; distinguir "presente no Ollama" de "produto dos nossos treinos" é importante para a interpretação de M4. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (confirmação only-read). Artefato verificado: `amalia:latest` no Ollama (de run anterior, built from `models/amalia-merged/amalia.f16.gguf` via `configs/Modelfile`).

## Decisão de revisão
✅ APROVADO (com nota) — T303 cumpre o AC literal (`ollama list` mostra `amalia`). A limitação de que o `amalia` não é produto dos fine-tunes T301/T302 é documentada como gap para M4/M5.

## Acompanhamento (não bloqueia T303)
- Gap conhecido: `convert_to_gguf.py` quebrado (14 bytes) impede registar um modelo fine-tunado novo como `amalia`. Corrigir isso é escopo separado (fora de T303).
- M4 (T401-T403, avaliação contra `amalia`) avaliará o modelo existente, não um refinado pelos nossos fine-tunes — interpretar resultados com essa ressalva.
