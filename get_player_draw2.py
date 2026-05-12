with open('game.html', 'r') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if "drawEntity(ctx, player" in line or "drawEntity(player" in line or "drawEntity(ctx, b" in line or "drawEntity(ctx, e" in line:
        start = i
        break

if start != -1:
    print("Found drawEntity usage around line:", start)
    print("".join(lines[start-5:start+10]))
