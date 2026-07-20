## BotCF 

### Step 1:  Feature Extraction
- **Semantic Feature ( RoBERTa )** 
  - Bio / Description `profile.description`
  - Tweet `tweet [string list]`
- **Property Feature ( Z-score normalization and MLP )**
  - Numerical
    - Account age `profile.created_at`
    - Followers count `profile.followers_count`
    - Following count `profile.friends_count`
    - Like count `profile.favourites_count`
    - Tweet count `profile.statuses_count`
    - Username length `profile.screen_name`
    - Retweet count `not found in TwiBot-20 dataset and set by default 0`
  - Category
    - Verified status `profile.verified`
      - مشخص می‌کند که حساب دارای نشان تأیید (تیک آبی) است یا خیر.

    - Profile completeness
      - میزان کامل بودن اطلاعات پروفایل کاربر را نشان می‌دهد (ویژگی مشتق‌شده و نه یک فیلد مستقیم توییتر).

    - Default profile image `profile.default_profile_image`
      - مشخص می‌کند که کاربر هنوز از تصویر پروفایل پیش‌فرض توییتر استفاده می‌کند یا خیر.

    - Default profile `profile.default_profile`
      - مشخص می‌کند که کاربر هنوز از قالب و ظاهر پیش‌فرض پروفایل توییتر استفاده می‌کند یا خیر.

    - Geo Enabled `profile.geo_enabled`
      - مشخص می‌کند که اشتراک‌گذاری موقعیت مکانی در توییت‌ها برای این حساب فعال است یا خیر.

    - Protected `profile.protected`
      - مشخص می‌کند که حساب خصوصی (Private) است و فقط دنبال‌کنندگان تأییدشده می‌توانند توییت‌های آن را مشاهده کنند.

    - Contributors Enabled `profile.contributors_enabled`
      - مشخص می‌کند که امکان انتشار توییت توسط چندین کاربر مجاز به نمایندگی از این حساب فعال بوده است (ویژگی قدیمی توییتر).

    - Translator `profile.is_translator`
      - مشخص می‌کند که حساب به‌عنوان مترجم رسمی توییتر ثبت شده است یا خیر (ویژگی قدیمی).

    - Translation Enabled `profile.is_translation_enabled`
      - مشخص می‌کند که قابلیت‌های ترجمه توییتر برای این حساب فعال است یا خیر.

    - Background Tile `profile.profile_background_tile`
      - مشخص می‌کند که تصویر پس‌زمینه پروفایل به‌صورت تکرارشونده (Tile) نمایش داده می‌شود یا خیر (ویژگی قدیمی).

    - Use Background Image `profile.profile_use_background_image`
      - مشخص می‌کند که از تصویر پس‌زمینه سفارشی پروفایل استفاده می‌شود یا خیر (ویژگی قدیمی).

    - Extended Profile `profile.has_extended_profile`
      - مشخص می‌کند که پروفایل دارای اطلاعات تکمیلی فراتر از اطلاعات پایه است یا خیر.
- **Community Feature ( DANMF )** 
  - Generate graph with `neighbor.following` and `neighbor.following`
  - 128-dim Community Vector [0.8,0.1,0.05,0.05]
      - why 128-dim
         - Standard in Graph Embedding: The number 128 is the "sweet spot" in graph learning, preserving community structure complexity while preventing memory overflow or overfitting.
         - DANMF Inner Mechanism (Latent Communities): In the DANMF algorithm, 128 represents the number of latent communities in the network, defining the degree of each user's belonging to               these clusters.
         - Alignment with Attention Architecture: This 128-dimensional vector serves as a sufficient input for the linear layer to extract the best features, ultimately providing the                       structural features needed to build the model's final 160-dimensional vector.
        
-  `✅ Anti-Mimic Feature ( Z-score normalization and MLP )`
   -  Semantic Mimicry Features
      -  Semantic Distance `profile.description` , `tweet`
      - Text Diversity `tweet`
        - Vocabulary Size `کاربر چقدر دایره لغات غنی دارد؟`
        - Unique word ratio `این کاربر چقدر کلماتش را تکرار می‌کند`
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
| Dataset | Improvement | Final Accuracy | labels | Count | Edge |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TwiBot-20** | `+1.86%` | **86.53%** | 0: 3632, 1: 4646 | 8,178 | follower, following
| **TwiBot-22** | `+1.67%` | **81.33%** | | | |
| **Cresci-2015** | `+0.47%` | **98.21%** | | | |


####  Parameters
 - Epoch count: 150
 - Embedding size = 160
 - Features Count = numerrical 7D, categorical 11D
 
