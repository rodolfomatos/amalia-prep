---
ticket: T203
title: Dataset valido (JSONL, sem duplicatas) — saliencia
phase: plan
tier: AES-standard
---

# T203 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/salience_training.jsonl`: 50 linhas, produzido por T201/T202
- Schema (pós-T201): `id, conteudo, ilhas, relacoes(top-level achatado), novidade_esperada, total_relacoes, tipos_relacao, ilhas_conectadas, ilhas[i].{id,nome,descricao,relacoes[]}`
- IDs: `salience_0000`..`salience_0049` (sequenciais, únicos)
- 5 tipos de relação presentes (verificado no T202)
- T201 verify: top-level ilhas/relacoes/conteudo/novidade_esperada em todas as linhas; `relacoes` achatado bate com `total_relacoes`
- T202 verify: 5 tipos de relação (>=3 satisfeito)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T203 AC: "50 linhas, todas unicas, schema valido")
- `data/salience_training.jsonl` (artefato a validar)
- T201-plan/verify, T202-plan/verify (validações precedentes)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Dataset tem 50 linhas — justificação: `wc -l = 50` (T201/T202)
- [KNOWN] IDs únicos — justificação: 50 IDs sequenciais (T201)
- [KNOWN] Schema válido em todas as linhas — justificação: verificação campo a campo (T201)
- [KNOWN] JSONL válido — justificação: todas as linhas fazem `json.loads` (T201)
- [INFERRED] T203 é uma validação de confirmação, não requer alteração de código — evidence chain: T201/T202 já satisfizeram todos os sub-critérios de T203 no mesmo artefato
- [ASSUMED] Não é necessário criar um script de validação reutilizável para T203 — potential impact if false: validação não seria reproduzível em futuras regenerações do dataset
- [UNKNOWN] Se o dataset será regenerado futuramente (ex: `make data`) e precisaria de validação automática — impact: sem validação automática, uma regeneração poderia produzir dataset inválido sem ser detectado

### WHAT WASN'T SPECIFIED (that matters)
- Se T203 deve criar um mecanismo de validação automática reutilizável ou apenas confirmar o estado atual
- Se a validação deve ser integrada a `make check` ou `make data`

### ALTERNATIVES I DIDN'T CHOOSE
- Criar `scripts/validate_dataset.py` e ligar a `make check`: rejeitado como escopo de T203 — seria uma melhoria de infra (fora do AC do ticket). Pode ser proposta como backlog/tech debt.
- Alterar o dataset: rejeitado — já é válido; alterar seria desnecessário e regressivo

### INVITE CONTRADICTION
- Posso estar errado que T203 não deve criar um script de validação: se a intenção é que todo `make data` produza um dataset validado, então um script de validação seria valioso. Mas isso é uma decisão de arquitetura de infra, fora do escopo de T203 (validação do artefato atual). Registrado como sugestão de backlog.

### RISKS & SIDE EFFECTS
- Ticket só-leitura: nenhum risco de alteração de ficheiros.
- Risco residual: se o dataset for regenerado sem validação, poderia ficar inválido (mitigação: documento como sugestão de backlog).

### COST OF BEING WRONG
- BAIXO: T203 é confirmação; se algo estivesse inválido, T201/T202 já teriam detetado.

### REASONING SKELETON
Claim: T203 pode ser concluído com validação formal do artefato existente, sem alteração de código.
→ Premissa 1: T203 AC exige 50 linhas únicas, schema válido, JSONL válido
→ Premissa 2: T201/T202 já verificaram todos esses sub-critérios no mesmo artefato
→ Inference: executar validação formal única e documentar = satisfaz T203
→ Conclusion: validação de confirmação, sem novo código

### SCOPE BOUNDARIES
In scope: validação formal do `data/salience_training.jsonl` contra o AC T203; documentar resultado.
Out of scope: criar script de validação reutilizável, integrar a `make check`, alterar dataset, fine-tune.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Apenas executar validação formal (Python one-off) contra `data/salience_training.jsonl` e documentar o resultado nos outputs de verify/review/learn.

### What I will NOT change (and why)
- Não vou alterar `data/salience_training.jsonl` (já válido)
- Não vou criar `scripts/validate_dataset.py` (escopo separado; registado como sugestão de backlog na hostile analysis)
- Não vou alterar `Makefile`/`make check` (escopo separado)

### Verification criteria
- Script de validação one-off confirma: 50 linhas, IDs únicos, schema válido em todas, JSONL válido
- Resultado documentado em T203-verify.md

### Diffstory (placeholder — preenchido em Phase 3)
Nenhuma alteração de ficheiros rastreados pelo git (apenas execução de validação).
