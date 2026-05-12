import re
with open('game.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "drawVolumetricBlob(ctx, e.x, e.y, e.size" in line:
        print("Found line:", i)
        print("".join(lines[i-5:i+5]))
        break
