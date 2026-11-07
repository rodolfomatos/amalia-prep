---
ticket: T501
title: ACA_LLM_MODEL="ollama/amalia" funciona no ACA
phase: plan
tier: AES-standard
---

# T501 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- PLAN.md (M5: T501 `ACA_LLM_MODEL="ollama/amalia"` funciona no ACA; T502 re-executar H2/H3/H8/H6)
- Repositório atual: https://github.com/rodolfomatos/amalia-prep (ESTE projeto)
- Repositório ACA: EXTERNO, não disponível neste projeto
- `amalia:latest` presente no Ollama (T303), mas NÃO é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M5 T501, T502)
- T303 (amalia no Ollama, de run anterior, não dos nossos fine-tunes)
- Não há acesso ao repositório ACA neste ambiente

### ASSUMPTIONS I'M MAKING
- [KNOWN] O repositório ACA não está disponível aqui — justificação: este projeto é amalia-prep, separado do ACA
- [KNOWN] T501 requer executar `run_t603_h6.py --seeds 5 --items 20` no ACA com `ACA_LLM_MODEL="ollama/amalia"`
- [INFERRED] T501 não pode ser concluído neste projeto — evidence chain: não há acesso ao repositório ACA nem aos scripts `run_t603_h6.py`
- [ASSUMED] Quando o ACA estiver disponível, T501 poderá ser executado — potential impact if false: o `amalia` pode não funcionar no ACA (não testável aqui)
- [UNKNOWN] Se o `amalia:latest` funciona corretamente no ACA — não testável sem o ACA

### WHAT WASN'T SPECIFIED (that matters)
- O caminho/local do repositório ACA
- Se T501 pode ser considerado "concluído" sem execução real (não — requer execução)

### ALTERNATIVES I DIDN'T CHOOSE
- Executar T501 aqui: rejeitado — impossível (não há ACA nem scripts)
- Mascarar como concluído: rejeitado — "não yes-men", "se não é testado, está quebrado"

### INVITE CONTRADICTION
- O resultado é um bloqueio por dependência externa, documentado honestamente.

### RISKS & SIDE EFFECTS
- Ticket só-read/documentação: nenhum risco de alteração de ficheiros.
- Risco residual: M5 não pode ser concluído sem o repositório ACA.

### COST OF BEING WRONG
- BAIXO: bloqueio documentado com evidência.

### REASONING SKELETON
Claim: T501 não pode ser executado neste projeto porque depende do repositório ACA externo.
→ Premissa 1: T501 AC exige executar `run_t603_h6.py` no ACA com `ACA_LLM_MODEL="ollama/amalia"`
→ Premissa 2: O repositório ACA não está disponível neste ambiente
→ Inference: T501 não pode ser executado aqui
→ Conclusion: documentar bloqueio por dependência externa; não mascarar

### SCOPE BOUNDARIES
In scope: documentar que T501 requer o repositório ACA externo e não pode ser executado aqui.
Out of scope: executar T501 (impossível sem o ACA), corrigir o modelo.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Documentar o bloqueio por dependência externa (repositório ACA) nos outputs verify/review/learn.

### What I will NOT change (and why)
- Não vou tentar executar T501 aqui (impossível)
- Não vou mascarar o bloqueio

### Verification criteria
- Bloqueio documentado com evidência (repositório ACA não disponível)

### Diffstory
Nenhuma alteração de ficheiros rastreados pelo git (documentação de bloqueio).
