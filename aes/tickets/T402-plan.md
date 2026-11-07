---
ticket: T402
title: Teste de saliência relacional (acurácia > 0.5)
phase: plan
tier: AES-standard
---

# T402 — Plan Output (Phase 1 Hostile Analysis + Phase 2 Solution Proposal)

## Phase 0 — Reconnaissance (resumo)

- `eval/test_salience.py`: testa diferenciação de conteúdos conectados (menos novos) vs isolados (mais novos); `test_novidade_diferenciacao` roda exemplos (load_examples default 20) e exige acurácia > 0.5; `test_isolado_mais_novo_que_conectado` compara isolados vs conectados
- `data/salience_training.jsonl`: 50 exemplos, versão no git (T203); todos conectados (0 isolados)
- `eval/test_salience.py` execução real (`make eval`): acurácia de saliência 0.00 (0/20), alvo > 0.5 → FALHOU; `test_isolado_mais_novo_que_conectado` PULADO (sem isolados)

## Phase 1 — Hostile Analysis

### INSIGHTS CONSULTED
- PLAN.md (M4: T402 teste de saliência, acurácia > 0.5)
- eval/test_salience.py (lógica dos testes)
- data/salience_training.jsonl (todos conectados, 0 isolados)
- T303 (amalia não é dos fine-tunes T301/T302)
- Resultado real: acurácia 0.00 (0/20); isolado-vs-conectado pulado

### ASSUMPTIONS I'M MAKING
- [KNOWN] `amalia:latest` está no Ollama — justificação: `ollama list`
- [KNOWN] `amalia:latest` NÃO é dos fine-tunes T301/T302 — justificação: convert_to_gguf.py quebrado
- [KNOWN] Acurácia de saliência é 0.00 (0/20) — justificação: execução real
- [INFERRED] Falha de T402 devida ao modelo não ser o fine-tunado — evidence chain: fine-tune T302 convergiu (loss < 2.0) mas não foi registado; `amalia` avaliado é de run anterior
- [ASSUMED] Corrigir convert_to_gguf.py e re-registrar melhoraria a acurácia — potential impact if false: não testável sem registar
- [UNKNOWN] Acurácia que o fine-tune T302 alcançaria — não testável sem registar

### WHAT WASN'T SPECIFIED (that matters)
- Se `test_isolado_mais_novo_que_conectado` (pulado) é parte obrigatória de T402 — não é, o AC é `test_novidade_diferenciacao` > 0.5

### ALTERNATIVES I DIDN'T CHOOSE
- Corrigir convert_to_gguf.py: rejeitado — fora do escopo de T402
- Declarar T402 não aplicável: rejeitado — o AC é executável, resultado (falha) é dado válido
- Mascarar resultado: rejeitado — "não yes-men", "se não é testado, está quebrado"

### INVITE CONTRADICTION
- O resultado 0.00 é um dado válido de avaliação, não um erro de código. Reportá-lo honestamente é o correto.

### RISKS & SIDE EFFECTS
- Ticket só-read: nenhum risco de alteração de ficheiros.

### COST OF BEING WRONG
- BAIXO: falha documentada com evidência (0.00/20).

### REASONING SKELETON
Claim: T402 executa avaliação de saliência contra `amalia` e reporta resultado real (0.00/20, falha), com causa-raiz documentada.
→ Premissa 1: T402 AC exige acurácia > 0.5 em test_novidade_diferenciacao
→ Premissa 2: `amalia` não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado)
→ Premissa 3: Execução real deu acurácia 0.00 (0/20)
→ Inference: T402 não passa no AC, resultado medido e documentado honestamente
→ Conclusion: executar, reportar falha com causa-raiz, não mascarar

### SCOPE BOUNDARIES
In scope: executar test_novidade_diferenciacao contra `amalia`; medir; documentar.
Out of scope: corrigir modelo, re-treinar, re-registrar, corrigir convert_to_gguf.py.

## Phase 2 — Solution Proposal

### What I will change
Nenhum ficheiro de código. Executar `eval/test_salience.py::test_novidade_diferenciacao`; medir acurácia; documentar (0.00/20) com causa-raiz.

### What I will NOT change (and why)
- Não corrigir convert_to_gguf.py, não re-treinar, não re-registrar (fora do escopo de T402)
- Não mascarar resultado

### Verification criteria
- `test_novidade_diferenciacao` executado; acurácia medida e reportada (0.00/20)
- Causa-raiz documentada

### Diffstory
Nenhuma alteração de ficheiros rastreados pelo git (avaliação only-read).
