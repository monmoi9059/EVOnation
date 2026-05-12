import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "drawVolumetricBlob(ctx, cx, cy, player.size*0.5, player.color, time*3, \"player\", cAimAngle);" in line:
        start = i
        break

start = start - 100
if start < 0: start = 0
print("Found player main draw around line:", start)
print("".join(lines[start:start+150]))
