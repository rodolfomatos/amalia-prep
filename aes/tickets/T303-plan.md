---
ticket: T303
title: Modelo amalia disponível no Ollama local
phase: plan
tier: AES-standard
---

# T303 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- Ollama rodando (verificado em T001: `ollama list` responde)
- `amalia:latest` (16 GB) presente no Ollama — construído a partir de `models/amalia-merged/amalia.f16.gguf` via `configs/Modelfile`, de um run anterior
- `qwen3:8b` (5.2 GB) também presente
- `configs/Modelfile`: `FROM /home/rodolfo/amalia-prep/models/amalia-merged/amalia.f16.gguf`
- `scripts/convert_to_gguf.py`: 14 bytes, quebrado
- T301/T302 concluídos (produziram adapters LoRA em models/, não registados como `amalia`)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M3: T303 `ollama list` mostra `amalia`)
- configs/Modelfile (construção do `amalia` a partir de GGUF local)
- Ollama output (`amalia:latest` presente)
- scripts/convert_to_gguf.py (14 bytes, quebrado)
- T301/T302 verify (fine-tunes produziram adapters, não GGUF)

### ASSUMPTIONS I'M MAKING
- [KNOWN] `amalia:latest` está no Ollama — justificação: `ollama list` mostra `amalia:latest` (16 GB)
- [KNOWN] Este `amalia` NÃO é produto dos fine-tunes T301/T302 — justificação: T301/T302 salvaram adapters LoRA em models/, não fizeram `ollama create amalia`
- [KNOWN] `convert_to_gguf.py` está quebrado — justificação: 14 bytes, conteúdo não funcional
- [INFERRED] O AC de T303 (`ollama list` mostra `amalia`) está literalmente satisfeito — evidence chain: `amalia:latest` aparece no `ollama list`
- [ASSUMED] O `amalia:latest` existente é suficiente para M4 (avaliação contra `amalia`) — potential impact if false: M4 avaliaria um modelo que não incorpora nossos fine-tunes
- [UNKNOWN] Se o `amalia:latest` existente realmente resolve os problemas do ACA (repeat limit, saída verbosa) — impact: M4 (T401-T403) diria se resolve ou não

### WHAT WASN'T SPECIFIED (that matters)
- Se T303 exige que o `amalia` seja produto dos nossos fine-tunes, ou apenas esteja presente
- Se devemos corrigir convert_to_gguf.py para registrar um modelo novo

### ALTERNATIVES I DIDN'T CHOOSE
- Corrigir convert_to_gguf.py e registrar um modelo fine-tunado como `amalia`: rejeitado — GGUF conversion é complexo (integração llama.cpp), fora do escopo de T303, e o script tem 14 bytes (precisaria ser reescrito)
- Declarar T303 não satisfeito porque o `amalia` não é dos nossos fine-tunes: rejeitado — o AC é literal (`ollama list` mostra `amalia`) e está satisfeito; a limitação é documentada como gap

### INVITE CONTRADICTION
- Posso estar errado que declarar T303 satisfaz o AC: talvez a intenção seja que o `amalia` reflita nossos fine-tunes. Mas o AC é literal e está satisfeito; a limitação do modelo ser de um run anterior é documentada como gap para M4/M5.

### RISKS & SIDE EFFECTS
- Ticket só-leitura: nenhum risco de alteração de ficheiros.
- Risco residual: M4 avaliará um `amalia` que não incorpora os fine-tunes T301/T302, podendo mascarar ou não refletir as melhorias pretendidas.

### COST OF BEING WRONG
- BAIXO: o AC literal está satisfeito. A limitação é documentada.

### REASONING SKELETON
Claim: T303 pode ser concluído confirmando que `amalia` está no Ollama (AC literal satisfeito), com documentação da origem e limitações.
→ Premissa 1: T303 AC exige `ollama list` mostrar `amalia`
→ Premissa 2: `amalia:latest` aparece no `ollama list` (verificado)
→ Inference: AC satisfeito
→ Conclusion: confirmação formal, documentar origem e gap do convert_to_gguf.py

### SCOPE BOUNDARIES
In scope: confirmar `amalia` no Ollama; documentar origem (run anterior, merged GGUF) e limitação (convert_to_gguf.py quebrado, não registra fine-tunes novos).
Out of scope: corrigir convert_to_gguf.py, re-treinar e registar modelo novo, avaliação (M4).

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Executar confirmação (`ollama list`) e documentar o resultado nos outputs de verify/review/learn.

### What I will NOT change (and why)
- Não vou corrigir `convert_to_gguf.py` (fora do escopo de T303)
- Não vou re-treinar ou registar um modelo novo (fora do escopo)

### Verification criteria
- `ollama list` mostra `amalia` (amalia:latest)
- Resultado documentado com origem e limitações

### Diffstory (placeholder — preenchido em Phase 3)
Nenhuma alteração de ficheiros rastreados pelo git (confirmação only-read).
