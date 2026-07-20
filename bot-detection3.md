## BotCF 

### Step 1:  Feature Extraction
- **Semantic Feature ( RoBERTa )** 
  - Bio / Description
  - Tweet
- **Property Feature ( Z-score normalization and MLP )**
  - Numerical
    - Account age
    - Followers count
    - Following count
    - Number of tweets
  - Category
    - Verified status
    - Profile completeness
    - Default profile image
    - Geo Enabled
    - Protected
- **Community Feature ( DANMF )**
  - Community Vector [0.8,0.1,0.05,0.05]

-  `✅ Anti-Mimic Feature ( Z-score normalization and MLP )`
   -  Semantic Mimicry Features
      -  Semantic Distance
         -  Dsem​=1−cos(Si​,Shuman​)
      - Text Diversity
        - Vocabulary Size
        - Unique word ratio
    - Behavioral Mimicry Features
      - Posting Interval Pattern
      - Activity Periodicity
      - Burstiness

### Step 2:  Feature Fusion
  - **Cross-Attention Fusion ( Initial Node Representation )**


### Step 3:  Node Representation Learning
- **❌ Two-layer RGCN**
- `✅ Two-layer GraphSAGE`

### step 4: Classification
  - **Softmax** -> Human / Bot

### Step 5: ✅Explainable AI (XAI)
  - **Feature-level Explainability**
    - SHAP
  - **Graph Explainability**
    - PGExplainer
  - **Counterfactual**
    - DiCE
    - CF-GNNExplainer (For Graph)
  - **Natural Language Explanation**
    - make report for user



###  BotCF 
#### General Information
* **Journal:** [IEEE Transactions on Network and Service Management](https://ieeexplore.ieee.org/document/11129974)
* **Impact Factor:** `5.7`
* **Publication Date:** December 2025
* **Citations:** 3 total (1 in IEEE | 2 by other publishers)


####  References & Links
* **Source Code:** [FengLiuii/BotCF (GitHub)](https://github.com/FengLiuii/BotCF)
* **Author Profile:** [IEEE Author Link](https://ieeexplore.ieee.org/author/400935237016586)
* **Baseline/Base Paper (BotRGCN):**
  * [BotRGCN Paper Link](https://doi.org/10.1145/3487351.3488336)
  * [BotRGCN Source Code](https://github.com/BunsenFeng/BotRGCN)


####  Datasets
* [TwiBot-20](https://www.kaggle.com/datasets/marvinvanbo/twibot-20)
* [TwiBot-22](https://botometer.osome.iu.edu/data/datasets/twibot-22/twibot-22.csv.gz)
* [Cresci-2015](https://botometer.osome.iu.edu/data/datasets/cresci-2015/cresci-2015.csv.tar.gz)


####  Performance Improvement
| Dataset | Improvement | Final Accuracy | labels | Count |
| :--- | :---: | :---: | :---: |
| **TwiBot-20** | `+1.86%` | **86.53%** | 0: 3632, 1: 4646 | 8,178 |
| **TwiBot-22** | `+1.67%` | **81.33%** | | |
| **Cresci-2015** | `+0.47%` | **98.21%** | | |


####  Parameters
 - Epoch count: 150
 - Embedding size = 160
 - Features Count = numerrical 7D, categorical 11D
 
