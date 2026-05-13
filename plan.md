1. **Analyze speed and zoom relationship:**
   - Currently, `cameraZoom = (30 / (16 + player.size)) * player.visionMod;`
   - So as `player.size` goes up, `cameraZoom` gets smaller (camera zooms out).
   - Currently, `speedScale = Math.max(1, Math.pow(player.size / 14, 0.5));`
   - And `currentSpeed = (player.speed + player.speedBoost) * speedScale;`
   - So as `player.size` goes up, `currentSpeed` goes UP.
   - Since the camera zooms out AND speed goes up, the character appears to cover massive distances on the screen very quickly.

2. **Adjust Speed Calculation (`game.html`):**
   - The user wants the apparent speed on screen to not feel "much too fast".
   - A good way to connect character speed to zoom level is to make `speedScale` directly proportional to `1 / cameraZoom` (which means it scales up based on size), but maybe the current `speedScale` is scaling *too* much or the combination is off.
   - Alternatively, if we just want the *perceived screen speed* to be relatively constant, the world-space speed should scale linearly with `1 / cameraZoom`. Right now it's `speedScale` which is roughly square root.
   - Let's look closely: if the character gets 4x bigger, camera zoom is roughly 1/4. To appear to move at the same speed across the screen, the world speed needs to be 4x faster. But right now, `speedScale` is `Math.pow(4, 0.5) = 2`. So it actually appears *slower* on screen as you get bigger?
   - Wait! "we dont have the impression of going much too fast at some point".
   - Oh, I see. `cameraZoom` is smaller (e.g. 0.25). A world-speed of 10 means screen-speed is `10 * 0.25 = 2.5`.
   - Let's read the user request again: "character speed and zoom level should be connected so that we dont have the impression of going much too fast at some point".
   - Maybe right now `speedScale` increases base speed, and various mutations increase base speed (`player.speed`). A base speed of 10 scaled up by `speedScale` is fast.
   - A very common way to balance this is to make `currentSpeed` inversely proportional to `cameraZoom`. So `currentSpeed = baseSpeed / cameraZoom`. This guarantees the *screen pixels per second* is strictly constant based on base speed.
   - Let's try changing `let speedScale = Math.max(1, Math.pow(player.size / 14, 0.5));` to `let speedScale = 1 / cameraZoom;`.
   - Wait, if `cameraZoom` also includes `player.visionMod` (which zooms out further, making `cameraZoom` smaller), then `1 / cameraZoom` would increase speed just because you have better vision. That's a bad side effect.
   - So `speedScale` should just be `(16 + player.size) / 30`. Since base `player.size` is 14, at base it's `30/30 = 1.0`.
   - Then `currentSpeed = (player.speed + player.speedBoost) * ((16 + player.size) / 30)`. This exactly matches the zoom out caused by size.

3. **Verify and Adjust:**
   - I will modify `speedScale` in `update()` to `(16 + player.size) / 30`.
   - Currently, it is `Math.max(1, Math.pow(player.size / 14, 0.5))`.
   - `Math.pow(size/14, 0.5)` grows much slower than linear.
   - If the user says "impression of going much too fast", maybe the base speed just gets completely out of hand due to flat speed boosts stacking (e.g. `player.speed += 4.0` from fins, `player.speed += 2.5` from wings).
   - If I change it to `(16 + player.size) / 30`, it grows linearly with size, which might make it even faster world-wise, but *constant* screen-wise.
   - Let's clarify: if screen-wise is constant, then they won't feel like they are zipping across the map at supersonic speeds visually.
   - Also, we should apply this same scale to projectiles so they also feel consistent. Projectiles currently do: `(12 + player.speed) * speedScale`.

4. **Plan Execution:**
   - Modify `speedScale` calculation in `game.html` using `replace_with_git_merge_diff`.
   - Run verification.
   - Complete pre-commit.
   - Submit.
