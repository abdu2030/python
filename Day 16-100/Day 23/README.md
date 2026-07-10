# 🐢 Crossing the Road (Frogger Arcade)

An upgraded, retro-style action arcade game based on the classic Frogger. Help the turtle cross a busy highway filled with speeding cars, collect power-ups, and level up while avoiding crashes!

---

## ✨ Features

### 🎮 Gameplay & Controls
*   **4-Directional Movement**: Move UP, DOWN, LEFT, and RIGHT using Arrow keys or `WASD` keys.
*   **Grid Boundaries**: Added boundaries to keep the player safely within the playable screen frame.
*   **Lives System**: Start with **3 lives** (displayed as `❤️` hearts). Colliding with a car resets your position and clears the road, rather than triggering an instant Game Over.
*   **High Score Persistence**: Displays your current level and the all-time high score (`HI`) on the screen. The high score is saved to and loaded from a local file (`highscore.txt`).

### ⚡ Power-Up System
Special items spawn randomly on the road and remain visible for 10 seconds. Collecting them grants unique bonuses:
*   **Shield (Cyan Circle 🔵)**: Grants temporary invincibility. It absorbs the next car collision, destroying the car and protecting your life. Changes the turtle's color to cyan.
*   **Snail (Orange Square 🟧)**: Triggers slow-motion mode, reducing the speed of all cars by 65% for 8 seconds.
*   **Feather (Golden Triangle 🔺)**: Grants a speed boost to the turtle's movement (moving at 32 pixels instead of 20) for 8 seconds. Changes the turtle's color to orange.

### 🎨 Visual & Audio Polish
*   **Court Lanes & Sidewalks**: Beautifully drawn emerald-green sidewalks (safe zones), solid white boundary lines, and golden yellow dashed road dividers.
*   **Asynchronous Audio Effects**: Uses standard Python `winsound` running inside background threads. It triggers audio cues for movement, level completion, collisions, and collecting power-ups without causing any lag.
*   **Precise Collisions**: Implements bounding-box overlap checks to handle rectangular car collisions fairly.

---

## 🛠️ File Structure & Architecture

*   [main.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/main.py) — Coordinates game loop, keyboard state history (clicks play sound only on initial press), collision overlaps, and power-up timers.
*   [player.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/player.py) — Manages player coordinates, speed modifiers, and changes shape colors dynamically based on active power-up states.
*   [car_manager.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/car_manager.py) — Manages car creation, speed increases per level, and slow-motion overrides.
*   [scoreboard.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/scoreboard.py) — Manages text displays for levels, remaining lives, game over panels, and persistent file reads/writes.
*   [road_drawer.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/road_drawer.py) — Drawing script using a fast turtle to paint the road visual markings.
*   [powerup.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/powerup.py) — Handles the spawning, lifetime tick reduction, and coordinates of collectable items on the road.
*   [sound_manager.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2023/sound_manager.py) — Plays arcade beeps asynchronously.

---

## 🚀 Installation & Requirements

### 1. Requirements
*   Python 3.10+
*   Windows OS (for `winsound` audio support)

Runs entirely using standard libraries (no external pip packages required).

### 2. Run the Game
Navigate to the directory and run:
```bash
python main.py
```
