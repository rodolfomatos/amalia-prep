---
ticket: T301
title: Fine-tune qwen3:8b em abdução
phase: review
tier: AES-standard
---

# T301 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Sim o suficiente | Alteração mínima em fine_tune.py (salience opcional) + 1 execução de treino. Sem abstrações especulativas. |
| Está correto para todos os inputs identificados? | Sim | Loss convergiu (6.519 → 0.149), < 2.0; modelo salvo com adapter + tokenizer. |
| Introduz dívida técnica? | Não | A alteração em fine_tune.py é limpa e retrocompatível. `models/` não versionado é decisão de infra existente (.gitignore). |
| Um colega entende sem perguntar? | Sim | O treino usa o script existente com ID HF correto (`Qwen/Qwen3-8B`); loss e salvamento são reportados pelo Trainer. |
| Qual insight vai para o registo de aprendizagem? | - | QLoRA 4-bit de Qwen3-8B cabe na RTX 5090 com batch-size 1 + expandable_segments; batch-size 4 causa OOM. |

## Difstory (resumo da alteração)

Ficheiros alterados: 1 (código) + execução de treino (artefato local, não versionado)
1. `scripts/fine_tune.py`:
   - `--salience-data` agora opcional (`required=False`, default `None`)
   - `prepare_dataset(abduction_path, salience_path=None)`: usa apenas abduction se `salience_path` for None
2. Execução de treino abduction-only → `models/amalia-abduction/` (não versionado)

O que foi intencionalmente não tocado:
- Makefile `BASE=qwen3:8b` (uso o ID HF `Qwen/Qwen3-8B` diretamente na execução; corrigir o Makefile é escopo separado)
- `convert_to_gguf.py` (quebrado, afeta T303)
- T302 (salience fine-tune — ticket separado)
- T303 (registro no Ollama — requer GGUF, bloqueado por convert_to_gguf.py quebrado)

Riscos restantes: `models/` não versionado; OOM com batch-size 4 (usar 1); amalia:latest existente no Ollama não é produto deste treino.

## Decisão de revisão
✅ APROVADO — T301 cumpre o AC completo (modelo salvo, loss < 2.0, sem divergência).

## Acompanhamento (não bloqueia T301)
- T302 (fine-tune salience, loss < 2.0) é o próximo, usando o mesmo suporte single-dataset.
- T303 (Ollama) está bloqueado pela quebra do convert_to_gguf.py; `amalia:latest` já existe no Ollama de um run anterior mas não é produto deste treino.
