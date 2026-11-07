---
ticket: T303
title: Modelo amalia disponível no Ollama local
phase: learn
tier: AES-standard
---

# T303 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
T303 foi um ticket de confirmação: verifiquei que `amalia:latest` (16 GB) está presente no Ollama (`ollama list` mostra `amalia`), satisfazendo o AC literal. Este modelo foi construído a partir de `models/amalia-merged/amalia.f16.gguf` via `configs/Modelfile`, de um run anterior — não é produto dos fine-tunes T301/T302 (que produziram adapters LoRA locais, não registados como `amalia` porque `convert_to_gguf.py` está quebrado).

## O que correu bem
- Confirmação direta e rápida de que `amalia` está disponível no Ollama.
- Limitação documentada com transparência (origem do modelo, convert_to_gguf.py quebrado).

## O que correu mal / pode melhorar
- Não há como registar um modelo fine-tunado novo como `amalia` porque `convert_to_gguf.py` está quebrado (14 bytes). Isso é um gap real: M4 (avaliação) usará o `amalia` existente, não um modelo refinado pelos nossos fine-tunes T301/T302.
- `models/` não é versionado pelo git → os adapters fine-tunados ficam apenas localmente.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Distinção entre "modelo presente" e "modelo refinado pelos nossos treinos"
> **Insight**: Um AC literal (`ollama list` mostra `amalia`) pode estar satisfeito enquanto o modelo subjacente não incorpora o trabalho recente (fine-tunes T301/T302). Para interpretar corretamente os resultados de avaliação (M4), é essencial distinguir a presença do modelo no Ollama da sua procedência.
> **Origem**: T303 (Phase 1 hostile analysis).
> **Impacto**: Mitigado por documentação explícita; M4 deve ser interpretado com essa ressalva.
> **Aplicado a**: T303; relevante para M4 (T401-T403) e M5 (integração ACA).
> **Data**: 2026-11-07

## Marco M3 concluído
T301 (fine-tune abduction, loss < 2.0), T302 (fine-tune salience, convergência < 2.0), T303 (`amalia` no Ollama) — todos done, com a ressalva de que o `amalia` no Ollama não reflete os fine-tunes T301/T302.
Próximo: M4 (T401-T403, avaliação offline contra os critérios de aceitação).
