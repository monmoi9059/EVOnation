import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "let stageIdx = 0;" in line and i > 2000:
        start = i
        break

start = start - 5
print("Found stageIdx block around line:", start)
print("".join(lines[start:start+50]))
