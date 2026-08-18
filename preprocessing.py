import pandas as pd

# load data
df = pd.read_csv('data/wc_players.csv')

# select only important columns
df = df[[
    'full_name',
    'position',
    'Current Club',
    'nationality',
    'goals_overall',
    'assists_overall',
    'minutes_played_overall',
    'average_rating_overall'
]]

# rename for simplicity
df.columns = [
    'player',
    'position',
    'club',
    'nationality',
    'goals',
    'assists',
    'minutes',
    'rating'
]

# remove players with 0 minutes (very important)
df = df[df['minutes'] > 0]

# handle missing values
df = df.dropna()

# create performance metrics
df['goals_per_90'] = df['goals'] / (df['minutes'] / 90)
df['assists_per_90'] = df['assists'] / (df['minutes'] / 90)

# 🔥 FUTURE STAR BASIC SCORE
df['performance_score'] = (
    df['goals_per_90'] * 0.5 +
    df['assists_per_90'] * 0.3 +
    df['rating'] * 0.2
)

# save cleaned data
df.to_csv('data/cleaned_wc_players.csv', index=False)

print(df.head())
print("✅ CLEANING DONE")