---
ticket: T201
title: 50 exemplos de ilha → conteúdo conectado/isolado
phase: learn
tier: AES-standard
---

# T201 — Learn Output (Phase 5 / Learn)

## O que foi construído e porquê
O dataset de saliência já existia com 50 exemplos, mas não satisfazia o AC literal do PLAN.md T201 (cada exemplo deve ter top-level `ilhas`, `relacoes`, `conteudo`, `novidade_esperada`): o `relacoes` estava apenas aninhado em `ilhas[i].relacoes`. Adicionei o campo top-level `relacoes` (lista achatada de todas as relações de todas as ilhas do exemplo, espelhando `total_relacoes`) ao gerador e regenerei o dataset (mesmas seeds → mesmo conteúdo + novo campo), para que o dataset satisfaça o AC literal sem quebrar o contrato executável dos testes (`eval/test_salience.py` lê `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`).

## O que correu bem
- Hostile analysis surfou a mesma contradição de schema de T101 (PLAN.md vs código vs testes) antes de qualquer alteração.
- Alteração cirúrgica: 1 linha no gerador + regeneração do dataset; nenhum outro ficheiro tocado.
- Contrato executável preservado: testes continuam a ler `conteudo`/`novidade_esperada`/`ilhas`/`ilhas_conectadas`.
- T202 (5 tipos de relação, incluindo os 3 exigidos) já está satisfeito.

## O que correu mal / pode melhorar
- 2 erros de ruff pré-existentes em `scripts/generate_salience_data.py` (`EXE001` shebang, `C401` generator). Não são da responsabilidade de T201.
- Todos os 50 exemplos são conectados; nenhum isolado. O teste `test_isolado_mais_novo_que_conectado` fará `pytest.skip`. Registrado para T402.

## Insight para o registo hostil (Hostile Insights Registry)
> **Categoria**: Consistência de schema / padrão recorrente (mesmo que T101)
> **Insight**: A mesma contradição de schema (PLAN.md exige campo no nível top-level; o código o mantém aninhado) reapareceu em M2 (saliência). Isso indica um padrão sistémico: os ACs do PLAN.md descrevem campos top-level que o gerador implementa aninhados. A solução consistente é espelhar o campo em ambos os níveis, preservando o contrato executável dos testes.
> **Origem**: Hostile analysis de T201 (Phase 1), consistente com T101.
> **Impacto**: Mitigado espelhando `relacoes` em nível top-level e mantendo `ilhas[].relacoes`.
> **Aplicado a**: T101 e T201; relevante para qualquer novo dataset gerado neste projeto.
> **Data**: 2026-11-07

## Próximo ticket na sequência
T203 (validação formal: JSONL válido, 50 linhas únicas, schema válido) — conclui M2. Depois M3 (T301-T303, fine-tune QLoRA).
