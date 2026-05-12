import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "drawVolumetricBlob(ctx, player.x, player.y, player.size, player.color, time, \"player\", aimAngle);" in line:
        start = i
        break

start = start - 150
if start < 0: start = 0
print("Found player main draw around line:", start)
print("".join(lines[start:start+180]))
