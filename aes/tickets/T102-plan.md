---
ticket: T102
title: 5 categorias de latente, 20 exemplos por categoria
phase: plan
tier: AES-standard
---

# T102 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `data/abduction_training.jsonl`: 100 linhas, distribuição 23/19/17/20/21 (não 20/categoria)
- `scripts/generate_abduction_data.py`: `generate_example(seed)` escolhe categoria aleatória via `rng.choice(list(LATENT_CATEGORIES.keys()))`; `main()` gera `args.count` exemplos com seeds sequenciais
- Schema (pós-T101): `id, category, observation, latent_variable(top-level), context, ground_truth{latent_variable, mechanism}`
- `eval/test_abduction.py` lê `ground_truth.latent_variable` — não quebrar
- T101 concluído (top-level `latent_variable` presente)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (T102: "5 categorias de latente", "20 exemplos por categoria")
- `scripts/generate_abduction_data.py` (gerador, distribuição aleatória)
- `data/abduction_training.jsonl` (distribuição real 23/19/17/20/21)

### ASSUMPTIONS I'M MAKING
- [KNOWN] Distribuição atual não é 20/categoria — justificação: contagem real (23/19/17/20/21)
- [KNOWN] Gerador escolhe categoria aleatoriamente — justificação: código `rng.choice(list(LATENT_CATEGORIES.keys()))`
- [INFERRED] Para satisfazer T102, o gerador deve distribuir `--count` igualmente pelas categorias — evidence chain: AC exige 20/categoria; distribuição aleatória não garante isso → lógica de distribuição controlada necessária
- [ASSUMED] Manter seed sequencial por exemplo + categoria explícita produz latentes determinísticos e IDs únicos — potential impact if false: `rng.choice` dentro de uma categoria pode repetir latentes (aceitável; T103 valida IDs únicos, não latentes únicos)
- [UNKNOWN] Se T103 espera um esquema de seeds específico — impact: alterar o esquema de seeds pode afetar T103

### WHAT WASN'T SPECIFIED (that matters)
- Como lidar com `--count` não divisível por 5 (ex: 102) — distribuir resto (1,1,0,0,0) é razoável
- Se a ordem dos exemplos no JSONL importa (agrupados por categoria vs intercalados) — não especificado; agrupados por categoria é mais claro e determinístico

### ALTERNATIVES I DIDN'T CHOOSE
- Manter geração aleatória e filtrar até bater 20/categoria: rejeitado — não determinístico, poderia loopar indefinidamente, complexo
- Adicionar parâmetro `--count-per-category`: rejeitado — muda a CLI mais do que necessário; `--count` total distribuído é mais limpo e retrocompatível para counts divisíveis por 5
- Gerar categorias em round-robin sem `rng` para escolha de categoria: escolhido implicitamente (iterar categorias ordenadas)

### INVITE CONTRADICTION
- Posso estar errado que agrupar por categoria no JSONL é aceitável: se a ordem aleatória for importante para treino, isso poderia ser um problema. Mitigação: o fine-tune (T301) embaralha normalmente; ordem no JSONL não afeta o modelo.
- O esquema de seed (índice sequencial) pode produzir latentes repetidos dentro de uma categoria: aceitável para T102 (AC não exige latentes únicos).

### RISKS & SIDE EFFECTS
- Conteúdo do dataset muda (exemplos diferentes dos de T101) — esperado, T102 redefine a distribuição
- IDs continuam únicos (contador sequencial global)
- Campo `latent_variable` de topo (T101) preservado — não regressão

### COST OF BEING WRONG
- MEDIUM: distribuição errada propaga para T301 (fine-tune desbalanceado por categoria) e T401 (avaliação). Mitigação: validação explícita de 20/categoria na Phase 4.

### REASONING SKELETON
Claim: distribuir `--count` igualmente pelas 5 categorias (iterando categorias ordenadas, seed sequencial) satisfaz T102.
→ Premissa 1: T102 AC exige 20 exemplos por cada uma das 5 categorias
→ Premissa 2: gerador atual escolhe categoria aleatoriamente → não garante 20/categoria
→ Premissa 3: iterar categorias ordenadas com contador por categoria garante exatamente count//n (ou +1 para o resto)
→ Inference: modificar `main` para loop categoria×contador satisfaz o AC
→ Conclusion: implementar distribuição controlada por categoria

### SCOPE BOUNDARIES
In scope: modificar gerador para distribuição por categoria; regenerar dataset com 20/categoria; preservar schema T101.
Out of scope: T103 (validação formal), alterar testes, alterar PLAN.md, fine-tune.

## Phase 2 — Solution Proposal

### What I will change
1. `scripts/generate_abduction_data.py`:
   - `generate_example(seed, category=None)`: aceita categoria opcional; se None, escolhe aleatoriamente (compatível com uso direto).
   - `main()`: distribui `args.count` igualmente pelas categorias ordenadas (base = count // 5, resto distribuído nas primeiras categorias); itera categoria × contador com seed sequencial global; escreve JSONL.
2. `data/abduction_training.jsonl`: regenerar com `--count 100` → 20/categoria.

### What I will NOT change (and why)
- Não remover a escolha aleatória de categoria quando `category=None` (compatibilidade)
- Não alterar `eval/test_abduction.py` (contrato executável)
- Não remover `latent_variable` top-level (T101) nem `ground_truth.latent_variable` (testes)

### Verification criteria
- 100 linhas, exatamente 20 por cada uma das 5 categorias
- Cada linha com `observation`, `latent_variable` (top-level), `context`, `ground_truth.latent_variable`
- IDs únicos (sequenciais `abduction_0000`..)
- JSONL válido

### Diffstory (placeholder — preenchido em Phase 3)
Aguardar implementação.
