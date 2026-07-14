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
  - **Natural Language Explanation**
    - make report for user
