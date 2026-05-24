# Full Fine-tuning (FFT) 
 Updating all model weights during training.

## Key Concepts
- `Parameter`: Internal model weights.
- `Backpropagation`: Updating weights using errors.
- `Weight Update`: Changing model parameters during training.
- `VRAM`: GPU memory used for training.
- `Optimizer State`: Extra optimizer memory data.

## Advantages
- `Deep Knowledge Injection`: Learning completely new domains.
- `Maximum Performance`: Best accuracy for complex tasks.
- `Zero Inference Overhead`: No extra latency after training.

## Limitations
- `Catastrophic Forgetting`: Losing previous knowledge.
- `Resource Intensity`: Requires powerful GPUs.
- `Overfitting`: Memorizing small datasets.

# LoRA (Low-Rank Adaptation)
Lightweight fine-tuning using small trainable matrices.

## Key Concepts
- `Low-Rank`: Low-dimensional weight changes.
- `Matrix Decomposition`: Splitting large matrices into smaller ones.
- `Rank (r)`: Size of LoRA matrices.
- `Matrix A`: First trainable matrix.
- `Matrix B`: Second trainable matrix.
- `ΔW = B × A`: Main LoRA formula.

## Advantages
- `Low Memory Usage`: Much lower VRAM consumption.
- `Zero Inference Overhead`: No speed reduction after merge.
- `Adapter Switching`: Fast switching between adapters.

# QLoRA
Quantized LoRA using 4-bit compressed base models.

## Key Concepts
- `Quantization`: Compressing model weights.
- `4-bit Quantization`: Using only 4 bits per weight.
- `NF4`: Special 4-bit datatype for LLMs.
- `Double Quantization`: Compressing quantization values again.
- `Paged Optimizers`: Temporarily moving memory to RAM.
- `De-quantization`: Restoring precision during computation.

## Advantages
- `Low VRAM Usage`: Training large models on consumer GPUs.
- `High Accuracy`: Very small quality loss.
- `Lower Cost`: Cheaper hardware requirements.

# Behavioral Dataset Design — Teaching behavior, safety, and interaction style.

## Key Concepts
- `Alignment`: Matching model behavior with human goals.
- `Preference Dataset`: Dataset with preferred answers.
- `Persona`: Behavioral personality of the model.
- `Red Teaming`: Stress-testing model safety.

## Methods
- `RLAIF`: AI-generated feedback instead of human feedback.
- `Constitutional AI`: Training with predefined behavior rules.
- `UltraFeedback`: Ranking multiple generated outputs.
- `STaR`: Training self-correction ability.
- `SPiN`: Training using self-play conversations.

# Adapter Training
Methods for training LoRA-style adapters.

## Methods
- `PEFT`: Parameter-Efficient Fine-Tuning.
- `DPO`: Direct optimization from preferences.
- `Preference Loss`: Increasing preferred-answer probability.
- `NEFTune`: Adding noise to embeddings.
- `Random Noise`: Small perturbations for generalization.
- `DoRA`: Separating weight magnitude and direction.
- `Magnitude`: Size of weights.
- `Direction`: Orientation of weights.

# Model Evaluation Metrics
Measuring reasoning and behavior quality.


## Metrics
- `Reasoning Consistency`: Logical stability during reasoning.
- `Executive Communication`: Clear and structured reporting.
- `Uncertainty Handling`: Correctly expressing uncertainty.
- `Structured Analysis`: Breaking problems into logical parts.
- `Hallucination`: Producing false but believable outputs.
- `Chain of Thought (CoT)`: Step-by-step reasoning process.
