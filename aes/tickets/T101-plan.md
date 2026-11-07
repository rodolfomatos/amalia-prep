---
ticket: T101
title: 100 exemplos de observação → mecanismo latente
phase: plan
tier: AES-standard
---

# T101 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/abduction_training.jsonl`: 100 linhas, seeds 0-99, gerado por `scripts/generate_abduction_data.py`
- Schema atual por exemplo: `id, category, observation, context, ground_truth{latent_variable, mechanism}`
- `scripts/generate_abduction_data.py`: `generate_example(seed)` devolve dict com `ground_truth` nested; `main()` escreve JSONL com `--count` (default 100)
- `eval/test_abduction.py:61`: lê `example.get("ground_truth", {}).get("latent_variable", "")` — contrato executável usa nested
- `PLAN.md` T101 AC: cada exemplo tem top-level `observation`, `latent_variable`, `context`
- T001 concluído (ambiente pronto)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T101, T102, T103 AC; milestone M1)
- `scripts/generate_abduction_data.py` (gerador, schema)
- `eval/test_abduction.py` (contrato de leitura do dataset)
- `data/abduction_training.jsonl` (100 exemplos reais)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Dataset tem 100 linhas únicas (seeds 0-99) — justificação: `wc -l = 100`, ids `abduction_0000`..`abduction_0099`
- [KNOWN] Cada exemplo tem `observation` e `context` no top-level — justificação: inspeção do JSONL
- [KNOWN] Cada exemplo tem `ground_truth.latent_variable` (nested), NÃO top-level `latent_variable` — justificação: inspeção (top-level keys = id, category, observation, context, ground_truth)
- [KNOWN] Testes leem `ground_truth.latent_variable` — justificação: `eval/test_abduction.py:61`
- [INFERRED] PLAN.md T101 AC ("top-level `latent_variable`") está impreciso em relação ao contrato executável — evidence chain: PLAN diz top-level, código/teste usam nested → um dos dois está errado
- [ASSUMED] Adicionar top-level `latent_variable` espelhando `ground_truth.latent_variable` satisfaz o AC literal sem quebrar testes — potential impact if false: testes ainda passam (não usam o campo novo), AC fica literal
- [UNKNOWN] Se T102/T103 esperam schema diferente — impact: alterar o schema agora pode afetar tickets subsequentes

### WHAT WASN'T SPECIFIED (that matters)
- Se `latent_variable` deve ser top-level OU nested — PLAN e código discordam
- Se o campo `mechanism` (explicação causal) deve ser top-level também (PLAN só menciona `latent_variable`)

### ALTERNATIVES I DIDN'T CHOOSE
- Alterar `eval/test_abduction.py` para ler top-level `latent_variable`: rejeitado — muda o contrato executável, fora do escopo de T101 (ticket é sobre o dataset, não os testes)
- Remover `ground_truth` e usar só top-level: rejeitado — quebraria os testes (eles lêem `ground_truth.latent_variable`)
- Deixar como está e declarar PLAN.md errado: rejeitado — não corrige o AC; T101 não passaria literal

### INVITE CONTRADICTION
- Posso estar errado que o AC literal deve ser satisfeito: talvez o PLAN.md esteja certo e os testes/dados estejam errados (deveriam ser top-level). Mas mudar os testes é fora do escopo de T101 e quebraria a avaliação (T401). Vou priorizar não quebrar o contrato executável.
- O campo `mechanism` também mereceria ser top-level? Não inclui agora — escopo mínimo para T101.

### RISKS & SIDE EFFECTS
- Campo duplicado (`latent_variable` top-level = `ground_truth.latent_variable`) — pequena redundância, justificada por satisfazer AC literal
- Regenerar o dataset com o gerador alterado: mesmo conteúdo (mesmas seeds) + novo campo; ids inalterados
- Qualquer alteração em `scripts/generate_abduction_data.py` pode afetar regenerações futuras (T103 validação)

### COST OF BEING WRONG
- MEDIUM: se a decisão de schema estiver errada, T102/T103/T301/T401 herdam o schema errado. Mitigação: manter `ground_truth.latent_variable` intocado (testes não quebram) e apenas adicionar o campo top-level.

### REASONING SKELETON
Claim: adicionar top-level `latent_variable` espelhando `ground_truth.latent_variable` torna T101 literal sem quebrar nada.
→ Premissa 1: PLAN.md T101 AC exige top-level `latent_variable`
→ Premissa 2: testes leem `ground_truth.latent_variable` (não top-level)
→ Premissa 3: adicionar um campo novo não remove o existente → testes continuam a passar
→ Inference: adicionar top-level `latent_variable` satisfaz PLAN e preserva testes
→ Conclusion: implementar campo top-level espelhado

### SCOPE BOUNDARIES
In scope: adicionar top-level `latent_variable` a cada exemplo do dataset; atualizar gerador para emitir o campo.
Out of scope: T102 (20/categoria), T103 (validação duplicatas), alterar testes, alterar PLAN.md, fine-tune.

## Phase 2 — Solution Proposal

### What I will change
1. `scripts/generate_abduction_data.py`: no `generate_example`, adicionar `"latent_variable": latent` no nível superior do dict retornado (espelhando `ground_truth.latent_variable`).
2. `data/abduction_training.jsonl`: regenerar com o gerador atualizado (mesmas seeds 0-99 → mesmo conteúdo + campo `latent_variable` top-level).

### What I will NOT change (and why)
- Não vou alterar `eval/test_abduction.py` (contrato executável, fora do escopo de T101)
- Não vou remover `ground_truth.latent_variable` (quebraria testes)
- Não vou alterar `PLAN.md` (documentação de plano, fora do escopo do ticket; a contradição fica registada na hostile analysis)

### Verification criteria
- Cada uma das 100 linhas tem chaves top-level `observation`, `latent_variable`, `context`
- 100 linhas, todas únicas (ids únicos)
- JSONL válido (cada linha parseável)
- `eval/test_abduction.py` ainda consegue ler `ground_truth.latent_variable` (não quebrado) — validar executando `test_model_available` + leitura de schema (não rodar LLM, que é lento e depende do modelo)

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
