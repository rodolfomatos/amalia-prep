#!/usr/bin/env python3
"""
Gerador de dataset sintético de abdução para fine-tune do Amália.

Cada exemplo tem:
- observation: texto incompleto com uma variável latente escondida
- context: relações observadas (sem a variável latente)
- latent_variable: o significado escondido (alvo da abdução)
- mechanism: explicação causal que liga o contexto à latente

Formato: JSONL, uma linha por exemplo.
"""
import argparse
import json
import random
import sys
from pathlib import Path

# Categorias de variáveis latentes (espelhando o dataset do ACA)
LATENT_CATEGORIES = {
    "objeto_infancia": [
        "trenó da infância", "bola de gude", "avião de papel", "boneca velha",
        "caixa de música", "bicicleta pequena", "pipinha de pipoca"
    ],
    "pessoa_proibida": [
        "nome de um amante proibido", "amigo secreto", "vizinho misterioso",
        "professor desaparecido", "estranho na parada"
    ],
    "evento_trágico": [
        "hora de um acidente trágico", "momento da perda", "instante da doença",
        "dia do desastre natural", "noite do incêndio"
    ],
    "amor_proibido": [
        "um grande amor proibido", "caso amoroso secreto", "paixão impossível",
        "encontro às escondidas", "promessa não cumprida"
    ],
    "ausência": [
        "ausência do autor", "condição secreta violada", "acordo lateral secreto",
        "pedido de perdão não feito", "promessa quebrada"
    ]
}

RELATION_TEMPLATES = [
    "{sujeito} está relacionado a {objeto}",
    "{sujeito} ocorre antes de {objeto}",
    "{sujeito} explica {objeto}",
    "{sujeito} contrasta com {objeto}",
    "{sujeito} está em {objeto}",
    "{sujeito} causa {objeto}",
    "{sujeito} é parte de {objeto}"
]

OBSERVATION_TEMPLATES = [
    "Uma pessoa encontra um objeto misterioso e diz: '{palavra_chave}'. Não há contexto adicional.",
    "Em um momento de crise, alguém menciona '{palavra_chave}' sem explicar.",
    "O registro mostra apenas a palavra '{palavra_chave}' ligada a um evento passado.",
    "Alguém murmura '{palavra_chave}' antes de desaparecer. Nada mais é dito.",
    "O contexto contém apenas '{palavra_chave}' como pista isolada."
]


def generate_example(seed: int, category: str | None = None) -> dict:
    rng = random.Random(seed)
    if category is None:
        category = rng.choice(list(LATENT_CATEGORIES.keys()))
    latent = rng.choice(LATENT_CATEGORIES[category])
    palavra_chave = latent.split()[-1] if len(latent.split()) > 1 else latent

    # Gerar relações observadas (sem a variável latente completa)
    n_relations = rng.randint(2, 5)
    relations = []
    for _ in range(n_relations):
        subj = rng.choice([palavra_chave, "evento", "pessoa", "lugar", "tempo"])
        obj = rng.choice(["contexto", "passado", "memória", "sinal", "rastro"])
        template = rng.choice(RELATION_TEMPLATES)
        relations.append(template.format(sujeito=subj, objeto=obj))

    # Gerar mecanismo (explicação causal)
    mechanism = (
        f"A variável latente '{latent}' está escondida por trás das relações "
        f"observadas. As relações {', '.join(relations[:2])} sugerem que "
        f"{palavra_chave} é a chave para entender o fenômeno."
    )

    # Gerar observação (incompleta, sem a variável latente completa)
    observation = rng.choice(OBSERVATION_TEMPLATES).format(palavra_chave=palavra_chave)

    # Contexto (relações sem a latente completa)
    context = {
        "relations": relations,
        "key_concepts": [palavra_chave, "evento", "memória", "pista"]
    }

    return {
        "id": f"abduction_{seed:04d}",
        "category": category,
        "observation": observation,
        "latent_variable": latent,
        "context": context,
        "ground_truth": {
            "latent_variable": latent,
            "mechanism": mechanism
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Gerar dataset de abdução")
    parser.add_argument("--output", required=True, help="Caminho do arquivo JSONL de saída")
    parser.add_argument("--count", type=int, default=100, help="Número de exemplos")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    n_categories = len(LATENT_CATEGORIES)
    base, remainder = divmod(args.count, n_categories)
    ordered_cats = sorted(LATENT_CATEGORIES)
    # Distribui `args.count` igualmente pelas categorias; o resto (se houver)
    # vai para as primeiras categorias ordenadas.
    cat_counts = {
        cat: base + (1 if i < remainder else 0)
        for i, cat in enumerate(ordered_cats)
    }

    with open(output_path, "w", encoding="utf-8") as f:
        idx = 0
        for cat in ordered_cats:
            for _ in range(cat_counts[cat]):
                example = generate_example(idx, category=cat)
                f.write(json.dumps(example, ensure_ascii=False) + "\n")
                idx += 1

    print(f"Gerados {idx} exemplos em {output_path}")


if __name__ == "__main__":
    main()
