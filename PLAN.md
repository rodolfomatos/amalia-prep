# Amália — Plano de Preparação de Modelo

## Milestones

| Milestone | Objetivo | Tickets | Status |
|-----------|----------|---------|--------|
| M0 | Infraestrutura de treino | T001-T003 | pendente |
| M1 | Dataset sintético de abdução | T101-T103 | pendente |
| M2 | Dataset sintético de saliência relacional | T201-T203 | pendente |
| M3 | Fine-tune QLoRA do qwen3:8b | T301-T303 | pendente |
| M4 | Avaliação offline contra critérios de aceitação | T401-T403 | pendente |
| M5 | Integração com o ACA | T501-T502 | pendente |

---

## Tickets

### M0 — Infraestrutura de treino

| ID | Título | AC verificável |
|----|--------|----------------|
| T001 | Ambiente de treino (Ollama + Python + deps) | `make setup` roda sem erros |
| T002 | Script de fine-tune (QLoRA) | `make train` executa e produz modelo |
| T003 | Script de avaliação offline | `make eval` roda 3 testes e reporta métricas |

### M1 — Dataset sintético de abdução

| ID | Título | AC verificável |
|----|--------|----------------|
| T101 | 100 exemplos de observação → mecanismo latente | Cada exemplo tem `observation`, `latent_variable`, `context` |
| T102 | 5 categorias de latente (como dataset do ACA) | 20 exemplos por categoria |
| T103 | Dataset válido (JSONL, sem duplicatas) | 100 linhas, todas únicas, schema válido |

### M2 — Dataset sintético de saliência relacional

| ID | Título | AC verificável |
|----|--------|----------------|
| T201 | 50 exemplos de ilha → conteúdo conectado/isolado | Cada exemplo tem `ilhas`, `relacoes`, `conteudo`, `novidade_esperada` |
| T202 | Ilhas com múltiplos tipos de relação | Pelo menos 3 tipos diferentes (RELATED_TO, CONTRADIZ, COMPLEMENTA) |
| T203 | Dataset válido (JSONL, sem duplicatas) | 50 linhas, todas únicas, schema válido |

### M3 — Fine-tune QLoRA

| ID | Título | AC verificável |
|----|--------|----------------|
| T301 | Fine-tune qwen3:8b em abdução | Modelo salva, não diverge (loss < 2.0) |
| T302 | Fine-tune qwen3:8b em saliência | Modelo salva, não diverge |
| T303 | Modelo `amalia` disponível no Ollama local | `ollama list` mostra `amalia` |

### M4 — Avaliação offline

| ID | Título | AC verificável |
|----|--------|----------------|
| T401 | Teste de abdução (acurácia > 0.3) | `eval/test_abduction.py` passa |
| T402 | Teste de saliência relacional | `eval/test_salience.py` passa |
| T403 | Teste de repeat limit (0 falhas em 100 calls) | `eval/test_repeat_limit.py` passa |

### M5 — Integração com o ACA

| ID | Título | AC verificável |
|----|--------|----------------|
| T501 | `ACA_LLM_MODEL="ollama/amalia"` funciona no ACA | `run_t603_h6.py` roda com amalia |
| T502 | Re-executar H2, H3/H8, H6 com amalia | Decisões registradas em `RESULTS.md` do ACA |

---

## Restrições de ordenação

- T001 antes de T101 (precisa de ambiente para gerar dados)
- T101 antes de T301 (precisa de dados para treinar)
- T201 antes de T302 (precisa de dados de saliência)
- T301 antes de T401 (precisa de modelo para avaliar)
- T302 antes de T402 (mesmo)
- T303 antes de T401/T402/T403 (precisa do modelo instalado)
- T401 antes de T501 (precisa validar antes de integrar)
- T501 antes de T502 (precisa do modelo integrado antes de re-executar hipóteses)

---

## Dependências externas

- GPU NVIDIA com VRAM suficiente para QLoRA (RTX 5090 com 32 GB é ideal)
- Ollama instalado e rodando
- Python 3.12+ com `peft`, `transformers`, `bitsandbytes`

---

## Rollback

Se o fine-tune não produzir melhoria mensurável, manter `qwen3:8b` como baseline e documentar a limitação no `NOT-PROVEN.md` do ACA.
