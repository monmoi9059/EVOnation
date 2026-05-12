import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "let aimAngle = Math.atan2(mouse.worldY - player.y, mouse.worldX - player.x);" in line:
        start = i
        break

print("Found player draw loop start around line:", start)
print("".join(lines[start:start+150]))
