const fs = require('fs');
const code = fs.readFileSync('game.html', 'utf8');

const expectedSpeedScale = `let speedScale = Math.max(1, player.size / 14);`;
const currentSpeedScaled = `let currentSpeed = (player.speed + player.speedBoost) * speedScale;`;

if (code.includes(expectedSpeedScale) && code.includes(currentSpeedScaled) && code.includes(`* speedScale`)) {
    console.log("Looks good");
} else {
    console.log("Missing expected lines in game.html");
}
