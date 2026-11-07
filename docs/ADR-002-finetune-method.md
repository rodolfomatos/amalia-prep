# ADR-002: Método de fine-tune (QLoRA)

## Status

Aceito

## Contexto

Precisamos ajustar o qwen3:8b para as tarefas específicas do ACA (abdução, saliência relacional, reconstrução de variável latente). As opções são:

1. **Full fine-tune** — treinar todos os parâmetros
2. **LoRA** — treinar apenas camadas de baixa ordem
3. **QLoRA** — LoRA com quantização de 4 bits

## Decisão

Usar QLoRA (quantização de 4 bits + LoRA).

## Justificativa

- **VRAM limitada**: RTX 5090 tem 32 GB, full fine-tune de 8B não cabe
- **Velocidade**: QLoRA é mais rápido que LoRA completo
- **Qualidade**: Estudos mostram que QLoRA preserva quase toda a qualidade do full fine-tune
- **Ecossistema**: `peft` + `bitsandbytes` são maduros e bem documentados

## Parâmetros

| Parâmetro | Valor |
|-----------|-------|
| r (rank) | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| target_modules | q_proj, v_proj, k_proj, o_proj |
| bias | none |
| task_type | CAUSAL_LM |
| Epochs | 3 |
| Batch size | 4 |
| Learning rate | 2e-4 |
| Max length | 512 |

## Consequências

- O modelo base permanece inalterado (apenas adaptadores LoRA são salvos)
- Pode fazer merge dos adaptadores com o modelo base para criar um modelo Ollama nativo
- Requantização de 4 bits pode perder alguma precisão, mas é aceitável para este uso
