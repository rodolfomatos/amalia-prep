# Amália — Preparação de Modelo para o ACA

Projeto separado para preparar um modelo de linguagem (`amalia`) específico para as tarefas do Artificial Creativity Architecture (ACA).

## Estrutura

```
amalia-prep/
├── CLAUDE.md          # Contrato operacional (protocolo AES)
├── PLAN.md            # Plano com marcos e tickets
├── Makefile           # Comandos: setup, data, train, eval, push, check
├── requirements.txt   # Dependências Python
├── configs/           # Configurações (Modelfile do Ollama)
├── docs/              # ADRs e documentação
├── src/               # Código-fonte (se houver)
├── scripts/           # Scripts de geração, treino, verificação
├── data/              # Datasets sintéticos (JSONL)
├── eval/              # Testes de avaliação (pytest)
├── tests/             # Testes unitários
└── models/            # Modelos treinados (output)
```

## Fluxo de trabalho

```bash
# 1. Configurar ambiente
make setup

# 2. Gerar datasets sintéticos
make data

# 3. Executar fine-tune QLoRA
make train

# 4. Avaliar contra critérios de aceitação
make eval

# 5. Verificar se tudo está ok
make check

# 6. Publicar no Ollama local
make push
```

## Critérios de aceitação

| Critério | Alvo |
|----------|------|
| Latência | < 3s por chamada |
| Repeat limit | 0 falhas em 100 chamadas |
| Acurácia abdução | > 0.3 |
| Acurácia saliência | > 0.5 |
| Saída curta | < 200 tokens/média |

## Integração com o ACA

Quando o modelo estiver pronto:

```bash
# No repositório do ACA
export ACA_LLM_MODEL="ollama/amalia"
python scripts/run_t603_h6.py --seeds 5 --items 20  # H6
python scripts/run_t305_h2.py --seeds 5 --items 20  # H2
python scripts/run_m9_h3_h8.py --seeds 5 --items 20 # H3/H8
```

## Licença

Próprio — para uso no projeto ACA.
