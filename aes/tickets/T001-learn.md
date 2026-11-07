---
ticket: T001
title: Ambiente de treino (Ollama + Python + deps)
phase: learn
tier: AES-standard
---

# T001 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
Verificámos que `make setup` já funcionava (exit code 0, `.venv` com todas as dependências, Ollama a correr com `amalia:latest` e `qwen3:8b`). A única alteração feita foi fixar versões exatas (`==`) em `requirements.txt` para que o ambiente de treino seja reprodutível em qualquer máquina — risco identificado na hostile analysis (dependências com `>=` resolvem versões diferentes em máquinas diferentes, o que afeta a reprodutibilidade do fine-tune QLoRA).

## O que correu bem
- `make setup` passa antes e depois da alteração (sem regressões).
- Hostile analysis surfou o risco de reprodutibilidade antes de qualquer alteração.
- Alteração cirúrgica: um só ficheiro, sem tocar em código adjacente.

## O que correu mal / pode melhorar
- 21 erros de ruff pré-existentes em `eval/test_abduction.py` (e possivelmente `scripts/`). Não são da responsabilidade de T001, mas deixam o projeto sem `make lint` verde. Devem ser endereçados como tech debt separado.
- Não há verificação de versão mínima do Python (3.12+) nem de GPU dentro do target `setup` — documentado como risco, fora do escopo deste ticket.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Reprodutibilidade de ambiente
> **Insight**: Em projetos de fine-tune ML, dependências não fixas (`>=`) em `requirements.txt` tornam o ambiente de treino não reprodutível; pequenas diferenças de versão de torch/transformers/peft podem alterar o comportamento do treino sem que `make setup` sinalize erro.
> **Origem**: Hostile analysis de T001 (Phase 1).
> **Impacto**: Mitigado por pinning de versões em `requirements.txt`.
> **Aplicado a**: T001; relevante para todos os tickets de treino e avaliação (T301-T403).
> **Data**: 2026-11-07

## Próximo ticket na sequência
T101 (100 exemplos de observação → mecanismo latente), dependente de T001 (ambiente pronto para gerar dados). Ordem de execução: T001 → T101 → T102 → T103 → T201 → T202 → T203 → T301 → ...
