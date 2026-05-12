with open("game.html", "r") as f:
    content = f.read()

import re

search_block = """            // --- COMPLEX PLAYER BODY BLOCK ---
            ctx.save();
            ctx.translate(player.x, player.y);
            ctx.rotate(aimAngle);

            let stageIdx = 0;
            if (player.level >= 5 && player.level < 15) stageIdx = 1;
            else if (player.level >= 15) {
                stageIdx = Math.floor((player.level - 15) / 10) + 2;
            }

            let wobble = Math.sin(time * 5) * (player.size * 0.08);
            let r = player.size;"""

replace_block = """            // --- COMPLEX PLAYER BODY BLOCK ---
            ctx.save();
            ctx.translate(player.x, player.y);
            ctx.rotate(aimAngle);

            let stageIdx = 0;
            if (player.level >= 5 && player.level < 15) stageIdx = 1;
            else if (player.level >= 15) {
                stageIdx = Math.floor((player.level - 15) / 10) + 2;
            }

            let wobble = Math.sin(time * 5) * (player.size * 0.08);
            let r = player.size;

            let torsoOffsetX = stageIdx >= 2 ? -r * 0.4 : 0;
            let torsoOffsetY = 0;
            let headOffsetX = stageIdx >= 2 ? r * 0.8 : 0;
            let headOffsetY = 0;"""

content = content.replace(search_block, replace_block)

with open("game.html", "w") as f:
    f.write(content)
