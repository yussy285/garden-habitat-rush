"""Simulate bot players to check how fair each round of Garden Habitat Rush is.
Pure Python, no installs needed:  python simulate_balance.py
"""
import random

ROUNDS = 10          # how many rounds to test
GAMES = 5000         # simulated rounds per skill level and round number
BASE_TIME = 90       # seconds on the clock in round 1
SPEED_STEP = 0.12    # extra clock speed per round (matches the game)
MAX_SPEED = 2.5

# Each bot: (name, average seconds per item, chance of choosing the right item first time,
#            chance of tapping a clue before each item, seconds a clue costs)
BOTS = [
    ("Fast & sharp", 2.5, 0.90, 0.10, 1.5),
    ("Average", 4.0, 0.75, 0.30, 2.0),
    ("Careful beginner", 6.0, 0.60, 0.50, 2.5),
]

def speed(rnd):
    return min(MAX_SPEED, 1 + SPEED_STEP * (rnd - 1))

def play_round(rnd, secs, p_right, p_clue, clue_cost):
    """Return True if a bot finishes all 9 deposits (3 animals x 3 items) in time."""
    budget = BASE_TIME / speed(rnd)  # real seconds before the clock hits zero
    used = 0.0
    for _ in range(9):
        if random.random() < p_clue:
            used += clue_cost
        while True:
            used += max(1.5, random.gauss(secs, secs * 0.25))
            if random.random() < p_right:
                break  # right item placed; a wrong one costs another full attempt
        if used > budget:
            return False
    return used <= budget

if __name__ == "__main__":
    random.seed(42)
    print(f"{'Round':<7}{'Speed':<8}" + "".join(f"{b[0]:<20}" for b in BOTS))
    for rnd in range(1, ROUNDS + 1):
        row = f"{rnd:<7}x{speed(rnd):<7.2f}"
        for _, secs, p_right, p_clue, cost in BOTS:
            wins = sum(play_round(rnd, secs, p_right, p_clue, cost) for _ in range(GAMES))
            row += f"{wins / GAMES:<20.0%}"
        print(row)
    print("\nTip: if the 'Average' bot drops below ~50% before round 4, soften SPEED_STEP.")
