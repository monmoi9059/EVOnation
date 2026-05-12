with open('game.html', 'r') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines):
    if "function drawEntity(" in line:
        start = i
        break

if start != -1:
    print("".join(lines[start:start+120]))
