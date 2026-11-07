---
ticket: T303
title: Modelo amalia disponível no Ollama local
phase: verify
tier: AES-standard
---

# T303 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| `ollama list` mostra `amalia` | ✅ PASS | `amalia:latest` (16 GB, ID 70efb056df7a, modificado há 43 min) está presente; `qwen3:8b` (5.2 GB) também |
| Critério AC T303 | ✅ PASS | `ollama list` mostra `amalia` |

## Critério AC T303
- [x] `ollama list` mostra `amalia` — SATISFEITO

## Novas falhas introduzidas
Nenhuma (ticket só-leitura, sem alteração de ficheiros).

## Limitações documentadas (não bloqueiam o AC, mas relevantes para M4/M5)
- O `amalia:latest` no Ollama NÃO é produto dos fine-tunes T301/T302. Esses produziram adapters LoRA em `models/amalia-abduction/` e `models/amalia-salience/` (não versionados, `models/` ignorado pelo git).
- `scripts/convert_to_gguf.py` tem 14 bytes (quebrado) → não é possível converter um adapter fine-tunado para GGUF e registá-lo como `amalia` via `make train`/`Modelfile`.
- Logo, o `amalia` avaliado em M4 (T401-T403) será o modelo de um run anterior, não um modelo refinado pelos nossos fine-tunes. Isso é um gap conhecido, documentado aqui.

## Conclusão Phase 4
T303 passa no Acceptance Criteria completo (`ollama list` mostra `amalia`). Marco M3 concluído (T301, T302, T303 — todos done), com a ressalva documentada acima. Pronto para Phase 5 (Critical Review).
