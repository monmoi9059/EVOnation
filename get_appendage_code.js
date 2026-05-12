const fs = require('fs');
const html = fs.readFileSync('game.html', 'utf8');

const startIdx = html.indexOf('// --- PLAYER RENDERING SECTION ---');
const endIdx = html.indexOf('// --- COMPLEX PLAYER BODY BLOCK ---');
console.log(html.substring(startIdx, endIdx));
