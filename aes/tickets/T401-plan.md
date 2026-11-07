---
ticket: T401
title: Teste de abdução (acurácia > 0.3)
phase: plan
tier: AES-standard
---

# T401 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `eval/test_abduction.py`: testa se o modelo adivinha variáveis latentes; `test_abduction_accuracy` roda 20 exemplos (load_examples default) e exige acurácia > 0.3
- `data/abduction_training.jsonl`: 100 exemplos, versão no git (T103)
- Ollama: `amalia:latest` presente (T303), mas NÃO é produto dos fine-tunes T301/T302
- `scripts/check_acceptance.py`: também mede latência e repeat limit (não parte de T401)
- Execução prévia (`make eval`): `test_abduction_accuracy` → acurácia 0.00 (0/20), alvo > 0.3 → FALHOU

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M4: T401 teste de abdução, acurácia > 0.3)
- eval/test_abduction.py (lógica do teste, limiar 0.3)
- data/abduction_training.jsonl (dataset usado)
- T303-plan/verify (limitação: amalia não é dos nossos fine-tunes)
- Resultado real da execução: acurácia 0.00 (0/20)

### ASSUMPTIONS I'M MAKING
- [KNOWN] `amalia:latest` está no Ollama — justificação: `ollama list` mostra
- [KNOWN] O `amalia:latest` NÃO reflete os fine-tunes T301/T302 — justificação: convert_to_gguf.py quebrado (14 bytes), impedindo registo de modelos fine-tunados
- [KNOWN] A acurácia de abdução é 0.00 (0/20) — justificação: execução real de `eval/test_abduction.py`
- [INFERRED] A falha de T401 é devida ao modelo avaliado não ser o modelo fine-tunado — evidence chain: fine-tunes T301/T302 convergiram (loss < 2.0) mas não foram registados como `amalia`; o `amalia` avaliado é de um run anterior
- [ASSUMED] Se convert_to_gguf.py fosse corrigido e os fine-tunes registados, a acurácia melhoraria — potential impact if false: o modelo base pode não aprender abdução mesmo fine-tunado (hipótese não testável sem registar)
- [UNKNOWN] Qual acurácia o modelo fine-tunado T301 alcançaria — impact: não testável sem registar o modelo no Ollama

### WHAT WASN'T SPECIFIED (that matters)
- Se T401 exige que o `amalia` seja o modelo fine-tunado, ou apenas qualquer modelo chamado `amalia`
- O que fazer quando a avaliação falha por limitação de infra (convert_to_gguf.py) e não por qualidade do fine-tune

### ALTERNATIVES I DIDN'T CHOOSE
- Corrigir convert_to_gguf.py e re-registrar o modelo: rejeitado — fora do escopo de T401 (avaliação), complexo (GGUF/llama.cpp)
- Declarar T401 "não aplicável" porque o modelo não é nosso: rejeitado — o AC é executável e foi executado; o resultado (falha) é um dado válido
- Mascarar o resultado como "passou": rejeitado — viola o princípio "se não é testado, está quebrado" e "não yes-men"

### INVITE CONTRADICTION
- Posso estar errado que a falha deve ser reportada como tal: talvez o ACE critério deva ser avaliado contra o modelo disponível, independentemente da procedência. Mas o resultado é o que é (0.00), e mascará-lo seria desonesto.

### RISKS & SIDE EFFECTS
- Ticket só-read sobre o modelo: nenhum risco de alteração de ficheiros.
- Risco residual: M5 (integração ACA) dependeria de um `amalia` funcional, que atualmente não atende aos critérios.

### COST OF BEING WRONG
- BAIXO: a falha é documentada com evidência (0.00/20). Não bloqueia o projeto; aponta para o gap real (convert_to_gguf.py).

### REASONING SKELETON
Claim: T401 executa a avaliação de abdução contra `amalia` e reporta o resultado real (0.00/20, falha), com a causa-raiz documentada.
→ Premissa 1: T401 AC exige acurácia > 0.3 em test_abduction_accuracy
→ Premissa 2: O `amalia` no Ollama não é dos nossos fine-tunes (convert_to_gguf.py quebrado)
→ Premissa 3: A execução real deu acurácia 0.00 (0/20)
→ Inference: T401 não passa no AC, mas o resultado é medido e documentado honestamente
→ Conclusion: executar avaliação, reportar falha com causa-raiz, não mascarar

### SCOPE BOUNDARIES
In scope: executar test_abduction_accuracy contra `amalia`; medir acurácia; documentar resultado e causa-raiz.
Out of scope: corrigir o modelo, re-treinar, re-registrar no Ollama, corrigir convert_to_gguf.py.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Executar `eval/test_abduction.py::test_abduction_accuracy` contra `amalia`; medir acurácia; documentar no verify/review/learn.

### What I will NOT change (and why)
- Não vou corrigir convert_to_gguf.py (fora do escopo de T401)
- Não vou re-treinar ou re-registrar o modelo (fora do escopo)
- Não vou mascarar o resultado (violation of "não yes-men")

### Verification criteria
- `eval/test_abduction.py::test_abduction_accuracy` executado; acurácia medida e reportada (0.00/20)
- Resultado documentado com causa-raiz (amalia não é dos fine-tunes T301/T302)

### Diffstory (placeholder — preenchido em Phase 3)
Nenhuma alteração de ficheiros rastreados pelo git (avaliação only-read).
