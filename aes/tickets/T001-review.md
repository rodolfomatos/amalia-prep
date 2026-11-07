---
ticket: T001
title: Ambiente de treino (Ollama + Python + deps)
phase: review
tier: AES-standard
---

# T001 — Critical Review Output (Phase 5)

## Perguntas críticas de revisão

| Pergunta | Resposta | Justificação |
|----------|----------|--------------|
| Pode ser mais simples? | Não | Alteração é mínima: apenas `requirements.txt`, 8 linhas, com comentário a explicar o porquê. Sem abstrações especulativas. |
| Está correto para todos os inputs identificados? | Sim | Versões fixadas batem com as instaladas no `.venv`. Num `make setup` fresco, o pip instala exatamente estas versões → reprodutível. |
| Introduz dívida técnica? | Não | O pinning reduz dívida (reprodutibilidade). Os 21 erros de ruff pré-existentes são dívida antiga, não introduzida por esta alteração. |
| Um colega entende sem perguntar? | Sim | Comentário em `requirements.txt` explica que as versões são fixas para reprodutibilidade do ambiente de treino. |
| Qual insight vai para o registo de aprendizagem? | - | Ambientes de treino de ML exigem dependências fixas; `>=` não é suficiente para reprodutibilidade de fine-tune QLoRA. |

## Difstory (resumo da alteração)

Ficheiros alterados: `requirements.txt` (1 ficheiro, 10 inserções, 9 remoções).
- O que mudou: `torch>=2.0.0` → `torch==2.15.0` (idem para transformers, peft, bitsandbytes, datasets, accelerate, ruff, pytest).
- Porquê estes ficheiros: `requirements.txt` é a fonte de verdade do `make setup`; fixar versões aqui torna o ambiente de treino reprodutível (Phase 1, risco identificado).
- O que foi intencionalmente não tocado: Makefile (target `setup` já funciona), `src/` (vazio), `eval/` (testes pré-existentes, fora do escopo de T001), `scripts/` (fora do escopo), `configs/` (Modelfile, fora do escopo).
- Riscos restantes: 21 erros de ruff pré-existentes (não bloqueantes para T001); necessidade de GPU/CUDA para T301+ (fora do escopo de T001).

## Decisão de revisão
✅ APROVADO — T001 cumpre o Acceptance Criteria (`make setup` roda sem erros) e a alteração de pinning é justificada, segura e mínima.

## Acompanhamento (não bloqueia T001)
- Os 21 erros de ruff pré-existentes podem ser registados em `docs/ROADMAP.md` como backlog de tech debt, mas não pertencem a este ticket.
