---
ticket: T202
title: Ilhas com múltiplos tipos de relação (≥3 tipos)
phase: plan
tier: AES-standard
---

# T202 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `scripts/generate_salience_data.py`: `RELATION_TYPES = [RELATED_TO, CONTRADIZ, COMPLEMENTA, DERIVA_DE, AGREGADO_EM]` (5 tipos)
- `data/salience_training.jsonl`: 50 linhas, todos os 5 tipos de relação presentes (contagem total: AGREGADO_EM 97, COMPLEMENTA 88, CONTRADIZ 106, DERIVA_DE 105, RELATED_TO 106)
- `eval/test_salience.py`: não testa tipos de relação diretamente (usa `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`)
- T201 concluído (dataset com `relacoes` de topo)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T202 AC: "Pelo menos 3 tipos diferentes (RELATED_TO, CONTRADIZ, COMPLEMENTA)")
- `scripts/generate_salience_data.py` (RELATION_TYPES)
- `data/salience_training.jsonl` (tipos presentes)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Gerador define 5 tipos de relação — justificação: código `RELATION_TYPES`
- [KNOWN] Dataset contém todos os 5 tipos — justificação: contagem verificada no T201 (5 tipos, todos > 0)
- [KNOWN] ≥3 tipos satisfeito (5 ≥ 3) — justificação: aritmética direta
- [INFERRED] T202 é confirmação de estado já satisfeito por T201, não requer alteração de código — evidence chain: gerador tem 5 tipos, dataset tem 5 tipos, AC exige ≥3
- [ASSUMED] Não é necessário alterar o gerador para "garantir" os 3 tipos — potential impact if false: o gerador escolhe `rng.choice(RELATION_TYPES)` aleatoriamente; com 50 exemplos e várias relações por exemplo, é virtualmente certo que todos apareçam (já confirmado empíricamente)
- [UNKNOWN] Se uma regeneração futura com pouca amostragem poderia perder um tipo — impact: baixo, dado que há 5 tipos e muitas relações por exemplo

### WHAT WASN'T SPECIFIED (that matters)
- Se T202 exige que cada tipo apareça em cada exemplo, ou apenas no dataset como um todo — PLAN.md diz "Pelo menos 3 tipos diferentes" (no dataset como um todo)

### ALTERNATIVES I DIDN'T CHOOSE
- Alterar o gerador para forçar pelo menos 3 tipos por exemplo: rejeitado — excessivo, o AC é no nível do dataset, não por exemplo
- Adicionar validação automática de tipos a `make check`: rejeitado — escopo separado (backlog/tech debt)

### INVITE CONTRADICTION
- Posso estar errado que não é necessário alterar o gerador: se a intenção é garantir os 3 tipos mesmo em regenerações pequenas, uma validação ou forçamento seria útil. Mas o AC é satisfeito pelo estado atual. Registrado como observação.

### RISKS & SIDE EFFECTS
- Ticket só-leitura: nenhum risco de alteração de ficheiros.
- Risco residual: regeneração futura com `--count` muito baixo poderia, por acaso, não incluir algum tipo (improvável com 5 tipos e múltiplas relações).

### COST OF BEING WRONG
- BAIXO: T202 já está satisfeito (5 tipos presentes). Se houvesse um problema, T201 já teria detetado.

### REASONING SKELETON
Claim: T202 (>=3 tipos de relação, incluindo RELATED_TO/CONTRADIZ/COMPLEMENTA) já está satisfeito sem alteração de código.
→ Premissa 1: T202 AC exige ≥3 tipos diferentes, incluindo os 3 nomeados
→ Premissa 2: Gerador define 5 tipos (RELATION_TYPES)
→ Premissa 3: Dataset contém todos os 5 tipos (verificado empíricamente no T201)
→ Inference: 5 ≥ 3 e os 3 nomeados estão presentes → AC satisfeito
→ Conclusion: confirmação formal, sem novo código

### SCOPE BOUNDARIES
In scope: confirmação formal de que o dataset/gerador têm ≥3 tipos incluindo os 3 exigidos; documentar resultado.
Out of scope: alterar gerador/dataset, T203 (validação de validade/unicidade), validação automática.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Executar confirmação formal (contagem de tipos no dataset) e documentar o resultado nos outputs de verify/review/learn.

### What I will NOT change (and why)
- Não vou alterar `scripts/generate_salience_data.py` (já tem 5 tipos)
- Não vou alterar `data/salience_training.jsonl` (já tem os 5 tipos)
- Não vou criar validação automática (escopo separado)

### Verification criteria
- Script de confirmação one-off conta tipos distintos no dataset: ≥3 e inclui RELATED_TO, CONTRADIZ, COMPLEMENTA

### Diffstory (placeholder — preenchido em Phase 3)
Nenhuma alteração de ficheiros rastreados pelo git (apenas execução de confirmação).
