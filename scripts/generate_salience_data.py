#!/usr/bin/env python3
"""
Gerador de dataset sintético de saliência relacional para fine-tune do Amália.

Cada exemplo tem:
- ilhas: lista de ilhas com nome, descrição e relações
- conteudo: conteúdo a ser avaliado
- novidade_esperada: score de novidade (0.0 a 1.0)
- relacoes: lista de relações entre ilhas

Formato: JSONL, uma linha por exemplo.
"""
import argparse
import json
import random
from pathlib import Path

RELATION_TYPES = ["RELATED_TO", "CONTRADIZ", "COMPLEMENTA", "DERIVA_DE", "AGREGADO_EM"]

ISLAND_NAMES = [
    "Ilha da Memória", "Ilha do Esquecimento", "Ilha dos Símbolos",
    "Ilha dos Acidentes", "Ilha dos Amores", "Ilha das Ausências",
    "Ilha dos Desastres", "Ilha dos Protetores", "Ilha dos Líderes",
    "Ilha dos Ancestrais"
]


def generate_example(seed: int) -> dict:
    rng = random.Random(seed + 1000)
    n_islands = rng.randint(3, 8)
    islands = []

    for i in range(n_islands):
        name = f"{rng.choice(ISLAND_NAMES)} {i}"
        desc = rng.choice([
            "uma ilha misteriosa com relações complexas",
            "um local isolado com poucas conexões",
            "um ponto central de muitas relações",
            "um lugar de transição entre domínios",
            "um arquivo de eventos passados"
        ])
        relations = []
        for _ in range(rng.randint(0, 4)):
            target = rng.choice([n for n in ISLAND_NAMES if n != name])
            rel_type = rng.choice(RELATION_TYPES)
            relations.append({
                "ilha_id": target,
                "tipo": rel_type,
                "forca": round(rng.uniform(0.1, 1.0), 2)
            })
        islands.append({
            "id": f"ILHA-{i:03d}",
            "nome": name,
            "descricao": desc,
            "relacoes": relations
        })

    # Gerar conteúdo a ser avaliado
    conteudo = rng.choice([
        "símbolo de proteção ancestral",
        "evento trágico não resolvido",
        "amor proibido entre domínios",
        "ausência de autor conhecido",
        "acordo lateral secreto"
    ])

    # Calcular novidade relacional esperada
    total_relations = sum(len(i["relacoes"]) for i in islands)
    n_relation_types = len(set(r["tipo"] for i in islands for r in i["relacoes"]))
    connected_islands = sum(1 for i in islands if len(i["relacoes"]) > 0)

    if connected_islands == 0:
        novidade = 0.9  # Isolado = muito novo
    else:
        densidade = min(1.0, connected_islands / len(islands))
        diversidade = min(1.0, n_relation_types / len(RELATION_TYPES))
        novidade = max(0.0, min(1.0, 1.0 - (0.6 * densidade + 0.4 * diversidade)))

    return {
        "id": f"salience_{seed:04d}",
        "conteudo": conteudo,
        "ilhas": islands,
        "novidade_esperada": round(novidade, 2),
        "total_relacoes": total_relations,
        "tipos_relacao": n_relation_types,
        "ilhas_conectadas": connected_islands
    }


def main():
    parser = argparse.ArgumentParser(description="Gerar dataset de saliência relacional")
    parser.add_argument("--output", required=True, help="Caminho do arquivo JSONL de saída")
    parser.add_argument("--count", type=int, default=50, help="Número de exemplos")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for i in range(args.count):
            example = generate_example(i)
            f.write(json.dumps(example, ensure_ascii=False) + "\n")

    print(f"Gerados {args.count} exemplos em {output_path}")


if __name__ == "__main__":
    main()
