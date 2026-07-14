# GNNs

## **1. Graph Basics**
- Nodes (Vertices) & Edges
- Node Features & Edge Features
- Graph-level Features
- Subgraphs & Cliques

## **2. Graph Types**
- Undirected / Directed
- Weighted / Unweighted
- Homogeneous / Heterogeneous
- Static / Dynamic / Temporal Graphs
- Bipartite / Multipartite Graphs
- Signed Graphs

## **3. Graph Representations**
- Edge List
- Adjacency List
- Adjacency Matrix
- Weighted Matrix
- Degree Matrix
- Graph Laplacian (Normalized & Unnormalized)
- Incidence Matrix
- 🔧 Sparse Tensor Representation (COO / CSR)

## **4. Traditional Graph Algorithms & Pre-GNN Learning**
- **Graph Traversal**
  - BFS (Breadth-First Search)
  - DFS (Depth-First Search)
  - Shortest Path (Dijkstra, Bellman-Ford)
- **Random Walk Methods**
  - **Random Walk**
    - مدل به‌صورت تصادفی روی شبکه حرکت می‌کند تا ببیند کدام کاربران معمولاً کنار هم دیده می‌شوند. مثلاً از یوزر A حرکت می‌کند و در طول مسیر بین فالورها (یا هر ویژگی دیگر) مدام به حلقه‌ی ABC می‌رسد؛ بنابراین یک خوشه (کلاستر) پیدا کرده است.
  - Biased Random Walk
- **Spectral Graph Theory**
  - Graph Fourier Transform
  - Laplacian Eigenmaps
- **Graph Representation Learning**
  - Matrix Factorization Methods
  - **DeepWalk**
  - Skip-Gram
  - **Node2Vec (Parameters p and q)**
    - **Node Embedding (DeepWalk / Node2Vec):** ویژگی‌های هر کاربر (فالور، فالوینگ، ریتوییت، منشن و...) به یک بردار عددی تبدیل می‌شوند که ساختار شبکه‌ی اطراف او را مشخص می‌کند. اگر دو کاربر بردارهای مشابهی داشته باشند، احتمالاً در یک دسته (ساید) قرار دارند.
  - LINE
- **Key Concepts**
  - Non-Euclidean Data
  - Permutation Invariance & Equivariance

## **5. GNN Fundamentals**
- **Theoretical Foundations**
  - Weisfeiler-Leman (WL) Test & Expressiveness
  - Message Passing Framework
- **Spectral Methods**
  - Spectral Graph Convolution
  - Signal Processing on Graphs
- **Spatial Methods**
  - Neighborhood Aggregation
- **Message Passing Neural Networks (MPNN)**
  - Message Phase
  - Aggregate Phase (Sum, Mean, Max)
  - Update Phase
- **Learning Paradigms**
  - Transductive Learning
  - Inductive Learning

  |  | Transductive | Inductive |
  |---------|--------------|------------|
  | Test nodes seen during training | ✅ | ❌ |
  | Test node labels available | ❌ | ❌ |
  | Test graph structure available during training | ✅ | ❌ |
  | Can predict new nodes | ❌ | ✅ |
  | Retraining needed for new nodes | ✅ | ❌ |
  | Best for | Static graphs | Dynamic graphs |
  | Example | Classifying users in a fixed social network | Detecting bots for newly created users |
  | Main advantage | Uses the entire graph for higher accuracy | Can generalize to new nodes and new graphs |
  | GNN models | GCN, RGCN, GAT | GraphSAGE, PinSAGE |

## **6. Classic GNN Architectures**
- **ChebNet (Chebyshev Spectral Graph Convolution)**
  - Polynomial Approximation
  - K-localized Filters
- **Graph Convolutional Network (GCN)**
  - اطلاعات همسایه‌ها را با اطلاعات خود گره ترکیب می‌کند. مثلاً برای تشخیص User B، مدل فقط خود B را نگاه نمی‌کند؛ بلکه ویژگی‌های Bot A و Bot C (همسایه‌ها) را نیز با ویژگی‌های B ترکیب می‌کند. اگر بیشتر همسایه‌های B ربات باشند، احتمال ربات بودن B نیز افزایش پیدا می‌کند.
  - Self-loops
  - Symmetric Normalization
  - Renormalization Trick
- **GraphSAGE**
  - به‌جای بررسی همه‌ی همسایه‌ها، فقط تعدادی از آن‌ها را نمونه‌گیری می‌کند (مثلاً به‌جای هزار همسایه، فقط ۱۰۰ همسایه بررسی می‌شود).
  - **Neighbor Selection Method**
    - Uniform Random Sampling
      - انتخاب تصادفی سریع، ساده ممکن است همسایه های مهم انتخاب نشوند.
    - Importance Sampling
      - همسایه‌ها بر اساس یک معیار اهمیت انتخاب می‌شوند.
        - Degree
        - Interaction frequency
        - Edge weight
        - Attention score
    -  Weighted Sampling
       - بسته به نحوه ارتباطات گراف معیار وزن (و یا جمع معیارها ) به عنوان امتیاز محاسبه می شود. و میانگین گیری میشود و درصد نهایی هر وزن محاسبه می شود.

  - **Neighbor Size Selection**
     - Fixed Sampling
     - Degree-based Sampling
       - min(k,Degree(v))
     - Adaptive Sampling
       - تعداد همسایه‌ها بر اساس اهمیت یا پیچیدگی نود تغییر می‌کند.
     - Learnable Sampling
       - مدل خودش یاد می‌گیرد چه تعداد همسایه لازم است.
       - Attention
       - Reinforcement Learning
       - Gating mechanism
 - **PinSAGE**
      - نسخه‌ای توسعه‌یافته از GraphSAGE است که توسط Pinterest برای سیستم‌های توصیه‌گر طراحی شده و برای انتخاب همسایه‌های مهم از Random Walk استفاده می‌کند.
- **Graph Attention Network (GAT)**
  - همه‌ی همسایه‌ها اهمیت یکسانی ندارند؛ مدل خودش یاد می‌گیرد به کدام همسایه بیشتر توجه کند. همسایه‌های مهم‌تر تأثیر بیشتری روی تصمیم نهایی دارند.
  - Attention Mechanism
  - Learnable Edge Weights
  - Multi-Head Attention
- **Simplifying Graph Convolution (SGC)**
  - Removing Non-linearities

## **7. Advanced GNN Architectures**
- **Expressiveness & Theory**
  - Graph Isomorphism Network (GIN)
  - 1-WL Equivalence
  - Maximal Expressiveness
- **Relational & Heterogeneous**
  - **Relational GCN (R-GCN)**
    - نسخه‌ی توسعه‌یافته‌ی GCN که نوع رابطه بین گره‌ها را نیز در نظر می‌گیرد (مثلاً Follow و Follower). GCN معمولی همه‌ی این ارتباط‌ها را تقریباً یکسان می‌بیند، اما RGCN به هرکدام وزن جداگانه می‌دهد.
  - Heterogeneous GNNs (HAN, MAGNN)
- **Equivariant GNNs**
  - E(n)-Equivariant Networks (EGNN)
  - SE(3)-Transformers
- **Graph Pooling & Hierarchical Learning**
  - DiffPool
  - SAGPool
  - TopKPool
  - MinCutPool
  - Global Pooling (Sum, Mean, Max, Attention)
- **Autoencoders & Generative**
  - Graph Autoencoder (GAE)
  - Variational Graph Autoencoder (VGAE)
- **Transformers on Graphs**
  - Graph Transformers
  - **Self-Attention on Graphs**
    - **Attention:** مدل هنگام تصمیم‌گیری یاد می‌گیرد به مهم‌ترین اطلاعات توجه بیشتری کند؛ مثلاً در جمله‌ی «گربه روی مبل خوابیده است»، برای فهم کلمه‌ی «خوابیده» بیشتر به «گربه» توجه می‌کند تا «روی».
    - **Self-Attention:** مدل ارتباط اجزای یک مجموعه را با خود همان مجموعه بررسی می‌کند؛ مثلاً در یک توییت، کلمات همان توییت به یکدیگر توجه می‌کنند تا معنای متن بهتر درک شود.
    - **Cross-Attention:** مدل ارتباط بین دو مجموعه‌ی متفاوت را یاد می‌گیرد؛ مثلاً ویژگی‌های کامیونیتی به متن توییت توجه می‌کنند تا مشخص شود آیا محتوای حساب با رفتار گروهی آن سازگار است یا خیر.
  - 🔧 Positional & Structural Encodings (Laplacian PE, RWSE)
  - Graphormer
  - Shortest Path Bias
  - GPS (General Powerful Scalable) Framework
- **Continuous & Implicit Models**
  - Deep Implicit Layers
  - ODE-GNN
  - Continuous Message Passing

## **8. GNN Challenges & Solutions**
- **Over-smoothing**
  - Representation Convergence
  - Jumping Knowledge Networks (JK-Net)
  - DropEdge
  - PairNorm, GroupNorm
- **Over-squashing**
  - Bottleneck Nodes
  - Information Loss
  - Graph Rewiring 🔧
    - 🔧 SDRF (Stochastic Discrete Ricci Flow)
    - 🔧 DIGL (Diffusion Improves Graph Learning)
  - MixHop
- **Heterophily**
  - Homophily vs Heterophily
  - H2GCN, Geom-GCN, LinkX
  - Adaptive Message Passing
- **Expressiveness Limitations**
  - Beyond 1-WL
  - Higher-Order GNNs (k-GNN, PPGN)

## **9. Scalability & Efficiency**
- **Sampling-based Methods**
  - Cluster-GCN
  - GraphSAINT
  - Neighbor Loading (ShaDow, VQGraph)
- **Graph Condensation & Dataset Distillation**
  - GCond, KIDD
  - Trajectory Matching
- **Distributed Training**
  - Partition-based Training
  - PipeGCN

## **10. Graph Learning Tasks**
- Node Classification
- Edge Classification
- Link Prediction
- Graph Classification
- Graph Regression
- Graph Generation
- Graph Clustering
- Knowledge Graph Embedding
- 🔧 Anomaly / Outlier Detection

## **11. Applications**
- Recommendation Systems
- Fraud Detection
- Knowledge Graph Completion
- Molecular Property Prediction
- Drug Discovery
- Spatial-Temporal Forecasting
- Traffic Prediction
- **Social Network Analysis**
  - 🔧 **تشخیص ربات در شبکه‌های اجتماعی (Bot Detection)**
    - **Community Features:** این حساب عضو چه گروهی است و ارتباطش با اعضای آن گروه چگونه است؟ مثلاً در ویژگی‌هایی مثل تعداد فالوور، آیا با هم کامیونیتی هستند یا چند ویژگی مشترک دیگر دارند؟
    - **Graph-Based Methods**
      - **Follow/Follower Analyze:** بررسی این‌که آیا حساب‌ها فقط همدیگر را فالو کرده‌اند و تقریباً هیچ ارتباطی با کاربران واقعی ندارند (نشانه‌ی شبکه‌ی ربات).
      - **MRF (Markov Random Field):** اگر دو همسایه‌ی User X ربات باشند، احتمال ربات بودن خود User X نیز افزایش پیدا می‌کند.
      - **Belief Propagation:** اگر یک حساب مشکوک باشد، بخشی از این «مشکوک بودن» به حساب‌های متصل به آن منتقل می‌شود؛ یعنی اگر احتمال یک برچسب را برای یک کاربر با درصد بالا بدانیم، می‌توان همان درصد را از طریق ارتباطاتش به اطرافیانش نیز تسری داد.
      - **Trust-based Detection:** کاربران واقعی معمولاً به کاربران واقعی اعتماد بیشتری دارند؛ در واقع هیچ کاربر واقعی ارتباط انسانیِ زیادی با یک ربات ندارد.
      - **Community Detection (Bot2Vec):** به‌جای بررسی یک کاربر، رفتار کل گروه بررسی می‌شود. اگر یک حساب جدید وارد یک کامیونیتی شود و رفتارش شبیه اعضای آن باشد، احتمال زیادی وجود دارد که آن هم ربات باشد.
    - **GNN-Based Methods در این کاربرد:** GCN، RGCN، GAT، GraphSAGE و PinSAGE (تعاریف کامل در بخش‌های 6 و 5) مستقیماً برای این مسئله به‌کار می‌روند.
      - **SATAR (Self-supervised Approach to Twitter Account Representation Learning):** فرض کنید حسابی داریم که متن توییت‌هایش طبیعی است، اما بیشتر با حساب‌های ربات در ارتباط است و الگوی پروفایلش نیز مشکوک است. SATAR این سه نوع اطلاعات (متن، ویژگی‌های پروفایل، ارتباط‌های شبکه) را هم‌زمان بررسی می‌کند و با استفاده از Attention یاد می‌گیرد کدام‌یک برای این حساب مهم‌تر است؛ مثلاً ممکن است نتیجه بگیرد که ارتباط‌های شبکه از متن مهم‌تر است و وزن بیشتری به آن بدهد، و در نهایت با ترکیب این اطلاعات، احتمال ربات بودن حساب را تعیین کند. هدف اصلی SATAR این است که به‌جای تکیه بر یک ویژگی، از چند نوع اطلاعات به‌طور هوشمند برای ساخت یک نمایش دقیق از هر حساب استفاده کند.
    - **Feature Fusion:** فرض کنید سه نوع اطلاعات از کاربر داریم (اطلاعات پروفایل، کامیونیتی، متن توییت‌ها)؛ به چند روش می‌توان این اطلاعات را به مدل داد:
      - Concatenation — ویژگی‌ها بدون تغییر، پشت سر هم قرار می‌گیرند.
      - Summation — ویژگی‌های هم‌اندازه با هم جمع می‌شوند.
      - Average / Max Pooling — با میانگین یا بیشترین مقدار، ویژگی‌ها به یک بردار خلاصه تبدیل می‌شوند.
      - Gated Fusion — مدل یاد می‌گیرد کدام ویژگی مهم‌تر است و به همان وزن بیشتری می‌دهد.
      - Self-Attention Fusion — هر ویژگی با سایر بخش‌های همان ویژگی ارتباط برقرار می‌کند تا اطلاعات مهم‌تر مشخص شود.
      - Cross-Attention Fusion — هر نوع ویژگی با ویژگی‌های دیگر ارتباط برقرار می‌کند تا وابستگی بین آن‌ها یاد گرفته شود *(روش استفاده‌شده در BotCF)*.
      - Co-Attention — دو نوع ویژگی به‌صورت دوطرفه هم‌زمان به یکدیگر توجه می‌کنند.
      - Smart Fusion — به هر نوع اطلاعات وزنی داده می‌شود تا مدل درجه‌ی اهمیت هرکدام را بفهمد.
- Computer Vision (Scene Graphs, Point Clouds)
- Natural Language Processing (Text Graphs)
- 🔧 Combinatorial Optimization (TSP, Graph Coloring)

## **12. Graph Deep Learning Libraries**
- **PyTorch Geometric (PyG)**
  - Dataset & Data Object
  - Node Features Tensor (x)
  - Edge Index (COO Format)
  - DataLoader & Mini-Batches
  - Block Diagonal Matrices
  - Heterogeneous Graphs & HeteroData
  - Custom Message Passing Layers
  - Profiling & Optimization
- 🔧 **DGL (Deep Graph Library)** — نام‌ برد کوتاه به‌عنوان کتابخانه‌ی جایگزین رایج

## **13. Benchmarks & Evaluation**
- Datasets: OGB, TUDataset, Planetoid (Cora/Citeseer/Pubmed)
- Metrics: Accuracy, F1, AUC-ROC, MRR/Hits@K (برای Link Prediction)
- Homophily Ratio به‌عنوان معیار توصیف داده

## **14. State-of-the-Art Topics**
- **Self-Supervised Learning (SSL)**
  - GraphCL
  - GraphMAE / GraphMAE2
  - BGRL
  - Masked Feature Reconstruction
  - Contrastive Learning on Graphs
- **Explainability (XAI)**
  - GNNExplainer
  - PGExplainer
  - Subgraph Attribution
  - ProtGNN, DIG
- **LLM + Graph**
  - GNN and LLM Integration
  - GraphGPT
  - Graph-based RAG
  - LLM as Enhancer / Predictor / Aligner
- **Generative Graph Models**
  - Diffusion Models on Graphs
  - DiGress
  - GeoDiff
  - Molecule Generation
  - Flow Matching on Graphs
- **Causal GNNs & OOD Generalization**
  - Causal Message Passing
  - Environment Invariance
  - 🔧 DIR (Discovering Invariant Rationales) — نام‌گذاری تصحیح شد
  - 🔧 CIGA (Causality Inspired Invariant Graph LeArning) — جایگزین GNN-CM
- **Foundation Models for Graphs**
  - Graph Foundation Models
  - Universal Graph Representations
  - Zero-shot & Few-shot Learning