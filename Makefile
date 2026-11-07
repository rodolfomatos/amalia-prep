# Amália — Makefile de preparação de modelo
#
# Uso: make <target>
#
# Targets principais:
#   setup     - instalar dependências
#   data      - gerar datasets sintéticos de treino
#   train     - executar fine-tune (QLoRA)
#   eval      - rodar testes offline de abdução, saliência, repeat limit
#   push      - publicar modelo no Ollama local
#   check     - gate: lint + testes + critérios de aceitação
#   clean     - limpar artefatos gerados

PYTHON   ?= python3
PIP      ?= pip3
OLLAMA   ?= ollama
MODEL    ?= amalia
BASE     ?= qwen3:8b
DATA_DIR ?= data
SRC_DIR  ?= src
EVAL_DIR ?= eval

.PHONY: setup data train eval push check clean help lint

setup:
	@echo "=== Instalando dependências ==="
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "=== Verificando Ollama ==="
	@$(OLLAMA) list > /dev/null 2>&1 || (echo "Ollama não está rodando. Execute: ollama serve" && exit 1)
	@echo "✓ Setup completo"

data:
	@echo "=== Gerando datasets sintéticos ==="
	$(PYTHON) scripts/generate_abduction_data.py --output $(DATA_DIR)/abduction_training.jsonl --count 100
	$(PYTHON) scripts/generate_salience_data.py --output $(DATA_DIR)/salience_training.jsonl --count 50
	@echo "✓ Datasets gerados em $(DATA_DIR)/"

train:
	@echo "=== Executando fine-tune QLoRA ==="
	$(PYTHON) scripts/fine_tune.py \
		--base-model $(BASE) \
		--output-model $(MODEL) \
		--train-data $(DATA_DIR)/abduction_training.jsonl \
		--salience-data $(DATA_DIR)/salience_training.jsonl \
		--epochs 3 \
		--batch-size 4 \
		--learning-rate 2e-4
	@echo "=== Registrando no Ollama ==="
	$(OLLAMA) create $(MODEL) -f configs/Modelfile
	@echo "✓ Modelo $(MODEL) pronto no Ollama"

eval:
	@echo "=== Executando avaliação offline ==="
	$(PYTHON) -m pytest $(EVAL_DIR)/ -q -v
	@echo "✓ Avaliação completa"

push:
	@echo "=== Publicando modelo no Ollama ==="
	$(OLLAMA) cp $(MODEL) $(MODEL):latest
	@echo "✓ $(MODEL):latest disponível"

check: lint eval
	@echo "=== Verificando critérios de aceitação ==="
	$(PYTHON) scripts/check_acceptance.py
	@echo "✓ Todos os critérios de aceitação atendidos"

lint:
	@echo "=== Executando lint ==="
	$(PYTHON) -m ruff check $(SRC_DIR) $(EVAL_DIR) $(SCRIPTS_DIR) 2>/dev/null || \
		$(PIP) install ruff && $(PYTHON) -m ruff check $(SRC_DIR) $(EVAL_DIR) scripts/
	@echo "✓ Lint aprovado"

clean:
	rm -rf __pycache__ .pytest_cache $(SRC_DIR)/__pycache__ $(EVAL_DIR)/__pycache__ scripts/__pycache__
	find . -name "*.pyc" -delete
	@echo "✓ Limpeza completa"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Default target
.DEFAULT_GOAL := help
