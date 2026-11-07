---
ticket: T301
title: Fine-tune qwen3:8b em abdução
phase: plan
tier: AES-standard
---

# T301 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/abduction_training.jsonl`: 100 exemplos, versão no git, 20/categoria, schema com `latent_variable` top-level (T103)
- `scripts/fine_tune.py`: QLoRA fine-tune; aceita `--train-data` e `--salience-data` (ambos obrigatórios); combina datasets; treina com Trainer (transformers); salva adapter + tokenizer em `./models/{output-model}`
- HF: `Qwen/Qwen3-8B` em cache local (`~/.cache/huggingface/hub/models--Qwen--Qwen3-8B`) e acessível online
- GPU: RTX 5090, 33.7 GB VRAM, CUDA disponível (torch.cuda.is_available() = True)
- Ollama: `amalia:latest` já presente (de run anterior) — não é produto deste fine-tune
- Makefile `train`: treino COMBINADO (abdução + saliência) com `BASE=qwen3:8b` + `ollama create amalia`
- `convert_to_gguf.py`: 14 bytes, quebrado (não converte para GGUF)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M3: T301 abduction fine-tune, loss < 2.0; T302 salience; T303 Ollama)
- Makefile (target `train`, `BASE ?= qwen3:8b`, `OLLAMA create amalia -f configs/Modelfile`)
- scripts/fine_tune.py (QLoRA, Trainer, salva adapter)
- configs/Modelfile (FROM models/amalia-merged/amalia.f16.gguf — requer GGUF)
- scripts/convert_to_gguf.py (14 bytes, quebrado)
- data/abduction_training.jsonl (versão no git, 100 exemplos)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Qwen/Qwen3-8B está em cache HF local — justificação: `~/.cache/huggingface/hub/models--Qwen--Qwen3-8B` existe; `list_repo_files` acessível
- [KNOWN] CUDA/RTX 5090 disponível — justificação: `nvidia-smi` e `torch.cuda.is_available()`
- [KNOWN] Makefile `BASE=qwen3:8b` está incorreto para `from_pretrained` — evidence: `from_pretrained` espera ID HF (`Qwen/Qwen3-8B`), não tag Ollama (`qwen3:8b`). Usarei o ID HF correto diretamente no fine_tune.py.
- [KNOWN] `fine_tune.py` exige ambos `--train-data` e `--salience-data` — justificação: `argparse` com `required=True` em ambos
- [INFERRED] Para honrar T301 (abduction-only) e T302 (salience-only) do PLAN.md, é necessário tornar `--salience-data` opcional no fine_tune.py — evidence chain: PLAN.md separa T301/T302; script exige ambos → script não suporta a separação declarada
- [ASSUMED] QLoRA 4-bit de Qwen3-8B cabe na RTX 5090 (33.7 GB) — potential impact if false: OOM, treino falha
- [UNKNOWN] Tempo de treino (100 exemplos, 3 épocas, batch 4, QLoRA) — impact: poderia demorar minutos a dezenas de minutos

### WHAT WASN'T SPECIFIED (that matters)
- ID base do modelo: `qwen3:8b` (Makefile/Ollama) vs `Qwen/Qwen3-8B` (HF)
- Se T301 deve salvar como adapter LoRA ou modelo completo — fine_tune.py salva adapter (`model.save_pretrained`)
- Como registrar o fine-tune no Ollama (convert_to_gguf.py quebrado)

### ALTERNATIVES I DIDN'T CHOOSE
- Usar `make train` (combinado, BASE errada): rejeitado — treina abdução+saliência junto (não separa T301/T302), usa BASE incorreta, e tenta `ollama create` com GGUF inexistente
- Treinar abduction passando o mesmo arquivo para `--train-data` e `--salience-data`: rejeitado — produziria dados de treino misturados/incoerentes (format_abduction vs format_salience)
- Não modificar fine_tune.py (treinar combinado e partir a perda): rejeitado — não daria perda específica de abduction para T301

### INVITE CONTRADICTION
- Posso estar errado que modificar fine_tune.py é necessário: talvez seja aceitável treinar combinado e considerar T301/T302 como "cobertos". Mas o PLAN.md as separa e cada uma tem AC próprio (loss < 2.0). Prefiro respeitar a separação.
- Posso estar errado que a RTX 5090 aguenta QLoRA 4-bit do Qwen3-8B: se houver OOM, reduzo batch size ou uso CPU (lento). Verificarei no treino.

### RISKS & SIDE EFFECTS
- Treino GPU consome tempo e energia; pode falhar por OOM ou erro de dependência
- `models/` não é versionado (.gitignore) → o artefato do fine-tune fica apenas local
- `convert_to_gguf.py` quebrado → não consigo registar o fine-tune como `amalia` no Ollama via `make train` (afeta T303, não T301)

### COST OF BEING WRONG
- MEDIUM: se o fine-tune falhar ou divergir (loss >= 2.0), T301 não passa e T302/T303/T401 ficam bloqueados. Mitigação: verificar loss no final e reduzir learning rate/batch se necessário.

### REASONING SKELETON
Claim: modificar fine_tune.py para aceitar single-dataset e treinar apenas abduction produz um modelo salvo com loss < 2.0, satisfazendo T301.
→ Premissa 1: T301 AC exige fine-tune que salva modelo e loss < 2.0
→ Premissa 2: fine_tune.py faz QLoRA + Trainer e reporta loss; salvar com model.save_pretrained
→ Premissa 3: Qwen/Qwen3-8B está em cache local e cabe na RTX 5090
→ Premissa 4: Tornar --salience-data opcional permite treino abduction-only
→ Inference: executar fine_tune.py com apenas --train-data (abduction) produz adapter + loss verificável
→ Conclusion: implementar suporte single-dataset + executar treino de abduction + verificar loss < 2.0

### SCOPE BOUNDARIES
In scope: modificar fine_tune.py (salience opcional), executar fine-tune abduction-only, verificar loss < 2.0, salvar modelo.
Out of scope: T302 (salience fine-tune — ticket separado), T303 (Ollama — requer GGUF, convert_to_gguf.py quebrado), avaliação T401, correção do convert_to_gguf.py, correção do BASE no Makefile (uso ID HF correto diretamente, não altero o Makefile agora).

## Phase 2 — Solution Proposal

### What I will change
1. `scripts/fine_tune.py`:
   - Tornar `--salience-data` opcional (`required=False`, default `None`)
   - `prepare_dataset(abduction_path, salience_path=None)`: se `salience_path` é None, usa apenas abduction
   - `main()`: passar `args.salience_data` (pode ser None)
2. Executar: `fine_tune.py --base-model Qwen/Qwen3-8B --output-model amalia-abduction --train-data data/abduction_training.jsonl --epochs 3 --batch-size 4 --learning-rate 2e-4`

### What I will NOT change (and why)
- Não vou corrigir `BASE=qwen3:8b` no Makefile agora (uso o ID HF correto diretamente na execução de T301; corrigir o Makefile é escopo separado)
- Não vou corrigir `convert_to_gguf.py` (afeta T303, não T301)
- Não vou fazer `make train` (combinado, BASE errada)
- Não vou registrar no Ollama (T303, separado)

### Verification criteria
- fine_tune.py executa sem erro (exit 0)
- Modelo salvo em `models/amalia-abduction/` (adapter + tokenizer)
- Loss final (último logging do Trainer) < 2.0

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
