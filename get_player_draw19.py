import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "let stageIdx = 0;" in line and i > 1500:
        start = i
        break

start = start + 30
print("Found block around line:", start)
print("".join(lines[start:start+50]))
