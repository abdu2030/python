# Snake Game — Day 20 (100 Days of Code)

A small, educational implementation of the classic Snake game built for the "100 Days of Code - The Complete Python Pro Bootcamp" (Day 20).

## Overview

This project implements a simple Snake game using Python's standard libraries. It demonstrates basic game loop logic, keyboard input handling, object-oriented design, and simple collision detection.

## Features

- Playable Snake game with grow-on-food behavior
- Scoreboard that tracks current score and high score
- Clean, modular code split across small modules for learning

## Files

- [main.py](main.py): Entry point that initializes the game window and starts the main loop.
- [snake.py](snake.py): Implements the `Snake` class (movement, growth, collisions).
- [food.py](food.py): Implements the `Food` class (randomly positioned food items).
- [scoreboard.py](scoreboard.py): Implements the `Scoreboard` class (score display and persistence).

## Requirements

- Python 3.7+ (3.8/3.9 recommended)
- `turtle` (part of the Python standard library; ensure `tkinter` is available on your system)

No external packages are required for the basic game.

## Running

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

The game window opens and the game starts. Close the window to end the program.

## Controls

- Arrow keys: Move the snake (Up, Down, Left, Right)

## Gameplay Notes

- The snake grows when it eats food. Collision with the wall or the snake's own body ends the run and resets the score (high score is preserved while the program runs).
- You can restart by running the program again.

## Development / Contributing

This repository is intended as a learning exercise. Contributions are welcome but please keep them focused on educational clarity and small, incremental improvements.

Suggested improvements:

- Add persistent high score (save/load to a file)
- Add pause/resume
- Add levels or speed increase over time

## License

This project is provided for learning purposes. Use or adapt the code freely. If you want a formal license, add a `LICENSE` file (MIT recommended).

## Contact

If you want help or have questions, open an issue or contact the maintainer.
