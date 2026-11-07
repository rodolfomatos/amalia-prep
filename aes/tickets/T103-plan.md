---
ticket: T103
title: Dataset valido (JSONL, sem duplicatas) — abducao
phase: plan
tier: AES-standard
---

# T103 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/abduction_training.jsonl`: 100 linhas, produzido por T101/T102
- Distribuição: 20 por cada uma das 5 categorias (amor_proibido, ausência, evento_trágico, objeto_infancia, pessoa_proibida)
- Schema (pós-T101): `id, category, observation, latent_variable(top-level), context, ground_truth{latent_variable, mechanism}`
- IDs: `abduction_0000`..`abduction_0099` (sequenciais, únicos)
- T101 verify: top-level observation/latent_variable/context em todas as linhas
- T102 verify: 20/categoria, IDs únicos, JSONL válido, ground_truth.latent_variable preservado

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T103 AC: "100 linhas, todas unicas, schema valido")
- `data/abduction_training.jsonl` (artefato a validar)
- T101-plan/verify, T102-plan/verify (validações precedentes)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Dataset tem 100 linhas — justificação: `wc -l = 100` (T101/T102)
- [KNOWN] IDs únicos — justificação: 100 IDs sequenciais (T102)
- [KNOWN] Schema válido em todas as linhas — justificação: verificação campo a campo (T101/T102)
- [KNOWN] JSONL válido — justificação: todas as linhas fazem `json.loads` (T102)
- [INFERRED] T103 é uma validação de confirmação, não requer alteração de código — evidence chain: T101/T102 já satisfizeram todos os sub-critérios de T103
- [ASSUMED] Não é necessário criar um script de validação reutilizável para T103 — potential impact if false: validação não seria reproduzível em futuras regenerações do dataset
- [UNKNOWN] Se o dataset será regenerado futuramente (ex: `make data`) e precisaria de validação automática — impact: sem validação automática, uma regeneração poderia produzir dataset inválido sem ser detectado

### WHAT WASN'T SPECIFIED (that matters)
- Se T103 deve criar um mecanismo de validação automática reutilizável ou apenas confirmar o estado atual
- Se a validação deve ser integrada a `make check` ou `make data`

### ALTERNATIVES I DIDN'T CHOOSE
- Criar `scripts/validate_dataset.py` e ligar a `make check`: rejeitado como escopo de T103 — seria uma melhoria de infra (fora do AC do ticket, que é validar o dataset existente). Pode ser proposta como backlog/tech debt.
- Alterar o dataset: rejeitado — já é válido; alterar seria desnecessário e regressivo

### INVITE CONTRADICTION
- Posso estar errado que T103 não deve criar um script de validação: se a intenção é que todo `make data` produza um dataset validado, então um script de validação seria valioso. Mas isso é uma decisão de arquitetura de infra, fora do escopo de T103 (validação do artefato atual). Registrado como sugestão de backlog.

### RISKS & SIDE EFFECTS
- Ticket só-leitura: nenhum risco de alteração de ficheiros.
- Risco residual: se o dataset for regenerado sem validação, poderia ficar inválido (mitigação: documento como sugestão de backlog).

### COST OF BEING WRONG
- BAIXO: T103 é confirmação; se algo estivesse inválido, T101/T102 já teriam detetado. O custo de não ter validação automática é médio mas é escopo separado.

### REASONING SKELETON
Claim: T103 pode ser concluído com validação formal do artefato existente, sem alteração de código.
→ Premissa 1: T103 AC exige 100 linhas únicas, schema válido, JSONL válido
→ Premissa 2: T101/T102 já verificaram todos esses sub-critérios no mesmo artefato
→ Inference: executar validação formal única e documentar = satisfaz T103
→ Conclusion: validação de confirmação, sem novo código

### SCOPE BOUNDARIES
In scope: validação formal do `data/abduction_training.jsonl` contra o AC T103; documentar resultado.
Out of scope: criar script de validação reutilizável, integrar a `make check`, alterar dataset, fine-tune.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Apenas executar validação formal (Python one-off) contra `data/abduction_training.jsonl` e documentar o resultado nos outputs de verify/review/learn.

### What I will NOT change (and why)
- Não vou alterar `data/abduction_training.jsonl` (já válido)
- Não vou criar `scripts/validate_dataset.py` (escopo separado; registado como sugestão de backlog na hostile analysis)
- Não vou alterar `Makefile`/`make check` (escopo separado)

### Verification criteria
- Script de validação one-off confirma: 100 linhas, IDs únicos, schema válido em todas, JSONL válido
- Resultado documentado em T103-verify.md

### Diffstory (placeholder — preenchido em Phase 3)
Nenhuma alteração de ficheiros rastreados pelo git (apenas execução de validação).
