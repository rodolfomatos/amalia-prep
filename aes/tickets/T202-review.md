---
ticket: T202
title: Ilhas com múltiplos tipos de relação (≥3 tipos)
phase: review
tier: AES-standard
---

# T202 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Ticket de confirmação sem alteração de código; verificação direta de contagem de tipos. |
| Está correto para todos os inputs identificados? | Sim | Verificado empíricamente: 5 tipos distintos, todos > 0, incluindo os 3 exigidos. |
| Introduz dívida técnica? | Não | Sem alteração de código. |
| Um colega entende sem perguntar? | Sim | O resultado é direto: 5 tipos presentes, AC satisfeito. |
| Qual insight vai para o registo de aprendizagem? | - | O gerador já definia 5 tipos desde o início; T202 confirma que o dataset herda essa diversidade. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (confirmação only-read). Artefato verificado: `data/salience_training.jsonl` (5 tipos de relação) e `scripts/generate_salience_data.py` (`RELATION_TYPES` com 5 tipos).

## Decisão de revisão
✅ APROVADO — T202 cumpre o AC completo (≥3 tipos de relação incluindo RELATED_TO, CONTRADIZ, COMPLEMENTA).

## Acompanhamento (não bloqueia T202)
- Próximo: T203 (validação formal: JSONL válido, 50 linhas únicas, schema válido), concluindo M2.
