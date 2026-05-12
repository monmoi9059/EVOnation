const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();

    // Log console messages
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

    await page.goto(`file://${process.cwd()}/game.html`);

    // Wait a little bit for the game to start and draw the player
    await page.waitForTimeout(2000);

    // Get player stats
    const playerStats = await page.evaluate(() => {
        return {
            level: player.level,
            stageIdx: (player.level >= 5 && player.level < 15) ? 1 : (player.level >= 15 ? Math.floor((player.level - 15) / 10) + 2 : 0)
        };
    });
    console.log("Player stats:", playerStats);

    await page.screenshot({ path: 'screenshot_lvl1.png' });
    console.log("Screenshot saved as screenshot_lvl1.png");

    await browser.close();
})();
