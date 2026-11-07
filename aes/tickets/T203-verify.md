---
ticket: T203
title: Dataset valido (JSONL, sem duplicatas) — saliencia
phase: verify
tier: AES-standard
---

# T203 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| 50 linhas | ✅ PASS | `len(lines) == 50` |
| Todas as linhas únicas (id e conteúdo) | ✅ PASS | 50 IDs únicos, 50 conteúdos únicos |
| Schema válido em cada linha (id, conteudo, ilhas, relacoes top-level, novidade_esperada, total_relacoes, tipos_relacao, ilhas_conectadas, ilhas[i].{id,nome,descricao,relacoes[]}) | ✅ PASS | 0 campos faltando em todas as 50 linhas |
| JSONL válido (todas as linhas parseáveis) | ✅ PASS | 0 erros de parse |

## Critério AC T203
- [x] 50 linhas — SATISFEITO
- [x] Todas as linhas únicas — SATISFEITO
- [x] Schema válido — SATISFEITO

## Novas falhas introduzidas
Nenhuma (ticket só-leitura, sem alteração de ficheiros).

## Conclusão Phase 4
T203 passa no Acceptance Criteria completo. O artefato `data/salience_training.jsonl` está válido e pronto para consumo por T302 (fine-tune QLoRA de saliência) e T402 (avaliação de saliência). Marco M2 concluído (T201, T202, T203 — todos done). Pronto para Phase 5 (Critical Review).
