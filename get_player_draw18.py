import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "ctx.save();" in line and "ctx.translate(player.x, player.y);" in lines[i+1]:
        start = i
        break

start = start - 15
print("Found block around line:", start)
print("".join(lines[start:start+50]))
