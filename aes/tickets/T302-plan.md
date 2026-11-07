---
ticket: T302
title: Fine-tune qwen3:8b em saliência
phase: plan
tier: AES-standard
---

# T302 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/salience_training.jsonl`: 50 exemplos, versão no git, schema com `relacoes` top-level (T203)
- `scripts/fine_tune.py`: `--salience-data` agora opcional (implementado em T301); `prepare_dataset` usa apenas salience quando `train-data`... (veja abaixo)
- Qwen/Qwen3-8B em cache HF local; RTX 5090 (33.7 GB VRAM), CUDA disponível
- T301 concluído (fine-tune abduction concluído, loss < 2.0, suporte single-dataset funcionando)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M3: T302 salience fine-tune, loss < 2.0)
- T301-plan/verify/review/learn (fine-tune abduction concluído, lições de OOM e base model)
- scripts/fine_tune.py (salience opcional após T301)
- data/salience_training.jsonl (50 exemplos, versão no git)

### ASSUMPTIONS I'M MAKING
- [KNOWN] `--salience-data` opcional funciona (validado em T301 com `--train-data` apenas) — justificação: T301 executou com sucesso
- [INFERRED] Para treinar salience-only, passo `--salience-data data/salience_training.jsonl` SEM `--train-data`? — need to verify prepare_dataset handles salience-only. Evidence: prepare_dataset(abduction_path, salience_path) — se abduction_path é obrigatório, não dá para passar apenas salience. GAP: prepare_dataset requer abduction_path obrigatório.
- [KNOWN] Batch-size 4 causa CUDA OOM (lição de T301) → usar batch-size 1 + expandable_segments
- [KNOWN] Qwen/Qwen3-8B em cache HF local

### WHAT WASN'T SPECIFIED (that matters)
- prepare_dataset(abduction_path, salience_path=None) exige abduction_path obrigatório → não dá para treinar salience-only sem passar um abduction_path (mesmo que dummy). GAP no suporte single-dataset implementado em T301.

### ALTERNATIVES I DIDN'T CHOOSE
- Passar um arquivo dummy para --train-data e o real para --salience-data: rejeitado — treina com dados dummy de abduction (incoerente).
- Tornar --train-data também opcional: necessário para salience-only puro. Vou fazer isso em T302 (alteração adicional em fine_tune.py).

### INVITE CONTRADICTION
- Posso estar errado que preciso modificar fine_tune.py novamente: talvez seja aceitável usar o combined (make train). Mas PLAN.md separa T301/T302 e cada uma tem AC próprio. Prefiro respeitar a separação com suporte adequado a single-dataset em ambos os lados.

### RISKS & SIDE EFFECTS
- CUDA OOM (mitigado com batch-size 1 + expandable_segments)
- Modelo salvo apenas localmente (models/ ignorado)

### COST OF BEING WRONG
- MEDIUM: se o fine-tune falhar ou divergir, T302 não passa e T402 fica bloqueado.

### REASONING SKELETON
Claim: estender fine_tune.py para permitir salience-only (--train-data opcional quando --salience-data fornecido) e treinar salience, verifica loss < 2.0, satisfaz T302.
→ Premissa 1: T302 AC exige fine-tune salience que salva modelo e loss < 2.0
→ Premissa 2: fine_tune.py já faz QLoRA + Trainer; precisa apenas permitir --train-data opcional
→ Premissa 3: Qwen/Qwen3-8B em cache local, cabe na RTX 5090 com batch-size 1
→ Inference: executar fine_tune.py com apenas --salience-data produz adapter + loss verificável
→ Conclusion: tornar --train-data opcional, executar treino salience-only, verificar loss < 2.0

### SCOPE BOUNDARIES
In scope: modificar fine_tune.py (--train-data opcional quando --salience-data fornecido), executar fine-tune salience-only, verificar loss < 2.0, salvar modelo.
Out of scope: T303 (Ollama, convert_to_gguf.py quebrado), T402 (avaliação), correção do Makefile BASE.

## Phase 2 — Solution Proposal

### What I will change
1. `scripts/fine_tune.py`:
   - Tornar `--train-data` opcional (`required=False`, default `None`) quando `--salience-data` fornecido
   - `prepare_dataset(abduction_path=None, salience_path=None)`: aceita qualquer um dos dois (ou ambos)
   - Validar que pelo menos um dos dois é fornecido
2. Executar: `fine_tune.py --base-model Qwen/Qwen3-8B --output-model amalia-salience --salience-data data/salience_training.jsonl --epochs 3 --batch-size 1 --learning-rate 2e-4`

### What I will NOT change (and why)
- Não corrigir Makefile BASE (escopo separado)
- Não corrigir convert_to_gguf.py (afeta T303)
- Não registrar no Ollama (T303)

### Verification criteria
- fine_tune.py executa sem erro (exit 0)
- Modelo salvo em `models/amalia-salience/`
- Loss final < 2.0

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
