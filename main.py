# One Line, Zero Use entry: a single original line (74 chars) naming a
# hilariously useless superpower. The program writes it to /output/entry.txt,
# where the gate checks it is 1-200 UTF-8 characters.
import os

LINE = "I can teleport anywhere in the world — as long as it's within arm's reach."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
