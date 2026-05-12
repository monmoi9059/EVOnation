const fs = require('fs');
let html = fs.readFileSync('game.html', 'utf8');

const startTag = '// --- PLAYER RENDERING SECTION ---';
const endTag = '// --- COMPLEX PLAYER BODY BLOCK ---';

let startIdx = html.indexOf(startTag);
let endIdx = html.indexOf(endTag);

if (startIdx === -1 || endIdx === -1) {
    console.error('Tags not found');
    process.exit(1);
}

let block = html.substring(startIdx, endIdx);

// We will replace occurrences of player.x and player.y with tCX and tCY respectively in specific rendering contexts,
// but carefully, because we also need to define tCX and tCY.

// Let's replace the top part
let newTop = `// --- PLAYER RENDERING SECTION ---
            let aimAngle = Math.atan2(mouse.worldY - player.y, mouse.worldX - player.x);

            let stageIdx_app = 0;
            if (player.level >= 5 && player.level < 15) stageIdx_app = 1;
            else if (player.level >= 15) {
                stageIdx_app = Math.floor((player.level - 15) / 10) + 2;
            }

            let torsoOffsetX_app = stageIdx_app >= 2 ? -player.size * 0.4 : 0;
            let tCX = player.x + Math.cos(aimAngle) * torsoOffsetX_app;
            let tCY = player.y + Math.sin(aimAngle) * torsoOffsetX_app;

            if(player.tail.length > 0) {`;

block = block.replace('// --- PLAYER RENDERING SECTION ---\n            let aimAngle = Math.atan2(mouse.worldY - player.y, mouse.worldX - player.x);\n\n            if(player.tail.length > 0) {', newTop);

// Fix tail coordinates
block = block.replace(/let tx = player\.tail\[i\]\.x;/g, 'let tx = player.tail[i].x + Math.cos(aimAngle) * torsoOffsetX_app;');
block = block.replace(/let ty = player\.tail\[i\]\.y;/g, 'let ty = player.tail[i].y + Math.sin(aimAngle) * torsoOffsetX_app;');
block = block.replace(/let prevX = i === 0 \? player\.x : player\.tail\[i-1\]\.x;/g, 'let prevX = i === 0 ? tCX : (player.tail[i-1].x + Math.cos(aimAngle) * torsoOffsetX_app);');
block = block.replace(/let prevY = i === 0 \? player\.y : player\.tail\[i-1\]\.y;/g, 'let prevY = i === 0 ? tCY : (player.tail[i-1].y + Math.sin(aimAngle) * torsoOffsetX_app);');

// Replace remaining player.x/player.y in the block with tCX/tCY (excluding the top aimAngle calc which is already handled, and stageIdx stuff)
// We will do this via regex for the appendage blocks.
// Let's just find and replace in the appendage blocks.

let appendageStart = block.indexOf('let isInvuln =');
let appendagesCode = block.substring(appendageStart);

// We replace `player.x` with `tCX` and `player.y` with `tCY`
appendagesCode = appendagesCode.replace(/player\.x/g, 'tCX').replace(/player\.y/g, 'tCY');

block = block.substring(0, appendageStart) + appendagesCode;

html = html.substring(0, startIdx) + block + html.substring(endIdx);
fs.writeFileSync('game.html', html);
console.log('Appended appendage base offsets patched.');
