"""Analyse playtest data exported from Garden Habitat Rush.

1. Play the game, then open the Data button on the win / lose / end screen.
2. Copy the CSV text into a file called playtests.csv next to this script.
3. pip install pandas matplotlib
4. python analyze_playtests.py playtests.csv
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else "playtests.csv"
df = pd.read_csv(path)
print(f"Loaded {len(df)} animal-rounds from {df['timestamp'].nunique()} sessions/rounds.\n")

# 1. Win rate by round (one row per animal, so collapse to one row per round played)
rounds = df.drop_duplicates(["timestamp", "round"])
win_rate = rounds.groupby("round")["round_result"].apply(lambda s: (s == "win").mean())
print("Win rate by round:\n", win_rate.round(2).to_string(), "\n")

# 2. Which animals are hardest?
by_animal = df.groupby("animal").agg(
    appearances=("animal", "count"),
    completion_rate=("completed", "mean"),
    avg_wrong=("wrong_placements", "mean"),
    avg_hints=("hints_used", "mean"),
    avg_seconds=("seconds_to_finish", "mean"),
).round(2).sort_values("avg_wrong", ascending=False)
print("Per-animal difficulty (most confusing first):\n", by_animal.to_string(), "\n")

hardest = by_animal.index[0]
print(f"Insight: '{hardest}' causes the most wrong placements. Try rewriting its clues.")

# 3. Charts for your README
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
win_rate.plot(kind="bar", ax=ax[0], color="#4cbb5a", title="Win rate by round")
ax[0].set_ylim(0, 1)
by_animal[["avg_wrong", "avg_hints"]].plot(kind="bar", ax=ax[1], title="Confusion by animal")
plt.tight_layout()
plt.savefig("playtest_summary.png", dpi=150)
print("Saved playtest_summary.png")
