# 🏡 Garden Habitat Rush (60-Second Sanctuary)

A browser game where you decode animals' clues, gather the right materials from the garden, and build three homes before the clock runs out. Each home needs 3 materials, and each round the clock runs faster.

**▶ Play it:** _add your GitHub Pages link here_

## How to play
1. Three random animals need houses, but nobody tells you what to build with.
2. Tap an animal's speech bubble for a clue.
3. Tap a material in the garden to pick it up, then tap the animal's building site to place it.
4. Finish all three homes before the timer hits zero. Round 2 runs 12% faster, round 3 more, and so on.

## Features
- 6 animals, 8 materials, all drawn as inline SVG
- Randomised rounds, escalating difficulty, a live high score (saved in your browser)
- Sound effects built with the Web Audio API (no audio files)
- Built-in playtest logging (Data button on the end-of-round screen)

## Python tools (`/python`)
| Script | What it does |
| --- | --- |
| `simulate_balance.py` | Simulates thousands of bot players to see how win rate changes per round |
| `analyze_playtests.py` | Analyses real playtest data with pandas and matplotlib and makes charts |
| `make_sample_data.py` | Generates fake data so you can try the analysis first |

```bash
pip install pandas matplotlib
python python/simulate_balance.py
python python/analyze_playtests.py playtests.csv
```

## Project structure
```
index.html      # the whole game (HTML + CSS + JavaScript)
python/         # balancing and analytics scripts
README.md
```

## What I learned
_Add 2–3 lines: e.g. which animal's clues confused players most and how you changed them._

Built by Yusrah.
