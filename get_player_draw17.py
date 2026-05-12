import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "function buildPlayerBodyPath(" in line:
        start = i
        break

print("Found buildPlayerBodyPath block around line:", start)
print("".join(lines[start:start+100]))
