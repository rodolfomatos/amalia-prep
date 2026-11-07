---
ticket: T301
title: Fine-tune qwen3:8b em abdução
phase: verify
tier: AES-standard
---

# T301 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| Fine-tune executa sem erro | ✅ PASS | exit code 0, "Fine-tune concluído!", 75 passos em ~112s |
| Modelo salvo (adapter + tokenizer) | ✅ PASS | `models/amalia-abduction/` com adapter_model.safetensors (61 MB), adapter_config.json, tokenizer.json, checkpoints |
| Loss final < 2.0 | ✅ PASS | Loss convergiu 6.519 → 0.149; `train_loss: 1.142` (última métrica do Trainer); todos os passos finais < 2.0 (0.2081 → 0.1502 → 0.149) |
| Modelo não diverge | ✅ PASS | Loss diminuiu monotonicamente nos últimos passos; sem divergência |
| Suporte single-dataset no gerador | ✅ PASS | `fine_tune.py` aceita `--salience-data` opcional; treinou apenas abduction |

## Critério AC T301
- [x] Fine-tune executa e produz modelo salvo — SATISFEITO
- [x] Loss < 2.0 (não diverge) — SATISFEITO (loss final 0.149; train_loss 1.142)

## Novas falhas introduzidas por esta alteração
Nenhuma. A alteração no fine_tune.py (salience opcional) é retrocompatível (treino combinado ainda funciona quando ambos passados).

## Falhas encontradas e corrigidas (não são regressões)
- 1ª execução falhou com **CUDA Out of Memory** (batch-size 4, 19.47 GiB usados). Corrigido reduzindo `--batch-size 1` e ativando `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`. A 2ª execução completou com sucesso.
- Isso foi uma falha de ambiente/memória, introduzida e corrigida dentro de T301; não regressa.

## Modelos não versionados
`models/` está ignorado pelo `.gitignore` (16 GB+, não cabe no git). O artefato `models/amalia-abduction/` existe apenas localmente. O código que o produz (`scripts/fine_tune.py`) está versionado.

## Conclusão Phase 4
T301 passa no Acceptance Criteria completo (modelo salvo, loss < 2.0, sem divergência). Pronto para Phase 5 (Critical Review).
