
# Enterprise AI Architecture — Academic Reference Collection

Comprehensive academic references for Enterprise AI systems, hybrid LLM architectures, RAG pipelines, inference optimization, Persian NLP, and autonomous AI workflows.

---

# Key Concepts

## Multi-Model Architecture
Using multiple specialized AI models together instead of relying on a single monolithic model.

### Academic Sources
- [Mixture of Experts Are Scalable Learners — Google Research](https://arxiv.org/abs/2112.06905)
- [Switch Transformers: Scaling to Trillion Parameter Models](https://arxiv.org/abs/2101.03961)
- [Outrageously Large Neural Networks: Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)

---

## Agentic Workflow
AI systems autonomously managing tasks, planning, reasoning, and tool usage.

### Academic Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)

---

## Cognitive Engine
AI systems capable of reasoning, memory management, planning, and decision-making.

### Academic Sources
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)
- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)

---

## Orchestrator
Central coordination layer managing multiple AI models and workflows.

### Academic Sources
- [TaskMatrix.AI: Completing Tasks by Connecting Foundation Models with Millions of APIs](https://arxiv.org/abs/2303.16434)
- [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends](https://arxiv.org/abs/2303.17580)

---

# Evolution of Enterprise AI

---

# Old Architecture

## Single Large Model
Using one giant model for all enterprise tasks.

### Academic Sources
- [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774)
- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)

---

## VRAM Bottleneck
GPU memory limitations in large-scale inference.

### Academic Sources
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054)
- [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473)

---

## High Latency
Slow inference caused by oversized models.

### Academic Sources
- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu)
- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)

---

## Hallucination
LLMs generating incorrect or fabricated information.

### Academic Sources
- [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629)
- [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958)

---

# Modern Hybrid Architecture

## Hybrid Pipeline
Combining multiple specialized AI subsystems.

### Academic Sources
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [RETRO: Improving Language Models by Retrieving from Trillions of Tokens](https://arxiv.org/abs/2112.04426)

---

## Specialized Models
Task-specific optimized AI models.

### Academic Sources
- [AdapterFusion: Non-Destructive Task Composition for Transfer Learning](https://arxiv.org/abs/2005.00247)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

---

## Distributed Processing
Distributing AI workloads across multiple nodes/models.

### Academic Sources
- [GPipe: Efficient Training of Giant Neural Networks](https://arxiv.org/abs/1811.06965)
- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)

---

# Model Zoo

---

# Dense Models

## Dense Architecture
All model parameters participate during inference.

### Academic Sources
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)

---

## Qwen Models
### Academic Sources
- [Qwen Technical Report](https://arxiv.org/abs/2309.16609)
- [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671)

---

## Llama Models
### Academic Sources
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
- [Llama 3 Model Card](https://arxiv.org/abs/2407.21783)

---

## Gemma Models
### Academic Sources
- [Gemma Technical Report](https://arxiv.org/abs/2403.08295)

---

## Phi Models
### Academic Sources
- [Phi-2: The surprising power of small language models](https://arxiv.org/abs/2402.17764)

---

# Mixture of Experts (MoE)

## MoE Architecture
### Academic Sources
- [Switch Transformers](https://arxiv.org/abs/2101.03961)
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088)

---

## DeepSeek
### Academic Sources
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

---

# Reasoning Models

## Deep Reasoning
### Academic Sources
- [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)
- [Program of Thoughts Prompting](https://arxiv.org/abs/2211.12588)

---

## Distillation
### Academic Sources
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)

---

# Vision-Language Models (VLM)

## Vision-Language Systems
### Academic Sources
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- [BLIP-2: Bootstrapping Language-Image Pre-training](https://arxiv.org/abs/2301.12597)

---

## Document Understanding
### Academic Sources
- [LayoutLM](https://arxiv.org/abs/1912.13318)
- [LayoutLMv3](https://arxiv.org/abs/2204.08387)

---

## Table Extraction
### Academic Sources
- [Table Transformer](https://arxiv.org/abs/2110.00061)

---

# AI Benchmarks

---

## MMLU
### Academic Sources
- [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)

---

## HellaSwag
### Academic Sources
- [HellaSwag](https://arxiv.org/abs/1905.07830)

---

## ARC-Challenge
### Academic Sources
- [Think you have Solved QA? Try ARC](https://arxiv.org/abs/1803.05457)

---

## HumanEval
### Academic Sources
- [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)

---

## GSM8K
### Academic Sources
- [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168)

---

## MATH
### Academic Sources
- [MATH Benchmark](https://arxiv.org/abs/2103.03874)

---

## BBH
### Academic Sources
- [Beyond the Imitation Game](https://arxiv.org/abs/2206.04615)

---

# Inference Optimization

---

## FlashAttention-2
### Academic Sources
- [FlashAttention-2](https://arxiv.org/abs/2307.08691)

---

## PagedAttention
### Academic Sources
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)

---

## Quantization
### Academic Sources
- [AWQ: Activation-aware Weight Quantization](https://arxiv.org/abs/2306.00978)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)

---

## Continuous Batching
### Academic Sources
- [Orca Distributed Serving System](https://www.usenix.org/conference/osdi22/presentation/yu)

---

# RAG Architecture

---

## Retrieval-Augmented Generation
### Academic Sources
- [RAG Original Paper](https://arxiv.org/abs/2005.11401)
- [RETRO](https://arxiv.org/abs/2112.04426)

---

## Semantic Retrieval
### Academic Sources
- [Sentence-BERT](https://arxiv.org/abs/1908.10084)
- [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)

---

## ColBERT
### Academic Sources
- [ColBERT](https://arxiv.org/abs/2004.12832)

---

## Vector Search
### Academic Sources
- [HNSW Graph Search](https://arxiv.org/abs/1603.09320)
- [FAISS Library](https://arxiv.org/abs/1702.08734)

---

# Persian NLP & OCR

---

## PersianQA
### Academic Sources
- [PersianQA Dataset](https://arxiv.org/abs/2109.06345)

---

## Persian Summarization
### Academic Sources
- [PN-Summary Dataset](https://arxiv.org/abs/2209.14969)

---

## PaddleOCR
### Academic Sources
- [PaddleOCR](https://arxiv.org/abs/2009.09941)

---

## Persian Handwriting Recognition
### Academic Sources
- [Offline Handwritten Persian Character Recognition](https://ieeexplore.ieee.org/document/8270148)

---

# Agentic Workflow

---

## ReAct Agents
### Academic Sources
- [ReAct](https://arxiv.org/abs/2210.03629)

---

## Tool Usage
### Academic Sources
- [Toolformer](https://arxiv.org/abs/2302.04761)

---

## Human-in-the-loop
### Academic Sources
- [Constitutional AI](https://arxiv.org/abs/2212.08073)

---

# Enterprise Security

---

## Prompt Injection
### Academic Sources
- [Prompt Injection Attacks and Defenses](https://arxiv.org/abs/2403.04957)

---

## Guardrails
### Academic Sources
- [NeMo Guardrails](https://arxiv.org/abs/2310.10501)

---

## AI Risk Management
### Academic Sources
- [NIST AI RMF PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

---

## OWASP LLM Security
### Academic Sources
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/)

---

# Infrastructure & GPU Scaling

---

## Megatron-LM
### Academic Sources
- [Megatron-LM](https://arxiv.org/abs/1909.08053)

---

## ZeRO
### Academic Sources
- [ZeRO Memory Optimization](https://arxiv.org/abs/1910.02054)

---

# Final Strategic Concepts

---

## Distributed AI
### Academic Sources
- [A Survey on Distributed AI](https://arxiv.org/abs/2402.09154)

---

## Autonomous Enterprise Systems
### Academic Sources
- [AutoGPT Research Overview](https://arxiv.org/abs/2308.11432)

---
