with open('game.html', 'r') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if "ctx.save();" in line and "ctx.translate(player.x - cameraX" in lines[i+1]:
        start = i
        break
    if "player.x - cameraX" in line:
        start = i

if start != -1:
    print("".join(lines[start:start+120]))
