---
ticket: T001
title: Ambiente de treino (Ollama + Python + deps)
phase: plan
tier: AES-standard
---

# T001 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `make setup` → exit code 0, todas as dependências já satisfeitas no `.venv`
- Python 3.12.3 (sistema e `.venv`)
- Ollama rodando: `amalia:latest` (16 GB) e `qwen3:8b` (5.2 GB)
- `requirements.txt`: torch, transformers, peft, bitsandbytes, datasets, accelerate, ruff, pytest (todas com `>=`, não fixas)
- `.gitignore` ignora `.venv` (não está versionado)
- `make lint` usa `$(PYTHON) -m ruff check $(SRC_DIR) $(EVAL_DIR) $(SCRIPTS_DIR)` com fallback `pip install ruff`

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- CLAUDE.md (comando `make setup`, critérios de aceitação)
- PLAN.md (T001 AC: `make setup` roda sem erros; dependências externas: GPU NVIDIA, Ollama, Python 3.12+)
- Makefile (target `setup`, `lint`)

### ASSUMPTIONS I'M MAKING
- [KNOWN] `.venv` existe e tem todas as dependências instaladas — justificação: `make setup` exit 0, `Requirement already satisfied` para todos os pacotes
- [KNOWN] Ollama está rodando e responde a `ollama list` — justificação: output mostra `amalia:latest` e `qwen3:8b`
- [KNOWN] Python 3.12.3 disponível — justificação: `python3 --version` e `.venv/bin/python --version`
- [INFERRED] `requirements.txt` não fixa versões → builds não reprodutíveis — evidence chain: todas as linhas usam `>=` → `pip install` pode resolver versões diferentes em máquinas diferentes → comportamento de fine-tune pode variar
- [ASSUMED] CUDA/GPU disponível para `bitsandbytes` e `torch` — potential impact if false: T301+ (fine-tune QLoRA) falha ou é lentíssimo em CPU
- [UNKNOWN] Se há acesso à rede para `pip install` numa máquina limpa — impact: `make setup` pode falhar offline

### WHAT WASN'T SPECIFIED (that matters)
- Versões exatas das dependências (reprodutibilidade do ambiente)
- Verificação de versão mínima do Python (3.12+) dentro do target `setup`
- O que fazer se Ollama não estiver rodando (target já falha com mensagem clara — aceitável)

### ALTERNATIVES I DIDN'T CHOOSE
- Usar `pip freeze > requirements.lock` separado: rejeitado — adiciona ficheiro extra fora do escopo do ticket; pinning direto em `requirements.txt` é mais simples e suficiente
- Usar `uv`/`poetry`: rejeitado — adiciona nova dependência de ferramenta, fora do escopo (projeto usa `venv` + `pip`)

### INVITE CONTRADICTION
- Posso estar errado que o ambiente está "pronto" só porque `make setup` passa agora: o risco real é a reprodutibilidade futura. Se o usuário discordar do pinning de versões, reverto.
- O que estaria a faltar na análise? (ex: variáveis de ambiente CUDA, versão do driver NVIDIA)

### RISKS & SIDE EFFECTS
- Versões não fixas → `make setup` numa máquina nova resolve versões diferentes → resultados de treino não reproduzíveis
- `bitsandbytes` depende do CUDA driver; sem GPU adequada, T301+ bloqueia (risco conhecido, fora do escopo de T001 mas documentado)
- Alterar `requirements.txt` pode forçar reinstalação de pacotes no `.venv` existente (baixo risco, `pip` gere dependências)

### COST OF BEING WRONG
- MEDIUM: problemas de ambiente bloqueiam todos os tickets downstream (T101-T502). O pinning reduz esse risco com custo baixíssimo.

### REASONING SKELETON
Claim: pinning versões em `requirements.txt` melhora a reprodutibilidade do ambiente de treino.
→ Premissa 1: `make setup` instala de `requirements.txt` (verificado no Makefile)
→ Premissa 2: versões `>=` permitem resolução diferente em máquinas diferentes (facto do pip)
→ Premissa 3: fine-tune QLoRA é sensível a versões de torch/transformers/peft (facto de engenharia de ML)
→ Inference: fixar versões remove uma fonte de variação não controlada
→ Conclusion: pinning é justificado para rigor do ambiente de treino

### SCOPE BOUNDARIES
In scope: verificar `make setup`, pinning de versões em `requirements.txt` para reprodutibilidade.
Out of scope: gerar datasets (T101-T103), executar treino (T301-T303), configurar CUDA/driver, publicar modelo (push).

## Phase 2 — Solution Proposal

### What I will change
- `requirements.txt`: fixar versões exatas (`==`) aos valores atualmente instalados e a funcionar (torch 2.15.0, transformers 5.22.2, peft 0.21.2, bitsandbytes 0.50.2, datasets 5.1.0, accelerate 1.15.0, ruff 0.17.4, pytest 9.2.0), mantendo os comentários de cabeçalho.

### What I will NOT change (and why)
- Não vou alterar o Makefile `setup` — o target já funciona e falha com mensagem clara se Ollama não estiver rodando; adicionar verificações de Python/CUDA seria escopo adicional não pedido no AC.
- Não vou criar ficheiro de lock separado — mantém a coisa simples (um único ficheiro de dependências).
- Não vou tocar em scripts/, src/, eval/, configs/ — fora do escopo de T001.

### Verification criteria (how I'll know it worked)
- `make setup` exit code 0 (regressão: ainda passa com versões fixas)
- `make lint` passa (ruff não reclama de requirements.txt — não é Python, mas confirma que nada quebrou)
- Versões em `requirements.txt` batem com as instaladas no `.venv` (reprodutibilidade)
- T001 AC: `make setup` roda sem erros

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
