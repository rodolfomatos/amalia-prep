# ADR-001: Modelo base para o Amália

## Status

Aceito

## Contexto

O projeto ACA precisa de um modelo de linguagem para substituir o `qwen3:8b` cru, que tem duas limitações:

1. **Token repeat limit** no `cost_ensation` do ITERReasoner (bloqueia H2)
2. **Saída verbosa com chain-of-thought** que destrói o overlap léxico com `ground_truth.latent_variable` (bloqueia H6)

O modelo base deve ser:
- Disponível localmente (Ollama)
- Rápido (< 3s por chamada na RTX 5090)
- Pequeno o suficiente para fine-tune com recursos limitados
- Capaz de seguir instruções de formato JSON estrito

## Decisão

Usar `qwen3:8b` como modelo base para o Amália.

## Justificativa

- Já está instalado e rodando no Ollama local
- 8B parâmetros cabe na VRAM da RTX 5090 com QLoRA
- Bom desempenho em instruções em português
- Já validado como funcional (embora com limitações)

## Alternativas consideradas

| Modelo | Prós | Contras |
|--------|------|---------|
| qwen3:8b | Já instalado, bom português | Limitado (ver acima) |
| llama3.1:8b | Boa qualidade geral | Não instalado, precisaria baixar |
| mistral:7b | Rápido, leve | Menor qualidade em português |
| qwen2.5:32b | Melhor qualidade | Muito grande para fine-tune rápido |

## Consequências

- Herdamos as limitações do qwen3:8b (saída verbosa, chain-of-thought)
- O fine-tune deve focar em fazer o modelo ignorar o chain-of-thought e responder direto
- Se o fine-tune não funcionar, considerar mudar para outro modelo base
