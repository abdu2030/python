# 🏓 AKA Pong Arcade

An upgraded, highly polished desktop clone of the classic Pong game. Built using Python's standard **Turtle graphics** library, this implementation features a smooth frame-rate lock, a beatable AI opponent, a pause state, customized court visual markings, and thread-safe asynchronous sound effects.

---

## ✨ Features

*   **Beatable AI CPU Opponent**: Press the `A` key to toggle the left paddle between manual player control (W/S) and automatic CPU tracking. The AI tracks the ball's Y-coordinate with a capped speed, making it challenging but fair and beatable.
*   **Asynchronous Audio Effects**: Uses Python's standard `winsound` library running inside background threads. It triggers audio feedback for wall bounces, paddle hits, scores, and match wins without stalling the gameplay loop.
*   **Pause & Resume Mechanics**: Press `P` at any time to pause or resume the game. An overlay clearly shows the paused state.
*   **Polished Court Visuals**: Generates a retro court layout with a dashed center divider line, a mid-court circle, and solid gray boundaries.
*   **Physics Speed Scaling & Cap**: The ball speeds up by a fixed increment after every successful paddle bounce, making rallies progressively harder. A hard speed cap keeps the ball within playable limits.
*   **Precise Collision Detection**: Uses rectangular bounding-box overlaps instead of simple radial distances, preventing the ball from clipping through paddle edges.
*   **Win Screen**: Play matches up to a target win score of **7 points**. When the match concludes, a victory banner displays the winner.

---

## 🎮 How to Play

### Controls
*   **Right Paddle**: Move with **Up Arrow** and **Down Arrow**.
*   **Left Paddle**: Move with **W** (up) and **S** (down).
*   **AI Toggle**: Press **A** to toggle the left paddle between manual Player 1 and AI CPU control.
*   **Pause**: Press **P** to Pause/Resume.

### Win Condition
*   First player to reach **7 points** wins the match.

---

## 🛠️ File Structure & Architecture

*   [main.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/main.py) — Holds the main game loop, keyboard listeners, physics update sequencing, and collision checks. It locks updates at a fixed tick rate (~20 fps) so that ball speed changes are independent of system hardware speed.
*   [paddel.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/paddel.py) — Defines the `Paddle` class with movement methods clamped to screen boundaries (paddles cannot go off-screen) and the AI tracking algorithm.
*   [ball.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/ball.py) — Defines the `Ball` class with velocity modifiers, a speed limit cap, and direction randomization on score reset.
*   [scoreboard.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/scoreboard.py) — Displays real-time scores, player name tags ("CPU" vs "Player 1"), and overlays for "PAUSED" or victory states.
*   [court_drawer.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/court_drawer.py) — Draw helper which uses a fast drawing turtle to construct the court stripes at startup.
*   [sound_manager.py](file:///c:/Users/Admin/Desktop/python%20repo/python/Day%2016-100/Day%2022/sound_manager.py) — Audio trigger functions running beeps inside background daemon threads.

---

## 🚀 Installation & Requirements

### 1. Requirements
*   Python 3.10+
*   Windows OS (for `winsound` support)

No external libraries are required. The game runs using Python standard library packages.

### 2. Run the Game
Navigate to the directory and run:
```bash
python main.py
```
