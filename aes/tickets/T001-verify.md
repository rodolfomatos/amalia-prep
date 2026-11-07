---
ticket: T001
title: Ambiente de treino (Ollama + Python + deps)
phase: verify
tier: AES-standard
---

# T001 — Verify Output (Phase 4)

## Gates executados

| Gate | Resultado | Detalhes |
|------|-----------|----------|
| `make setup` | ✅ PASS | exit code 0, todas as dependências `Requirement already satisfied`, Ollama verificado, `✓ Setup completo` |
| Versões fixas batem com instaladas | ✅ PASS | `requirements.txt` agora usa `==` aos valores instalados (torch 2.15.0, transformers 5.22.2, peft 0.21.2, bitsandbytes 0.50.2, datasets 5.1.0, accelerate 1.15.0, ruff 0.17.4, pytest 9.2.0) |
| `make lint` | ⚠️ PRE-EXISTING FAIL | 21 erros em `eval/` (ex: `F401` unused `sys`, `PLW1510` `subprocess.run` sem `check`). **Não introduzidos por esta alteração** (único diff: `requirements.txt`). Fora do escopo de T001. Reportado, não bloqueante. |
| Critério AC T001 (`make setup` sem erros) | ✅ PASS | exit code 0 |

## Novas falhas introduzidas por esta alteração
Nenhuma. O único diff é `requirements.txt` (pinning de versões), que não é verificado por `ruff` e não afeta lint/testes.

## Falhas pré-existentes (reportadas, não bloqueantes)
- 21 erros de ruff em `eval/test_abduction.py` e possivelmente `scripts/` — pré-existentes ao commit inicial, não relacionados a T001.
- Sugestão: adicionar a correção destes erros ao `docs/ROADMAP.md` como backlog (tag [DISCOVERED] ou [TECH-DEBT]).

## Verificação de regressão
- `make setup` continua a passar com versões fixas (não quebrou instalação).
- `.venv` mantido; não foram removidos pacotes.

## Conclusão Phase 4
T001 passa no seu Acceptance Criteria (`make setup` roda sem erros). A alteração de pinning de versões é segura e não introduz regressões. Pronto para Phase 5 (Critical Review).
