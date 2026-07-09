# Crossing the Road (Day 23)

This is a small "Crossing the Road" arcade game built with Python's turtle module. The goal is to move the turtle (player) from the bottom of the screen to the top while avoiding moving cars.

This README explains how to run the project, how the code is organized, and how to tweak behavior such as car spawn rate and speed.

---

## Requirements

- Python 3.10+ (the code was developed with modern Python; compiled files in the repo indicate Python 3.13, but 3.10+ is fine)
- Standard library only (uses `turtle`, `random`, `time`)

No external packages are required.

## Run (Windows PowerShell)

Open a PowerShell prompt in the project folder (the folder that contains `main.py`) and run:

```powershell
python .\main.py
```

If your environment uses `python3` instead of `python` use that command.

The game will open in a Turtle graphics window.

## Controls

- Up Arrow: move the turtle forward (toward the top of the screen)

## Gameplay

- Cars are spawned randomly on the right edge and move left across the screen.
- When the player reaches the top (finish line) the player is reset to the bottom, the scoreboard level increases, and cars speed up.
- If a car collides with the player, the player is reset to the starting position (collision handling can be customized).

## Project files

- `main.py` — game loop, input handling, and integration of Player, CarManager, and Scoreboard. The loop creates and moves cars each frame and checks collisions.
- `player.py` — `Player` class (subclass of `turtle.Turtle`) that handles player movement and reset.
- `car_manager.py` — `CarManager` class that manages multiple car `Turtle` objects, random spawning, moving, and speed increases.
- `scoreboard.py` — `Scoreboard` class that displays and increments the level.

## Key parameters (where to edit)

- Car spawn chance: in `car_manager.py`, `create_car()` currently spawns a car with a 1-in-6 chance each frame (random.randint(1, 6) == 1). Change the `6` to a smaller number to increase spawn rate or larger to decrease it.
- Car starting speed: `STARTING_MOVE_DISTANCE` in `car_manager.py`.
- Car speed increment: `MOVE_INCREMENT` in `car_manager.py`.
- Car sizes/appearance: `new_car.shapesize(stretch_len=3, stretch_wid=1)` and `COLORS` in `car_manager.py`.
- Screen size: `screen.setup(width=600, height=600)` in `main.py`.
- Collision sensitivity: `if car.distance(player) < 20:` in `main.py` — change the threshold if collisions are too permissive or too strict.



## Troubleshooting

- Nothing appears / window closes immediately: run from a terminal (PowerShell) so the window doesn't close; check for Python errors printed in the terminal.
- `ModuleNotFoundError`: ensure you're running the command from the correct folder which contains `main.py`.
- Slow performance: reduce the number of active cars; reduce shapesize or spawn rate; or increase `time.sleep` value (`speed` variable in `main.py`) to slow down the loop.

## License

This project is provided as-is for learning purposes. Feel free to reuse or modify the code for your own learning projects.

---

If you want, I can:

- add a short `USAGE.md` or inline in-game help, or
- implement one of the suggested improvements (collision handling that ends the game, lifebar, fixed lanes, off-screen cleanup improvements), or
- tune spawn/spawn-chance/speed values for a specific difficulty.

Tell me which improvement you'd like next and I will implement it.

