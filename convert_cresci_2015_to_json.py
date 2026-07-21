import pandas as pd
import json
import os
from collections import defaultdict

# ============================================
# تنظیم مسیر فایل‌ها
# ============================================
USERS_FILE = "users.csv"
TWEETS_FILE = "tweets.csv"
FOLLOWERS_FILE = "followers.csv"
FRIENDS_FILE = "friends.csv"
OUTPUT_FILE = "output.json"

CHUNKSIZE = 50000   # تعداد ردیف در هر چانک


def detect_encoding(path):
    """
    encoding فایل رو تست می‌کنه: utf-8 → latin-1 → cp1252
    """
    for enc in ["utf-8", "latin-1", "cp1252", "iso-8859-1"]:
        try:
            with open(path, 'r', encoding=enc) as f:
                f.read(1024)
            return enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    raise ValueError(f"هیچ encoding شناخته‌شده‌ای برای {path} پیدا نشد!")


def load_file(path):
    """
    فایل CSV یا Excel رو با encoding صحیح می‌خونه.
    """
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        enc = detect_encoding(path)
        return pd.read_csv(path, encoding=enc, low_memory=False)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    else:
        raise ValueError(f"فرمت فایل پشتیبانی نمی‌شود: {ext}")


def load_chunks(path, chunksize=CHUNKSIZE):
    """
    فایل CSV رو چانک‌چانک برمی‌گردونه (Generator).
    """
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        enc = detect_encoding(path)
        return pd.read_csv(path, encoding=enc, chunksize=chunksize, low_memory=False)
    elif ext in [".xlsx", ".xls"]:
        return [pd.read_excel(path)]
    else:
        raise ValueError(f"فرمت فایل پشتیبانی نمی‌شود: {ext}")


# ============================================
# ۱. خواندن users (کوچیکه، یه‌جا می‌خونیم)
# ============================================
print("📥 Loading users...")
users = load_file(USERS_FILE)
print(f"   → {len(users)} users loaded")

# ============================================
# ۲. خواندن tweets به صورت چانک‌چانک
# ============================================
print("📥 Loading tweets (chunked)...")
tweets_by_user = defaultdict(list)

for i, chunk in enumerate(load_chunks(TWEETS_FILE)):
    print(f"   → Processing tweet chunk {i+1} ({len(chunk)} rows)...")
    for _, row in chunk.iterrows():
        uid = str(row['user_id'])
        tweets_by_user[uid].append(str(row['text']))

print(f"   → Total tweets loaded for {len(tweets_by_user)} users")

# ============================================
# ۳. خواندن followers به صورت چانک‌چانک
# ============================================
print("📥 Loading followers (chunked)...")
followers_by_user = defaultdict(list)

for i, chunk in enumerate(load_chunks(FOLLOWERS_FILE)):
    print(f"   → Processing follower chunk {i+1} ({len(chunk)} rows)...")
    for _, row in chunk.iterrows():
        target = str(row['target_id'])
        source = str(row['source_id'])
        followers_by_user[target].append(source)

print(f"   → Total users with followers: {len(followers_by_user)}")

# ============================================
# ۴. خواندن friends (following) به صورت چانک‌چانک
# ============================================
print("📥 Loading friends (chunked)...")
following_by_user = defaultdict(list)

for i, chunk in enumerate(load_chunks(FRIENDS_FILE)):
    print(f"   → Processing friends chunk {i+1} ({len(chunk)} rows)...")
    for _, row in chunk.iterrows():
        source = str(row['source_id'])
        target = str(row['target_id'])
        following_by_user[source].append(target)

print(f"   → Total users with following: {len(following_by_user)}")

# ============================================
# ۵. ساخت خروجی JSON
# ============================================
print("🔧 Building JSON output...")
result = []

for _, row in users.iterrows():
    user_id = str(row['id'])
    
    # --- ساخت بخش profile ---
    profile = {}
    for col in users.columns:
        val = row[col]
        if pd.isna(val):
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
    
    # --- توییت‌ها و همسایه‌ها ---
    user_tweets = tweets_by_user.get(user_id, [])
    user_following = [x + " " for x in following_by_user.get(user_id, [])]
    user_followers = [x + " " for x in followers_by_user.get(user_id, [])]
    
    entry = {
        "ID": user_id + " ",
        "profile": profile,
        "tweet": user_tweets,
        "neighbor": {
            "following": user_following,
            "follower": user_followers
        },
        "domain": [],
        "label": "0"
    }
    result.append(entry)

# ============================================
# ۶. ذخیره JSON
# ============================================
print(f"💾 Saving to {OUTPUT_FILE}...")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"✅ Done! {len(result)} users processed → '{OUTPUT_FILE}'")
