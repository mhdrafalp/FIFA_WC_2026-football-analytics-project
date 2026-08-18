import pandas as pd
import numpy as np

# -------------------------------
# 1. LOAD DATA
# -------------------------------

df = pd.read_csv("data/wc_players.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")

df["position"] = df.get("position", "Unknown").fillna("Unknown")
df["full_name"] = df.get("full_name", df.index.astype(str))

print("✅ Data Loaded")

# -------------------------------
# 2. SAFE COLUMN GETTER
# -------------------------------

def get_col(name, fallback=None):
    if name in df.columns:
        return df[name].fillna(0)
    elif fallback and fallback in df.columns:
        return df[fallback].fillna(0)
    return pd.Series(0, index=df.index)

goals = get_col("goals", "goals_per_90")
assists = get_col("assists", "assists_per_90")
shots = get_col("shots_total")
key_passes = get_col("key_passes")
dribbles = get_col("dribbles")

df["age"] = df.get("age", 25).replace(0, 25).fillna(25)
df["minutes_played_overall"] = df.get("minutes_played_overall", 0).fillna(0)

# -------------------------------
# 3. NORMALIZATION
# -------------------------------

def normalize(s):
    return s / (s.max() if s.max() != 0 else 1)

norm_df = pd.DataFrame({
    "minutes_norm": normalize(df["minutes_played_overall"]),
    "goals_norm": normalize(goals),
    "assists_norm": normalize(assists),
    "shots_norm": normalize(shots),
    "key_passes_norm": normalize(key_passes),
    "dribbles_norm": normalize(dribbles)
})

df = pd.concat([df, norm_df], axis=1)

# -------------------------------
# 4. PERFORMANCE INDEX
# -------------------------------

df["performance_index"] = (
    0.30 * df["goals_norm"] +
    0.20 * df["assists_norm"] +
    0.15 * df["shots_norm"] +
    0.15 * df["key_passes_norm"] +
    0.10 * df["dribbles_norm"] +
    0.10 * df["minutes_norm"]
)

np.random.seed(42)
df["performance_index"] += np.random.uniform(0, 0.02, len(df))

# -------------------------------
# 5. PERFORMANCE SCORE (0–100)
# -------------------------------

def safe_norm(x):
    return (x - x.min()) / (x.max() - x.min()) * 100 if x.max() != x.min() else 50

df["performance_score"] = df.groupby("position")["performance_index"].transform(lambda x: safe_norm(x))

# -------------------------------
# 6. MARKET VALUE (kept but NOT used)
# -------------------------------

df["market_value_million"] = (
    df["performance_score"] * 0.7 +
    ((30 - df["age"]).clip(lower=0)) * 0.3
)

# -------------------------------
# 7. FINAL SCORE
# -------------------------------

def age_score(age):
    if 24 <= age <= 30: return 1
    elif 21 <= age < 24: return 0.9
    elif 18 <= age < 21: return 0.8
    return 0.85

df["age_score"] = df["age"].apply(age_score)

max_min = df["minutes_played_overall"].max()
df["consistency_score"] = df["minutes_played_overall"] / (max_min if max_min != 0 else 1)

df["final_score"] = (
    df["performance_score"] * 0.6 +
    df["age_score"] * 100 * 0.2 +
    df["consistency_score"] * 100 * 0.2
)

# -------------------------------
# 8. ✅ UNDERRATED LOGIC
# -------------------------------

df["minutes_percentile"] = df["minutes_played_overall"].rank(pct=True)
df["performance_percentile"] = df["performance_score"].rank(pct=True)

df["undervalued_score"] = (
    df["performance_percentile"] - df["minutes_percentile"]
).round(4)

# -------------------------------
# 9. PLAYER CATEGORY
# -------------------------------

def classify(score, age):
    if score >= 80: return "Elite"
    elif score >= 65: return "Top Player"
    elif score >= 50 and age <= 27: return "High Potential"
    elif score >= 50: return "Experienced"
    return "Developing"

df["player_category"] = df.apply(lambda x: classify(x["final_score"], x["age"]), axis=1)

# -------------------------------
# 10. ✅ UPDATED FILTER (RATING + LOW MINUTES)
# -------------------------------

rating = get_col("average_rating_overall")

df["rating"] = rating
filtered_df = df[
    (df["rating"] >= 7.5) &
    (df["minutes_played_overall"] < 420) &
    (df["age"] <= 29)
]

underrated_df = filtered_df.sort_values(
    by="undervalued_score", ascending=False
).head(25)

# -------------------------------
# 11. FIX PERFORMANCE WARNING
# -------------------------------

df = df.copy()

# -------------------------------
# 12. SAVE DATASETS
# -------------------------------

df.to_csv("final_players_dataset.csv", index=False)
underrated_df.to_csv("underrated_players.csv", index=False)

print("✅ Final dataset saved")
print("✅ Underrated players file created (RATING + MINUTES LOGIC APPLIED)")