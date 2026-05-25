## LLM naming conventions

Name & Version ( Claude-3 / GPT-4o / Phi-3)

Parameter Count ( 7B / 13B / 35B / 70B )

Active Params (MoE) ( A2B /  A3B / A6B / 8x7B / 16x3B)

Context Length ( 4K / 8K / 128K )

Floating Point Precision ( FP32 / FP16 / BF16 )

Quantization ( Q4 / Q5 / Q8 )

Instruction Tuning ( Instruct / Chat / Base / SFT / RLHF / DPO / IT / Dialogue / Assistant / Reasoning / Reasoner)

Multimodal (VL / VLM / MM / Vision / Vision-Language / Image-Text / Image-to-Text / OCR / Grounding)

Format ( GGUF / Safetensors / PyTorch / Checkpoint / ONNX )

Distilled (KD / Distill / Student / Teacher-Student / Small / Compressed)

## Instruction Tuning
| Tag | Abbreviation | Simple Meaning |
|-----|-------------|----------------|
| Base | Base | Raw model, only predicts next text, not instruction-following |
| Instruct | Instruct | Trained to follow human instructions (Q&A, tasks) |
| Chat | Chat | Optimized for conversation and dialogue behavior |
| SFT | Supervised Fine-Tuning | Trained on labeled instruction-response data |
| RLHF | Reinforcement Learning from Human Feedback | Improved using human preference feedback |
| DPO | Direct Preference Optimization | Alignment method using preference data, simpler than RLHF |
| IT | Instruction Tuning | General term for training model to follow instructions |
| Dialogue | Dialogue | Focused on multi-turn conversations |
| Assistant | Assistant | Optimized as a helpful task-solving assistant |
| Reasoning | Reasoning | Enhanced for multi-step logical problem solving |
| Reasoner | Reasoner | Specialized model for deeper and harder reasoning tasks |
