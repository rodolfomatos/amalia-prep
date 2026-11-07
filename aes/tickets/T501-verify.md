---
ticket: T501
title: ACA_LLM_MODEL="ollama/amalia" funciona no ACA
phase: verify
tier: AES-standard
---

# T501 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| Verificar disponibilidade do repositório ACA | ❌ BLOQUEADO | Repositório ACA não está disponível neste projeto (externo) |
| Executar `run_t603_h6.py --seeds 5 --items 20` com `ACA_LLM_MODEL="ollama/amalia"` | ❌ NÃO EXECUTÁVEL | Sem acesso ao ACA nem aos scripts `run_t*.py` |
| `amalia` no Ollama | ✅ CONFIRMADO | `amalia:latest` presente (T303), mas não é dos fine-tunes T301/T302 |

## Critério AC T501
- [ ] `ACA_LLM_MODEL="ollama/amalia"` funciona no ACA (`run_t603_h6.py` executa) — NÃO PODE SER VERIFICADO (dependência externa)

## Causa-raiz (documentada com evidência)
T501 depende do repositório ACA, que é um projeto separado e não está disponível neste ambiente (https://github.com/rodolfomatos/amalia-prep é este projeto). Sem o ACA, não é possível executar `run_t603_h6.py` nem configurar `ACA_LLM_MODEL="ollama/amalia"`.

## Novas falhas introduzidas
Nenhuma (ticket de documentação de bloqueio).

## Conclusão Phase 4
T501 NÃO pode ser executado neste projeto: bloqueado por dependência externa (repositório ACA). O AC não pode ser verificado aqui. Documentado com evidência. Pronto para Phase 5.
