---
ticket: T403
title: Teste de repeat limit (0 falhas em 100 calls)
phase: plan
tier: AES-standard
---

# T403 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `eval/test_repeat_limit.py`: faz 100 chamadas ao `amalia` via Ollama e exige 0 falhas de repeat limit; `test_no_repeat_limit` verifica se a resposta contém "repeat"/"limit"/"Error"
- `eval/test_repeat_limit.py` execução real (`make eval`): 3/100 chamadas falharam com repeat limit, alvo 0 → FALHOU

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M4: T403 teste de repeat limit, 0 falhas em 100 calls)
- eval/test_repeat_limit.py (lógica do teste)
- T303 (amalia não é dos fine-tunes)
- Resultado real: 3/100 falhas

### ASSUMPTIONS I'M MAKING
- [KNOWN] `amalia:latest` está no Ollama
- [KNOWN] `amalia:latest` NÃO é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado)
- [KNOWN] 3/100 chamadas falharam com repeat limit — justificação: execução real
- [INFERRED] Falha de T403 devida ao modelo não ser o fine-tunado (o fine-tune T301 convergiu e reduziu verbosidade/repetição, mas não foi registado)
- [UNKNOWN] Taxa de repeat limit do fine-tune T301 — não testável sem registar

### WHAT WASN'T SPECIFIED (that matters)
- Nenhuma variação relevante; AC é claro (0 falhas em 100 calls)

### ALTERNATIVES I DIDN'T CHOOSE
- Corrigir convert_to_gguf.py: rejeitado — fora do escopo de T403
- Mascarar o resultado: rejeitado

### INVITE CONTRADICTION
- 3/100 falhas é um dado válido; reportar honestamente é o correto.

### RISKS & SIDE EFFECTS
- Ticket só-read: nenhum risco de alteração de ficheiros.

### COST OF BEING WRONG
- BAIXO: falha documentada com evidência (3/100).

### REASONING SKELETON
Claim: T403 executa avaliação de repeat limit contra `amalia` e reporta resultado real (3/100 falhas, falha), com causa-raiz.
→ Premissa 1: T403 AC exige 0 falhas em 100 calls
→ Premissa 2: `amalia` não é dos fine-tunes T301/T302
→ Premissa 3: Execução real deu 3/100 falhas
→ Inference: T403 não passa no AC, resultado medido e documentado
→ Conclusion: executar, reportar falha com causa-raiz, não mascarar

### SCOPE BOUNDARIES
In scope: executar test_no_repeat_limit contra `amalia`; medir falhas; documentar.
Out of scope: corrigir modelo, re-treinar, re-registrar, corrigir convert_to_gguf.py.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Executar `eval/test_repeat_limit.py::test_no_repeat_limit`; medir falhas; documentar (3/100) com causa-raiz.

### What I will NOT change (and why)
- Não corrigir convert_to_gguf.py, não re-treinar, não re-registrar (fora do escopo)
- Não mascarar resultado

### Verification criteria
- `test_no_repeat_limit` executado; falhas medidas e reportadas (3/100)
- Causa-raiz documentada

### Diffstory
Nenhuma alteração de ficheiros rastreados pelo git (avaliação only-read).
