"""Create a fake playtests.csv so you can try the analysis before collecting real data."""
import csv, random
animals = ["bird", "turtle", "rabbit", "frog", "owl", "squirrel"]
random.seed(1)
with open("playtests.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "round", "speed", "animal", "round_result", "completed",
                "wrong_placements", "hints_used", "seconds_to_finish"])
    for g in range(40):
        rnd = random.randint(1, 5)
        result = "win" if random.random() < 0.85 - rnd * 0.1 else "lose"
        for a in random.sample(animals, 3):
            done = 1 if result == "win" or random.random() < 0.5 else 0
            w.writerow([f"2026-10-25T10:{g:02d}", rnd, f"{1 + .15 * (rnd - 1):.2f}", a, result, done,
                        random.randint(0, 3) + (2 if a == "frog" else 0), random.randint(0, 2),
                        round(random.uniform(8, 40), 1) if done else ""])
