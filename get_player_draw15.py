import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "ctx.translate(player.x, player.y);" in line:
        start = i
        break

start = start - 45
print("Found player body center around line:", start)
print("".join(lines[start:start+100]))
