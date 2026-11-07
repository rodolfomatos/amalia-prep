---
project: amalia-prep
created: 2026-11-07
current_sprint: sprint-01
current_ticket: ""
tier: AES-solo
---

# Kanban — amalia-prep

Source of truth for project state. Tickets mirror `PLAN.md`.

## Sprints

| Sprint | Period | Status | Goal |
|--------|--------|--------|------|
| sprint-01 | 2026-11-07 → 2026-11-14 | active | Infraestrutura de treino (M0) + datasets sintéticos (M1, M2) |

## Tickets

| ID | Title | Sprint | Status | AC |
|----|-------|--------|--------|----|
| T001 | Ambiente de treino (Ollama + Python + deps) | sprint-01 | done | `make setup` roda sem erros |
| T002 | Script de fine-tune (QLoRA) | sprint-01 | pending | `make train` executa e produz modelo |
| T003 | Script de avaliação offline | sprint-01 | pending | `make eval` roda 3 testes e reporta métricas |
| T101 | 100 exemplos de observação → mecanismo latente | sprint-01 | done | Cada exemplo tem `observation`, `latent_variable`, `context` |
| T102 | 5 categorias de latente (como dataset do ACA) | sprint-01 | done | 20 exemplos por categoria |
| T103 | Dataset válido (JSONL, sem duplicatas) | sprint-01 | done | 100 linhas, todas únicas, schema válido |
| T201 | 50 exemplos de ilha → conteúdo conectado/isolado | sprint-01 | done | Cada exemplo tem `ilhas`, `relacoes`, `conteudo`, `novidade_esperada` |
| T202 | Ilhas com múltiplos tipos de relação | sprint-01 | pending | Pelo menos 3 tipos diferentes (RELATED_TO, CONTRADIZ, COMPLEMENTA) |
| T203 | Dataset válido (JSONL, sem duplicatas) | sprint-01 | pending | 50 linhas, todas únicas, schema válido |
| T301 | Fine-tune qwen3:8b em abdução | — | pending | Modelo salva, não diverge (loss < 2.0) |
| T302 | Fine-tune qwen3:8b em saliência | — | pending | Modelo salva, não diverge |
| T303 | Modelo `amalia` disponível no Ollama local | — | pending | `ollama list` mostra `amalia` |
| T401 | Teste de abdução (acurácia > 0.3) | — | pending | `eval/test_abduction.py` passa |
| T402 | Teste de saliência relacional | — | pending | `eval/test_salience.py` passa |
| T403 | Teste de repeat limit (0 falhas em 100 calls) | — | pending | `eval/test_repeat_limit.py` passa |
| T501 | `ACA_LLM_MODEL="ollama/amalia"` funciona no ACA | — | pending | `run_t603_h6.py` roda com amalia |
| T502 | Re-executar H2, H3/H8, H6 com amalia | — | pending | Decisões registradas em `RESULTS.md` do ACA |

## Ordering constraints
- T001 → T101 → T301 → T401 → T501 → T502
- T201 → T302 → T402
- T301 → T401; T302 → T402; T303 → T401/T402/T403

## Notes
- AES-solo tier: no kanban enforcement, no peer review, no structured hostile analysis. Adversarial gate + memory system apply.
- To escalate to AES-standard (peer review + kanban + hostile analysis), re-run with `--tier=AES-standard`.
