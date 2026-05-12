with open('game.html', 'r') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if "drawVolumetricBlob" in line and "player.size" in line and not "player.clones" in line and "time" in line:
        start = i
        break

if start != -1:
    print("Found player drawing around line:", start)
    print("".join(lines[start-10:start+10]))
