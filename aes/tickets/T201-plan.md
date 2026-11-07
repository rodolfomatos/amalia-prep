---
ticket: T201
title: 50 exemplos de ilha → conteúdo conectado/isolado
phase: plan
tier: AES-standard
---

# T201 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/salience_training.jsonl`: 50 linhas, seeds 0-49, gerado por `scripts/generate_salience_data.py`
- Schema atual por exemplo (top-level): `id, conteudo, ilhas, novidade_esperada, total_relacoes, tipos_relacao, ilhas_conectadas`
- `ilhas[i].relacoes` é aninhado (lista de `{ilha_id, tipo, forca}`); NÃO há top-level `relacoes`
- 5 tipos de relação presentes: AGREGADO_EM, COMPLEMENTA, CONTRADIZ, DERIVA_DE, RELATED_TO
- Todos os 50 exemplos são "conectados" (ilhas_conectadas > 0); nenhum isolado
- `eval/test_salience.py`: lê `conteudo`, `novidade_esperada`, `ilhas`, `ilhas_conectadas` — não lê top-level `relacoes`
- `scripts/generate_salience_data.py`: `RELATION_TYPES = [RELATED_TO, CONTRADIZ, COMPLEMENTA, DERIVA_DE, AGREGADO_EM]` (5 tipos)
- T001 concluído (ambiente pronto)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T201, T202, T203 AC; milestone M2)
- `scripts/generate_salience_data.py` (gerador, schema)
- `eval/test_salience.py` (contrato de leitura do dataset)
- `data/salience_training.jsonl` (50 exemplos reais)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Dataset tem 50 linhas — justificação: `wc -l = 50`
- [KNOWN] Cada exemplo tem `ilhas`, `conteudo`, `novidade_esperada` no top-level — justificação: inspeção
- [KNOWN] `relacoes` é aninhado em `ilhas[i].relacoes`, NÃO top-level — justificação: inspeção (top-level keys sem `relacoes`)
- [KNOWN] Testes não leem top-level `relacoes` — justificação: `eval/test_salience.py` lê `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`
- [INFERRED] PLAN.md T201 AC ("top-level `relacoes`") está impreciso em relação ao esquema real — evidence chain: PLAN diz top-level `relacoes`, código/testes usam aninhado → um dos dois está impreciso
- [ASSUMED] Adicionar `relacoes` top-level (lista achatada de todas as relações do exemplo, espelhando `total_relacoes`/`tipos_relacao`) satisfaz o AC literal sem quebrar testes — potential impact if false: testes continuam a passar (não usam o campo novo), AC fica literal
- [UNKNOWN] Se T202/T203 esperam esquema diferente — impact: alterar o schema agora pode afetar tickets subsequentes
- [UNKNOWN] Se a ausência de exemplos "isolados" (todos são conectados) é problema para T402 — impact: o teste `test_isolado_mais_novo_que_conectado` faria `pytest.skip`; observação, fora do escopo estrito de T201

### WHAT WASN'T SPECIFIED (that matters)
- Se `relacoes` deve ser top-level OU aninhado — PLAN e código discordam
- Se o dataset deve conter exemplos tanto conectados quanto isolados (T201 descreve "conectado/isolado")

### ALTERNATIVES I DIDN'T CHOOSE
- Alterar `eval/test_salience.py` para ler top-level `relacoes`: rejeitado — muda contrato executável, fora do escopo de T201
- Remover `ilhas[].relacoes` e usar só top-level: rejeitado — quebraria a estrutura de ilhas e os testes (que iteram `ilhas[i]`)
- Deixar como está e declarar PLAN.md errado: rejeitado — não corrige o AC; T201 não passaria literal

### INVITE CONTRADICTION
- Posso estar errado que o AC literal deve ser satisfeito: talvez o PLAN.md esteja certo e os dados estejam errados (deveriam ter top-level `relacoes`). Mas mudar os testes é fora do escopo de T201. Priorizo não quebrar o contrato executável e satisfazer o AC adicionando o campo faltante no nível top-level.
- A ausência de exemplos isolados deve ser corrigida agora? Não — escopo mínimo para T201 (schema). Registrada como observação para T402.

### RISKS & SIDE EFFECTS
- Campo `relacoes` top-level (lista achatada) — espelha `total_relacoes`/`tipos_relacao` já existentes; pequena redundância justificada
- Regenerar o dataset com o gerador alterado: mesmo conteúdo (mesmas seeds) + campo `relacoes` top-level; ids inalterados (`salience_0000`..`salience_0049`)

### COST OF BEING WRONG
- MEDIUM: se a decisão de schema estiver errada, T202/T203/T302/T402 herdam o esquema errado. Mitigação: manter `ilhas[].relacoes` intocado (testes não quebram) e apenas adicionar o campo top-level.

### REASONING SKELETON
Claim: adicionar `relacoes` top-level (lista achatada) espelhando as relações das ilhas torna T201 literal sem quebrar nada.
→ Premissa 1: PLAN.md T201 AC exige top-level `relacoes`
→ Premissa 2: testes leem `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas` (não top-level `relacoes`)
→ Premissa 3: adicionar um campo novo não remove o existente → testes continuam a passar
→ Inference: adicionar `relacoes` top-level satisfaz PLAN e preserva testes
→ Conclusion: implementar campo `relacoes` top-level (lista achatada)

### SCOPE BOUNDARIES
In scope: adicionar `relacoes` top-level a cada exemplo do dataset; atualizar gerador para emitir o campo.
Out of scope: T202 (3+ tipos de relação — já satisfeito), T203 (validação duplicatas), alterar testes, alterar PLAN.md, adicionar exemplos isolados, fine-tune.

## Phase 2 — Solution Proposal

### What I will change
1. `scripts/generate_salience_data.py`: no `generate_example`, adicionar `"relacoes": [r for ilha in islands for r in ilha["relacoes"]]` (lista achatada de todas as relações de todas as ilhas do exemplo) no nível superior do dict retornado.
2. `data/salience_training.jsonl`: regenerar com o gerador atualizado (mesmas seeds 0-49 → mesmo conteúdo + campo `relacoes` top-level).

### What I will NOT change (and why)
- Não vou alterar `eval/test_salience.py` (contrato executável, fora do escopo de T201)
- Não vou remover `ilhas[i].relacoes` (estrutura de ilhas, usada pelos testes)
- Não vou adicionar exemplos isolados agora (observação para T402, fora do escopo de T201)
- Não vou alterar `PLAN.md`

### Verification criteria
- Cada uma das 50 linhas tem chaves top-level `ilhas`, `relacoes`, `conteudo`, `novidade_esperada`
- 50 linhas, todas únicas (ids únicos)
- JSONL válido
- `relacoes` top-level é a lista achatada de todas as `ilhas[i].relacoes` (contagem bate com `total_relacoes`)

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
