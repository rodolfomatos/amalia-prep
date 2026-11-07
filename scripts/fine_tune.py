#!/usr/bin/env python3
"""
Script de fine-tune QLoRA para o modelo Amália.

Treina o qwen3:8b nos datasets de abdução e saliência relacional.
Requer: peft, transformers, bitsandbytes, torch, datasets, accelerate
"""
import argparse
import json
import os
import sys
from pathlib import Path

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from bitsandbytes import __version__ as bnb_version
    from datasets import Dataset
except ImportError as e:
    print(f"Erro: dependência não encontrada: {e}")
    print("Instale com: pip install peft transformers bitsandbytes datasets accelerate")
    sys.exit(1)


def load_jsonl(path: str):
    """Carrega um arquivo JSONL como lista de dicionários."""
    examples = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                examples.append(json.loads(line))
    return examples


def format_abduction_example(example: dict) -> str:
    """Formata um exemplo de abdução para treino."""
    obs = example.get("observation", "")
    latent = example.get("ground_truth", {}).get("latent_variable", "")
    mechanism = example.get("ground_truth", {}).get("mechanism", "")
    return (
        f"### Observação: {obs}\n"
        f"### Contexto: {json.dumps(example.get('context', {}), ensure_ascii=False)}\n"
        f"### Tarefa: Adivinhe a variável latente escondida.\n"
        f"### Resposta: {latent}\n"
        f"### Mecanismo: {mechanism}\n"
    )


def format_salience_example(example: dict) -> str:
    """Formata um exemplo de saliência relacional para treino."""
    conteudo = example.get("conteudo", "")
    novidade = example.get("novidade_esperada", 0.5)
    ilhas = example.get("ilhas", [])
    ilhas_desc = "; ".join(
        f"{i.get('nome', '')}: {i.get('descricao', '')}" for i in ilhas[:5]
    )
    return (
        f"### Conteúdo: {conteudo}\n"
        f"### Ilhas: {ilhas_desc}\n"
        f"### Tarefa: Avalie a novidade relacional (0.0 a 1.0).\n"
        f"### Resposta: {novidade}\n"
    )


def prepare_dataset(abduction_path: str, salience_path: str) -> Dataset:
    """Prepara o dataset de treino combinando abdução e saliência."""
    abduction_examples = load_jsonl(abduction_path)
    salience_examples = load_jsonl(salience_path)

    texts = []
    for ex in abduction_examples:
        texts.append(format_abduction_example(ex))
    for ex in salience_examples:
        texts.append(format_salience_example(ex))

    return Dataset.from_list([{"text": t} for t in texts])


def tokenize_function(examples, tokenizer):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=512,
        return_tensors="pt"
    )


def main():
    parser = argparse.ArgumentParser(description="Fine-tune QLoRA para Amália")
    parser.add_argument("--base-model", required=True, help="Modelo base (ex: qwen3:8b)")
    parser.add_argument("--output-model", required=True, help="Nome do modelo de saída")
    parser.add_argument("--train-data", required=True, help="Arquivo JSONL de abdução")
    parser.add_argument("--salience-data", required=True, help="Arquivo JSONL de saliência")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--max-length", type=int, default=512)
    args = parser.parse_args()

    print(f"Carregando modelo base: {args.base_model}")
    print(f"Dataset de abdução: {args.train_data}")
    print(f"Dataset de saliência: {args.salience_data}")

    # Carregar datasets
    train_dataset = prepare_dataset(args.train_data, args.salience_data)
    print(f"Total de exemplos de treino: {len(train_dataset)}")

    # Carregar modelo e tokenizer
    print("Carregando modelo e tokenizer...")
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        load_in_4bit=True,
        device_map="auto",
        trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    # Preparar para k-bit training
    model = prepare_model_for_kbit_training(model)

    # Configurar LoRA
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Configurar treino
    training_args = TrainingArguments(
        output_dir=f"./models/{args.output_model}",
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=4,
        learning_rate=args.learning_rate,
        num_train_epochs=args.epochs,
        logging_steps=10,
        save_steps=50,
        fp16=True,
        report_to="none"
    )

    # Treinar
    from transformers import Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        tokenizer=tokenizer
    )
    trainer.train()

    # Salvar modelo
    print(f"Salvando modelo em ./models/{args.output_model}")
    model.save_pretrained(f"./models/{args.output_model}")
    tokenizer.save_pretrained(f"./models/{args.output_model}")
    print("Fine-tune concluído!")


if __name__ == "__main__":
    main()
