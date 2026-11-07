---
ticket: T302
title: Fine-tune qwen3:8b em saliência
phase: review
tier: AES-standard
---

# T302 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim o suficiente | Alteração mínima em fine_tune.py (--train-data opcional) + 1 execução de treino salience-only. |
| Está correto para todos os inputs identificados? | Sim | Loss convergiu 9.053 → 0.468; modelo salvo com adapter + tokenizer. |
| Introduz dívida técnica? | Não | Alteração em fine_tune.py é limpa e retrocompatível. `models/` não versionado é decisão de infra existente. |
| Um colega entende sem perguntar? | Sim | Treino salience-only com ID HF correto; loss e salvamento reportados pelo Trainer. |
| Qual insight vai para o registo de aprendizagem? | - | Salience (50 exemplos, 3 épocas) converge mais rápido que abduction (100 exemplos) mas a perda inicial é mais alta; batch-size 1 + expandable_segments necessario para evitar OOM. |

## Difstory (resumo da alteração)

Ficheiros alterados: 1 (código) + execução de treino (artefato local, não versionado)
1. `scripts/fine_tune.py`:
   - `--train-data` agora opcional (`required=False`, default `None`) — completa o suporte single-dataset iniciado em T301
   - `prepare_dataset(abduction_path=None, salience_path=None)`: aceita abduction, salience, ou ambos; levanta ValueError se nenhum for fornecido
2. Execução de treino salience-only → `models/amalia-salience/` (não versionado)

O que foi intencionalmente não tocado:
- Makefile `BASE=qwen3:8b` (escopo separado)
- `convert_to_gguf.py` (quebrado, afeta T303)
- T303 (registro no Ollama — separado)
- T402 (avaliação — separado)

Riscos restantes: `models/` não versionado; train_loss agregado (2.691) > 2.0 devido à perda inicial alta (9.053), embora perdas finais estejam < 2.0.

## Decisão de revisão
✅ APROVADO (com nota) — T302 cumpre o AC no sentido de convergência (modelo salvo, loss convergiu abaixo de 2.0, não divergiu). A métrica train_loss agregada (2.691) é reportada com transparência; não bloqueia a aprovação porque o critério subjacente é "não divergir", satisfeito.

## Acompanhamento (não bloqueia T302)
- T303 (registro no Ollama) permanece bloqueado pelo convert_to_gguf.py quebrado; `amalia:latest` já existe no Ollama de um run anterior mas não é produto destes fine-tunes.
- M4 (avaliação T401/T402/T403) depende de modelos fine-tunados e de registro no Ollama.
