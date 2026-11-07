# Amália — Preparação de Modelo para o Projeto ACA

Contrato operacional para o projeto de preparação do modelo `amalia`, destinado a ser usado como LLM de base no projeto Artificial Creativity Architecture (ACA).

---

## Intent

Trepar/ajustar um modelo de linguagem (base: `qwen3:8b` via Ollama) para as tarefas específicas do ACA:

1. **Abdução** — gerar mecanismos causais focados na variável latente, não explicações filosóficas abstratas
2. **Saliência relacional** — ranquear conexões entre ilhas por densidade relacional, não só sobreposição léxica
3. **Reconstrução de variável latente** — adivinhar o significado escondido a partir de observações incompletas

O objetivo é substituir o `qwen3:8b` cru pelo `amalia` no ACA, resolvendo dois problemas identificados:
- **Token repeat limit** no `cost_ensation` do ITERReasoner (bloqueia H2)
- **Saída verbosa** que destrói o overlap léxico com `ground_truth.latent_variable` (bloqueia H6)

---

## Não-objetivos

- Não treinar do zero (muito caro, não necessário)
- Não criar um modelo geral-purpose (especializar para as tarefas do ACA)
- Não depender de APIs externas pagas (usar Ollama local na GPU existente)

---

## Comandos

```bash
make setup          # instalar dependências
make data           # gerar datasets sintéticos de treino
make train          # executar fine-tune (LoRA/QLoRA)
make eval           # rodar testes offline de abdução, saliência, reconstrução
make push           # publicar modelo no Ollama local
make check          # gate: lint + testes + critérios de aceitação
```

---

## Critérios de aceitação (antes de integrar ao ACA)

| Critério | Alvo | Como medir |
|----------|------|------------|
| Latência < 3s | < 3s por chamada | `time ollama run amalia "prompt"` |
| Sem repeat limit | 0 falhas em 100 calls | Rodar ITERReasoner completo 100x |
| Acurácia abdução > 0.3 | > 30% de reconstrução correta | `run_t603_h6.py` com amalia |
| Novidade relacional | Diferencia ilhas conectadas vs isoladas | `eval/test_novidade_relacional.py` |
| Saída curta | < 200 tokens por resposta média | Medir tokens de saída |

---

## Protocol

Seguir o protocolo AES (Ambrósio Engineering System):
- Toda afirmação é falsificável com `falsified_if` e `decided_by`
- Nenhuma hipótese sai de `NÃO-VERIFICÁVEL` sem N≥5 seeds e confidence intervals
- Não usar yes-men; challenge decisões de arquitetura

---

## Arquivos críticos

| Ficheiro | Porquê |
|----------|--------|
| `CLAUDE.md` | Este contrato operacional |
| `PLAN.md` | Marcos, tickets, restrições de ordenação |
| `docs/ADR-001-amalia-base.md` | Decisão de usar qwen3:8b como base |
| `docs/ADR-002-finetune-method.md` | Decisão de LoRA vs QLoRA vs full fine-tune |
| `data/abduction_training.jsonl` | Dataset de treino para abdução |
| `data/salience_training.jsonl` | Dataset de treino para saliência |
| `eval/test_abduction.py` | Testes de abdução offline |
| `eval/test_salience.py` | Testes de saliência relacional offline |

---

## Nunca fazer

- Não usar dados de produção do ACA para treino sem anonimização
- Não declarar o modelo "pronto" sem passar nos critérios de aceitação
- Não fazer merge sem `make check` verde e aprovação humana
