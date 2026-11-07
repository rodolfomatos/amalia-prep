---
ticket: T203
title: Dataset valido (JSONL, sem duplicatas) — saliencia
phase: review
tier: AES-standard
---

# T203 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim | Ticket de confirmação sem alteração de código; validação one-off direta. |
| Está correto para todos os inputs identificados? | Sim | Validação cobriu todos os sub-critérios do AC (contagem, unicidade, schema, JSONL). |
| Introduz dívida técnica? | Não | Sem alteração de código. Registrada sugestão de backlog (script de validação reutilizável) mas não implementada — decisão consciente de escopo. |
| Um colega entende sem perguntar? | Sim | Os outputs de T201/T202/T203 documentam claramente o estado do dataset e as validações feitas. |
| Qual insight vai para o registo de aprendizagem? | - | Validar o dataset como ticket separado (T203) após gerá-lo (T201/T202) separa preocupações: geração vs validação. |

## Difstory
Nenhuma alteração de ficheiros rastreados pelo git (validação only-read). Artefato validado: `data/salience_training.jsonl` (já commitado em T201/T202).

## Decisão de revisão
✅ APROVADO — T203 cumpre o AC completo (50 linhas, únicas, schema válido, JSONL válido). O dataset de saliência de M2 está completo e validado.

## Acompanhamento (não bloqueia T203)
- Sugestão de backlog: criar `scripts/validate_dataset.py` e ligar a `make check`/`make data` para validação automática em regenerações futuras. Fora do escopo de T203.
- Marco M2 concluído: T201, T202, T203 todos done.
- Próximo marco: M3 (T301-T303, fine-tune QLoRA do qwen3:8b), que requer GPU NVIDIA e tempo de treino.
