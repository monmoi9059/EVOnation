with open('game.html', 'r') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if "ctx.arc(player.x, player.y" in line or "Math.cos(aimAngle)" in line and "player.size" in line:
        start = i
        break

if start != -1:
    print("Found player drawing around line:", start)
    print("".join(lines[start-20:start+20]))
