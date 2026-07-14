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




# BotCF
  - Reference:  [BotRGCN](https://doi.org/10.1145/3487351.3488336)- [source](https://github.com/BunsenFeng/BotRGCN) 
  - IEEE Transactions on Network and Service Management (5.7) December 2025
  - Citations (EEE (1) | Other Publishers (2))
  - [Journal Link](https://ieeexplore.ieee.org/document/11129974)
  - [source code](https://github.com/FengLiuii/BotCF)
  - [Author link](https://ieeexplore.ieee.org/author/400935237016586)
  - [Twibot20](https://www.kaggle.com/datasets/marvinvanbo/twibot-20), Twibot22, and Cresci-2015
  - 1.86%, 1.67%, 0.47%   => 86.53%, 81.33%, and 98.21%