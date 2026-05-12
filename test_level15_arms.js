const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file://' + __dirname + '/game.html');

  await page.evaluate(() => {
      player.level = 15;
      player.xp = 0;
      player.dna = 100;
      player.appendage = 'arms';
      player.mouth = 'beak';
      player.tail = [];
      for (let i = 0; i < 15; i++) {
        player.tail.push({x: player.x - i * 5, y: player.y});
      }
      player.predatorTraits = 1;

      console.log("Player stats:", { level: player.level, stageIdx: (Math.floor((player.level - 15) / 10) + 2) });
  });

  await page.waitForTimeout(1000);

  await page.screenshot({ path: 'screenshot_lvl15_arms.png' });
  console.log("Screenshot saved as screenshot_lvl15_arms.png");

  await browser.close();
})();
