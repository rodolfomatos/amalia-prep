---
ticket: T403
title: Teste de repeat limit (0 falhas em 100 calls)
phase: learn
tier: AES-standard
---

# T403 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Executei `eval/test_repeat_limit.py::test_no_repeat_limit` contra `amalia` (100 chamadas). Resultado: 3/100 chamadas falharam com repeat limit, alvo 0 → FALHOU.

## O que correu bem
- Avaliação executada de fato (100 chamadas reais), não assumida.
- Resultado não mascarado (3/100 falhas reportado honestamente).
- Causa-raiz identificada: `amalia` não é do fine-tune T301.

## O que correu mal / pode melhorar
- `amalia` tem falhas de repeat limit (3/100), não atingindo o alvo de 0.
- Causa: `convert_to_gguf.py` quebrado → fine-tune T301 não registrado como `amalia`.
- Fine-tune T301 convergiu (loss < 2.0) mas não pôde ser validado via Ollama.

## Insight para o registo hostil
> **Categoria**: Avaliação contra modelo errado (padrão recorrente — T401, T402, T403)
> **Insight**: Todos os três testes de M4 falham porque o `amalia` no Ollama não é o modelo fine-tunado. O fine-tune em si convergiu (T301/T302 loss < 2.0), mas o gap de infra (convert_to_gguf.py quebrado) impede registrar e validar. Corrigir convert_to_gguf.py é o pré-requisito para M4 e M5 fazerem sentido.
> **Origem**: T403, consistente com T401/T402.
> **Impacto**: Bloqueia validação de M4 e integração de M5 até ser corrigido.
> **Aplicado a**: T401, T402, T403; relevante para M4, M5.
> **Data**: 2026-11-07

## Marco M4 — resultado
T401 (abduction, 0.00/20 > 0.3) — FALHOU. T402 (saliência, 0.00/20 > 0.5) — FALHOU. T403 (repeat limit, 3/100 > 0) — FALHOU.
Todos falham pela mesma causa-raiz: `amalia:latest` no Ollama não é dos fine-tunes T301/T302 (convert_to_gguf.py quebrado).
Próximo: corrigir convert_to_gguf.py, registar modelo fine-tunado como `amalia`, re-executar M4; depois M5 (integração ACA).
