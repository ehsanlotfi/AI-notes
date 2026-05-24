# Knowledge Distillation for Lightweight Models

## Overview
Knowledge Distillation is a model compression technique where a large model (Teacher) transfers knowledge to a smaller model (Student).  
Goal: reduce size, improve speed, and maintain accuracy.

**2025–2026 State-of-the-Art**: focuses on:
- **Reasoning Distillation**: Transferring **Chain-of-Thought (CoT)** and **step-by-step logic** from large reasoning models (e.g., DeepSeek-R1) to smaller models.
- **On-Policy Distillation**: Student models generate their own training samples (on-policy), which are then refined by the Teacher.
- **Safety-Aligned Distillation**: Preserving **alignment and safety guardrails** during transfer (a major challenge as of 2026).
- **Diffusion Model Distillation**: Compressing **text-to-image diffusion models** (e.g., SDXL → SDXL-Turbo) via one-step or few-step distillation.


## Motivation
- Large models are accurate but slow and expensive
- Real-world systems need:
  - Low latency
  - Low memory usage
  - Energy efficiency

##  Core Idea (Teacher–Student Framework)
1. **Teacher Model**: Large, pre-trained, high-accuracy (e.g., Llama-3.1, GPT-4o).
2. **Student Model**: Small, efficient architecture (e.g., Llama-3.2-1B, MobileViT, TinyBERT).
3. **Knowledge Transfer**: Student learns from:
   - **Hard Labels** (The exact correct answers in the training data. e.g. Cat = 1, Dog = 0).
   - **Soft Labels** (Teacher's output distribution. e.g. Cat = 0.82, Dog = 0.14).
   - **Intermediate Features** (hidden states, attention maps).
   - **Reasoning Trajectories** (CoT steps, tool-use traces).

##  Basic Distillation Process
1. **Train/Obtain Teacher**: Use a pre-trained high-capacity model.
2. **Generate Soft Targets**: Run data through Teacher with **temperature scaling** (`T > 1`) to get softened probabilities.
3. **Train Student**: Minimize a **combined loss**:
   - **Hard Loss** (`L_hard`): Cross-entropy with true labels.
   - **Soft Loss** (`L_soft`): KL-divergence or other metric between Student and Teacher outputs.
4. **(Optional) Feature Distillation**: Align intermediate representations via MSE, cosine similarity, or attention transfer.


##  Loss Function
### Standard Form:
- `L_hard`: Cross-entropy with true labels
- `L_soft`: Difference between Teacher and Student outputs
- `α`: balance factor

### Modern Variants (2024–2026):
- **Wasserstein Distillation**: Uses **Wasserstein distance** instead of KL-divergence for more stable training ([Lv et al., 2024](https://arxiv.org/abs/2412.08139)).
- **Logit Standardization**: Normalizes logits across classes to improve stability ([Sun et al., CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Sun_Logit_Standardization_in_Knowledge_Distillation_CVPR_2024_paper.html)).
- **Orthogonal Projection (VkD)**: Projects student features to a subspace orthogonal to teacher's redundant directions ([Miles et al., CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Miles_VkD_Improving_Knowledge_Distillation_using_Orthogonal_Projections_CVPR_2024_paper.pdf)).

### **Reasoning Distillation (2025+)**
Transfer of **cognitive processes** (e.g., CoT, tool-use, self-reflection) from large reasoning models (LRMs) like **DeepSeek-R1**, **o1-preview**.  
- **How**: Teacher generates **intermediate reasoning steps**; Student learns to mimic the **trajectory**, not just the final answer.

### **Safety-Aligned Distillation**
Preserving **ethical guardrails and bias mitigations** during transfer.  
**2026 Finding**: ["To Distill or Not to Distill"](https://openreview.net/pdf/fed763a30898a94daf0c79a480b698875f2cf105.pdf) shows KD can **undermine safety** if Teacher's safety signals are not explicitly distilled.

### **On-Policy vs. Off-Policy**
- **Off-Policy** (Classic): Teacher fixed; Student learns from Teacher's *static* outputs.
- **On-Policy** (2026): Student **generates its own samples** (e.g., via sampling), Teacher **corrects** them. More sample-efficient but unstable.

##  Types of Knowledge Distillation (2026 Taxonomy)

| Category | Subtype | Description | Key Papers (2024–2026) |
|----------|---------|-------------|------------------------|
| **Response-based** | Logits/Output KD | Match final output distributions. | Classic (Hinton 2015), [Wasserstein KD](https://arxiv.org/abs/2412.08139) (2024) |
| **Feature-based** | Intermediate-layer KD | Align hidden states, attention maps. | [CRD](https://arxiv.org/pdf/1910.10699.pdf) (2019), [SemCKD](https://arxiv.org/abs/2012.03236) (2020) |
| **Relation-based** | Instance/Graph Relation | Model relationships between samples (e.g., pairwise similarities). | [RKD](https://arxiv.org/abs/1904.05068) (2019), [IRG](http://openaccess.thecvf.com/content_CVPR_2019/papers/Liu_Knowledge_Distillation_via_Instance_Relationship_Graph_CVPR_2019_paper.pdf) (2019) |
| **On-Policy Distillation** | Self-generated data | Student generates its own training samples (e.g., via sampling), Teacher provides feedback. | [Relaxed On-Policy Distillation](https://arxiv.org/abs/2603.11137) (2026) |
| **Reasoning Distillation** | CoT/Process-based | Transfer **step-by-step reasoning** (not just final answer). | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) (2025), [MaKD](https://arxiv.org/pdf/2501.13341) (2025) |
| **Self-Distillation** | Born-Again, Self-Training | Same model teaches itself across epochs/layers. | [Born-Again NNs](https://arxiv.org/abs/1805.04770) (2018), [Self-KD](https://arxiv.org/abs/1905.08094) (2019) |
| **Data-Free KD** | No original data needed | Generate synthetic data (e.g., via GANs, DeepInversion). | [DeepInversion](https://arxiv.org/abs/1912.08795) (2020), [EchoDFKD](https://arxiv.org/abs/2409.07566) (2025) |
| **Multi-Teacher** | Ensemble of Teachers | Combine knowledge from multiple specialized teachers. | [Ensemble Distribution Distillation](https://arxiv.org/abs/1905.00076) (2019) |


##  Model Families Using Distillation

| Domain | Teacher Models | Distilled Students | Notable Works |
|--------|---------------|-------------------|---------------|
| **NLP** | BERT-large, Llama-3-405B, GPT-4 | DistilBERT, TinyBERT, **Llama-3.2-1B**, **Phi-3.5-Mini**, **DeepSeek-R1-Distill-Qwen-7B** | [TinyBERT](https://arxiv.org/pdf/1909.10351.pdf) (2019), [DeepSeek-R1](https://arxiv.org/abs/2501.12948) (2025) |
| **Vision** | ViT-Huge, ConvNeXt-XXL | MobileViT, **MobileSAMv2**, **SDXL-Turbo** | [MobileSAMv2](https://arxiv.org/abs/2312.09579) (2023), [SDXL-Turbo](https://arxiv.org/abs/2311.18828) (2023) |
| **Multimodal** | LLaVA, GPT-4V | **TinyLLaVA**, **MobileCLIP** | [Knowledge Transfer from Vision Foundation Models](https://arxiv.org/abs/2311.18237) (2023) |
| **Diffusion** | Stable Diffusion XL, Imagen | **SDXL-Turbo**, **LCM-LoRA**, **ARD** (Autoregressive Distillation) | [Progressive Distillation](https://arxiv.org/abs/2202.00512) (2022), [ARD](https://arxiv.org/abs/2504.11295) (2025) |


##  Popular Distilled Models (2025–2026)

| Model | Size | Teacher | Distillation Type | Notes |
|-------|------|---------|-------------------|-------|
| **DeepSeek-R1-Distill** | 7B/14B | DeepSeek-R1 | **Reasoning (CoT) Distillation** | First major LRM → smaller model distillation. |
| **Llama-3.2-1B/3B** | 1B/3B | Llama-3.1-405B | Response + Feature KD | Optimized for edge devices. |
| **Phi-3.5-Mini** | 3.8B | Unspecified large model | Web-data + synthetic KD | Microsoft's efficient small model. |
| **SDXL-Turbo** | ~2B params (UNet) | SDXL | **One-step Diffusion Distillation** | Real-time text-to-image (1–4 steps). |
| **MobileSAMv2** | ~8M params | SAM-Huge | Feature + Response KD | Segment Anything in real-time on mobile. |
| **TinyBERT-6L** | 14.5M | BERT-base | Layer-wise KD | 7.5× smaller, 9× faster. |


##  Applications

- **Mobile AI**: On-device translation, assistants (e.g., Samsung Bixby, Google Assistant).
- **Edge Computing**: IoT sensors, drones, robots (e.g., NVIDIA Jetson, Raspberry Pi).
- **Autonomous Vehicles**: Real-time perception (object detection, segmentation) via distilled vision models.
- **Recommendation Systems**: Distilled two-tower models for faster retrieval.
- **Real-Time NLP**: Chatbots, code completion, search engines.
- **Diffusion Models**: Real-time image/video generation on consumer GPUs.

##  Advantages

1. **Size Reduction**: 2–10× fewer parameters.
2. **Speedup**: 2–15× faster inference (measured in **tokens/sec** or **FPS**).
3. **Memory Efficiency**: Lower VRAM/RAM usage (critical for edge).
4. **Energy Savings**: 50–80% less power consumption.
5. **Cost Reduction**: Cheaper cloud inference (e.g., 70% lower AWS/GCP costs).
6. **Accuracy Retention**: Often within **1–2%** of Teacher on benchmark datasets.

##  Limitations & Challenges (2026 Focus)

1. **Capacity Gap**: Student may lack capacity to mimic Teacher's complex logic → **"dark knowledge" loss**.
2. **Safety Alignment Erosion**: KD can **bypass safety training** if not explicitly aligned ([2026 Safety Paper](https://openreview.net/pdf/fed763a30898a94daf0c79a480b698875f2cf105.pdf)).
3. **Reasoning Distillation Difficulty**: CoT distillation requires **high-quality, diverse reasoning traces**; prone to **error propagation**.
4. **Hyperparameter Sensitivity**: `T`, `α`, learning rate, and **distillation schedule** require extensive tuning.
5. **Compute Cost**: Teacher inference + Student training still **expensive** (though less than pre-training from scratch).
6. **Data-Free Distillation**: Synthetic data quality limits Student performance.

##  Comparison with Other Compression Techniques

| Technique | Mechanism | Compression Ratio | Speedup | Accuracy Drop | Combo with KD? |
|-----------|-----------|-------------------|---------|---------------|----------------|
| **Knowledge Distillation** | Transfer soft knowledge | 2–10× | 2–15× | Low (1–3%) | ✅ **Yes** (often combined) |
| **Quantization** | Reduce bit precision (FP32 → INT8/INT4) | 4× (INT8) | 2–4× | Very Low (≤1%) | ✅ **Yes** (KD + Quant) |
| **Pruning** | Remove redundant weights/neurons | 2–5× | 1.5–3× | Medium (2–5%) | ✅ **Yes** (KD after pruning) |
| **LoRA/QLoRA** | Low-rank adaptation (not compression) | None | None | Minimal | ❌ No (fine-tuning only) |
| **Architecture Search** | Design efficient architectures (e.g., NAS) | 2–3× | 2–3× | Low | ✅ **Yes** (NAS + KD) |

**Best Practice (2026)**: **KD → Pruning → Quantization** pipeline for maximum compression.

##  Evaluation Metrics

| Metric | Description | Target for Distilled Models |
|--------|-------------|----------------------------|
| **Accuracy** | Top-1/Top-5 on benchmark (e.g., ImageNet, GLUE) | Within **1–2%** of Teacher |
| **Inference Latency** | ms per sample (or tokens/sec) | **2–10× faster** than Teacher |
| **Model Size** | Parameters (M/B) or disk size (MB/GB) | **2–10× smaller** |
| **Memory Footprint** | VRAM/RAM usage during inference | **2–5× less** |
| **Energy Efficiency** | Joules/sample or FPS/Watt | **2–4× more efficient** |
| **Throughput** | Samples/sec in batch mode | **2–15× higher** |
| **Safety Score** | (2026) Alignment, refusal rate, bias metrics | **Preserved** (not degraded) |


##  Industry Use Cases

- **OpenAI**: Distills GPT-4 → **GPT-4o Mini** (rumored).
- **Google**: Distills PaLM 2 → **PaLM 2-Gecko** (on-device).
- **Meta**: Distills Llama → **Llama-3.2** for mobile.
- **Microsoft**: **Phi** series (data + KD).
- **Hugging Face**: **Distilabel** pipeline for LLM distillation.
- **Apple**: On-device distilled models for Siri, image recognition.
- **Tesla**: Distilled vision models for FSD computer.

##  Future Directions (2026+)

1. **Reasoning Distillation at Scale**: Distilling **multi-step reasoning** from o1-class models to <10B parameter models.
2. **Cross-Modal Distillation**: Using **LLM reasoning** to guide vision model training (e.g., "Why" behind image classification).
3. **On-Device Continuous Distillation**: Models that **self-improve** via user interaction (federated KD).
4. **Uncertainty-Aware Distillation**: Transferring **calibrated uncertainty estimates** (critical for robotics/medical).
5. **Multimodal KD**: Distilling **LLaVA**-style models into **tiny multimodal** agents.
6. **Efficient Teacher Design**: Training **"distillable" teachers** from scratch (not just using giant pre-trained models).
7. **Causal Distillation**: Transferring **causal mechanisms** rather than correlations ([Wu et al., 2021](https://arxiv.org/abs/2112.02505)).
8. **Dataset Distillation**: Synthesizing **training data** that maximizes KD efficiency (emerging with LLMs).

## Recent Trends & Statistics (2025–2026)

| Trend | Description | Impact |
|-------|-------------|--------|
| **Reasoning Distillation** | Transferring CoT from LRMs (DeepSeek-R1, o1) | Enables **7B models** to achieve **70B+ reasoning** performance. |
| **On-Policy KD** | Student generates its own training data | **Reduces teacher dependency**; more sample-efficient. |
| **Safety-Preserving KD** | Explicitly distilling refusal, harmlessness | **Critical for production**; 2026 papers show **failure modes**. |
| **Diffusion → AR Distillation** | Turning diffusion models into fast autoregressive decoders | **Real-time image generation** (SDXL-Turbo, ARD). |
| **Data-Free KD** | No original training data needed | **Privacy-preserving**; useful for regulated industries. |
| **Multi-Teacher Distillation** | Combining coding, math, vision specialists | **Multi-skilled small models** (e.g., **Phi-3.5-Vision**). |


##  Practical Tips for Implementation

1. **Start with Temperature Scheduling**: Begin with `T=20` for soft targets, anneal to `T=1` during training.
2. **Use a Projector**: Student and Teacher hidden dimensions often differ → add a **linear projector** in Student's pathway.
3. **Match Depth**: Distill **layer-by-layer** (e.g., student layer `i` → teacher layer `2i`) for better feature alignment.
4. **Balance Hard/Soft Loss**: Start with `α=0.5`, then reduce to `0.1` as Student learns.
5. **For LLMs**: Use **sequence-level KD** (not token-level) to preserve fluency.
6. **For Diffusion**: Use **noise prediction distillation** + **adversarial loss** (e.g., **Adversarial Diffusion Distillation**, 2023).
7. **Monitor Safety Metrics**: For LLMs, track **refusal rate** and **harm score** during KD.

##  Common Pitfalls

1. **Teacher-Student Gap Too Large**: If Teacher is **100B+** and Student is **<1B**, KD may fail → use **Teacher Assistant** ([Mirzadeh et al., 2019](https://arxiv.org/abs/1902.03393)).
2. **Ignoring Safety**: Distilling a **safety-aligned teacher** without explicit safety loss → Student becomes **toxic/biased**.
3. **Over-Distillation**: Student matches Teacher on training data but **fails to generalize** → use **early stopping**.
4. **Wrong Loss Weighting**: `α` too high → Student ignores Teacher; too low → Student doesn't learn from true labels.
5. **No Data Augmentation**: KD + strong augmentation (e.g., **RandAugment**) → better Student generalization.


##  Conclusion
- [Few-Shot Knowledge Distillation of LLMs With Counterfactual Explanations](https://arxiv.org/abs/2510.21631),Faisal Hamman, Pasan Dissanayake, Yanjun Fu, Sanghamitra Dutta,2025
- [Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching](https://arxiv.org/abs/2503.20083),Benjamin Minixhofer, Ivan Vulić, Edoardo Maria Ponti,2025
- [CAST: Contrastive Adaptation and Distillation for Semi-Supervised Instance Segmentation](https://arxiv.org/pdf/2505.21904), Pardis Taghavi, Tian Liu, Renjie Li, Reza Langari, Zhengzhong Tu, 2025
- [An Empirical Study of Knowledge Distillation for Code Understanding Tasks](https://arxiv.org/abs/2508.15423),Ruiqi Wang, Zezhou Yang, Cuiyun Gao, Xin Xia, Qing Liao,2026
- [Scaling Reasoning Efficiently via Relaxed On-Policy Distillation](https://arxiv.org/abs/2603.11137), Jongwoo Ko, Sara Abdali, Young Jin Kim, Tianyi Chen, Pashmina Cameron, 2026
- [To Distill or Not to Distill: When Knowledge Transfer Undermines Safety of LLMs](https://openreview.net/pdf/fed763a30898a94daf0c79a480b698875f2cf105.pdf),2026
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) – Hinton et al. (2015) – **Foundational**.
- [FitNets: Hints for Thin Deep Nets](https://arxiv.org/abs/1412.6550) – Romero et al. (2015) – Feature-based KD.
- [Paying More Attention to Attention](https://arxiv.org/abs/1612.03928) – Zagoruyko & Komodakis (2016) – Attention transfer.
- [TinyBERT](https://arxiv.org/abs/1909.10351) – Jiao et al. (2019) – Layer-wise KD for BERT.
- [Relational Knowledge Distillation](https://arxiv.org/abs/1904.05068) – Park et al. (2019) – Instance relation graphs.
- **[2026]** [Scaling Reasoning Efficiently via Relaxed On-Policy Distillation](https://arxiv.org/abs/2603.11137) – Ko et al. – **On-policy** for reasoning models.
- **[2026]** [To Distill or Not to Distill: When Knowledge Transfer Undermines Safety of LLMs](https://openreview.net/pdf/fed763a30898a94daf0c79a480b698875f2cf105.pdf) – Critical safety analysis.
- **[2025]** [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) – **Reasoning distillation** pioneer.
- **[2025]** [MaKD: Multi-aspect Knowledge Distillation with Large Language Model](https://arxiv.org/pdf/2501.13341) – Lee et al. – Multi-aspect (logic, style, safety) distillation.
- **[2025]** [Knowledge Distillation and Dataset Distillation of LLMs: Emerging Trends](https://arxiv.org/abs/2504.14772) – Fang et al. – **Comprehensive survey**.
- **[2025]** [Autoregressive Distillation of Diffusion Transformers](https://arxiv.org/abs/2504.11295) – Kim et al. – Diffusion → AR distillation.
- **[2024]** [Wasserstein Distance Rivals KL-Divergence for Knowledge Distillation](https://arxiv.org/abs/2412.08139) – Lv et al. – More robust loss.
- **[2024]** [Logit Standardization in Knowledge Distillation](https://openaccess.thecvf.com/content/CVPR2024/html/Sun_Logit_Standardization_in_Knowledge_Distillation_CVPR_2024_paper.html) – Sun et al. – Stabilizes training.
- **[2024]** [Understanding the Role of the Projector in Knowledge Distillation](https://ojs.aaai.org/index.php/AAAI/article/view/28219/28433) – Miles & Mikolajczyk – Projector design insights.

## Implementations
### PyTorch Ecosystem
- https://github.com/yoshitomo-matsubara/torchdistill – Modular, config-driven KD framework
- https://github.com/argilla-io/distilabel – LLM distillation + synthetic data generation
- https://github.com/SforAiDl/KD_Lib – KD, pruning, quantization toolkit
- https://github.com/AberHu/Knowledge-Distillation-Zoo – Collection of 50+ KD methods
- https://github.com/dvlab-research/ReviewKD – Feature review-based distillation
- https://github.com/KaiyuYue/mgd – Matching Guided Distillation
- https://github.com/szagoruyko/attention-transfer – Attention-based distillation
- https://github.com/CuriousAI/mean-teacher – Mean Teacher framework
- https://github.com/lenscloth/RKD – Relational Knowledge Distillation
- https://github.com/HobbitLong/RepDistiller – Contrastive representation distillation
- https://github.com/NVlabs/DeepInversion – Data-free knowledge distillation
- https://github.com/IntelLabs/distiller – General compression toolkit
- https://github.com/huawei-noah/Pretrained-Language-Model/tree/master/TinyBERT – NLP distillation example
- https://github.com/clovaai/overhaul-distillation – Feature distillation improvements
- https://github.com/sunshangquan/logit-standardization-KD – Logit standardization method
- https://github.com/JiamingLv/WKD – Wasserstein distance KD
- https://github.com/gatech-sysml/deps – Efficient training / compression
- https://github.com/alsdudrla10/ARD – Diffusion transformer distillation
- https://github.com/karanchahal/distiller – Large-scale KD research framework
- https://github.com/peterliht/knowledge-distillation-pytorch – Simple KD experiments
- https://github.com/MingiJi/FRSKD – Feature refinement via self-distillation
- https://github.com/winycg/HSAKD – Self-supervised KD
- https://github.com/frankaging/Causal-Distill – Causal distillation for LLMs
- https://github.com/universal-ner/universal-ner – Distilled NER models
- https://github.com/ChaoningZhang/MobileSAM – Efficient distilled segmentation model


### TensorFlow Ecosystem
- https://www.tensorflow.org/model_optimization – Official KD + compression toolkit
- https://github.com/intel/neural-compressor – KD + quantization + pruning
- https://github.com/sseung0703/Knowledge_distillation_via_TF2.0 – TF2 implementations
- https://github.com/suhangpro/distillation – General KD implementation
- https://github.com/akamaus/mnist-distill – MNIST distillation example
- https://github.com/iRapha/replayed_distillation – Data-free KD
- https://github.com/luzai/NetworkCompress – Net2Net / compression
- https://github.com/sseung0703/KD_methods_with_TF – KD methods collection
- https://github.com/sseung0703/Zero-shot_Knowledge_Distillation – Zero-shot KD
- https://github.com/sseung0703/Knowledge_distillation_via_TF2.0 – Benchmarking KD

### Hugging Face Ecosystem
- https://huggingface.co/docs/transformers/training – Built-in training + distillation support
- https://distilabel.argilla.io/ – LLM synthetic data + distillation pipelines


### Diffusion / Vision Models
- https://github.com/huggingface/diffusers – Diffusion models + distillation support
- https://github.com/luosiallen/latent-consistency-model – Fast diffusion via LCM distillation

### TensorRT / Deployment / Optimization / Other
- https://github.com/openvinotoolkit/openvino – Inference optimization + compression
- https://github.com/PaddlePaddle/PaddleSlim – KD, pruning, quantization toolkit
- https://github.com/dmlc/mxnet/blob/master/example/bayesian-methods/bdk.ipynb – Bayesian dark knowledge
