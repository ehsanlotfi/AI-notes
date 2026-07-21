import pandas as pd
import json
import os

PREFIX_FILENAME = "E13.csv/"
# USERS_FILE = PREFIX_FILENAME+"users.csv"  # یا "users.xlsx"
USERS_FILE = PREFIX_FILENAME + "users.xlsx"  # یا "users.xlsx"
# TWEETS_FILE = PREFIX_FILENAME+"tweets.csv"  # یا "tweets.xlsx"
TWEETS_FILE = PREFIX_FILENAME + "tweets.xlsx"  # یا "tweets.xlsx"
# FOLLOWERS_FILE = PREFIX_FILENAME+"followers.csv"  # یا "followers.xlsx"
FOLLOWERS_FILE = PREFIX_FILENAME + "followers.xlsx"  # یا "followers.xlsx"
# FRIENDS_FILE = PREFIX_FILENAME+"friends.csv"  # یا "friends.xlsx"
FRIENDS_FILE = PREFIX_FILENAME + "friends.xlsx"  # یا "friends.xlsx"
OUTPUT_FILE = PREFIX_FILENAME + "output.json"
BOT_LABEL = "1"


def load_file(path):
    """
    فایل رو می‌خونه — فرمت CSV یا Excel رو خودش تشخیص می‌ده.
    """
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    else:
        raise ValueError(f"فرمت فایل پشتیبانی نمی‌شود: {ext}")


# ============================================
# ۱. خواندن فایل‌ها
# ============================================
users = load_file(USERS_FILE)
tweets = load_file(TWEETS_FILE)
followers = load_file(FOLLOWERS_FILE)
friends = load_file(FRIENDS_FILE)

# ============================================
# ۲. ساخت lookup برای دسترسی سریع
# ============================================
# توییت‌ها بر اساس user_id
tweets_by_user = tweets.groupby('user_id')['text'].apply(list).to_dict()

# فالوورها: target_id = کاربری که فالوور دارد، source_id = فالوور
followers_by_user = followers.groupby('target_id')['source_id'].apply(list).to_dict()

# دوستان (following): source_id = کاربر، target_id = فالو‌شونده
following_by_user = friends.groupby('source_id')['target_id'].apply(list).to_dict()

# ============================================
# ۳. ساخت خروجی JSON
# ============================================
result = []

for _, row in users.iterrows():
    user_id = row['id']

    # --- ساخت بخش profile ---
    profile = {}
    for col in users.columns:
        val = row[col]
        if pd.isna(val):
            # برای فیلدهای بولین، پیش‌فرض False
            if col in [
                'protected', 'verified', 'geo_enabled', 'default_profile',
                'default_profile_image', 'profile_use_background_image',
                'profile_background_tile', 'contributors_enabled',
                'is_translator', 'is_translation_enabled', 'has_extended_profile'
            ]:
                profile[col] = "False "
            else:
                profile[col] = "None "
        else:
            profile[col] = str(val) + " "

    # --- توییت‌های کاربر ---
    user_tweets = tweets_by_user.get(user_id, [])

    # --- همسایه‌ها ---
    user_following = following_by_user.get(user_id, [])
    user_followers = followers_by_user.get(user_id, [])

    # تبدیل IDها به رشته با فاصله انتهایی (مشابه نمونه)
    user_following = [str(x) + " " for x in user_following]
    user_followers = [str(x) + " " for x in user_followers]

    entry = {
        "ID": str(user_id) + " ",
        "profile": profile,
        "tweet": user_tweets,
        "neighbor": {
            "following": user_following,
            "follower": user_followers
        },
        "domain": [],  # در فایل‌ها موجود نیست
        "label": BOT_LABEL  # در فایل‌ها موجود نیست
    }

    result.append(entry)

# ============================================
# ۴. ذخیره در فایل JSON
# ============================================
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"✅ Done! {len(result)} users processed → saved to '{OUTPUT_FILE}'")
