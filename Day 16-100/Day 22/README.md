# Pong Game

A classic Pong game implementation in Python using the Turtle graphics library. This is an interactive two-player game where players control paddles to bounce a ball back and forth.

## Overview

Pong is one of the earliest arcade video games. In this implementation, two players compete to score points by causing the ball to pass their opponent's paddle. The game features increasing difficulty as the ball moves faster with each successful paddle hit.

## Features

- **Two-Player Gameplay**: Control two paddles (left and right) simultaneously
- **Real-time Score Tracking**: Display of current scores for both players
- **Dynamic Difficulty**: Game speed increases by 10% with each paddle hit
- **Continuous Paddle Movement**: Smooth paddle control when holding arrow keys or letter keys
- **Ball Physics**: Simple collision detection with walls and paddles
- **Win Condition**: First player to score 5 points wins the game
- **Visual Feedback**: Game Over message with winner announcement

## Requirements

- Python 3.x
- Turtle graphics (included with Python standard library)

## Installation

1. Clone or download this project to your local machine
2. Navigate to the Day 22 directory
3. Ensure all files are in the same directory:
   - `main.py`
   - `paddel.py`
   - `ball.py`
   - `scoreboard.py`

## How to Play

### Running the Game

```bash
python main.py
```

### Controls

**Right Player (Right Paddle):**
- **Up Arrow** - Move paddle up
- **Down Arrow** - Move paddle down

**Left Player (Left Paddle):**
- **W Key** - Move paddle up
- **S Key** - Move paddle down

### Objective

1. Use your paddle to bounce the ball back to your opponent
2. If your opponent misses the ball and it goes past their paddle, you score a point
3. The first player to score 5 points wins the game
4. The game speed increases with each successful hit, making it progressively more challenging

### Game Mechanics

- **Ball Bouncing**: The ball bounces off the top and bottom walls automatically
- **Paddle Collision**: When the ball collides with a paddle, it bounces back horizontally
- **Speed Increase**: Every time the ball hits a paddle, the game speed increases by 10%
- **Reset on Score**: When a player scores, the ball returns to the center and the speed resets to normal
- **Win Condition**: The game ends when either player reaches 5 points

## File Structure

### `main.py`
The main game loop and controller. Contains:
- Screen setup and configuration
- Game loop logic
- Collision detection (walls and paddles)
- Score tracking and win condition
- Keyboard input handling with continuous key press detection

### `paddel.py`
Defines the Paddle class. Features:
- Creates a white square paddle
- Methods to move the paddle up and down
- Inherits from Python's Turtle class

### `ball.py`
Defines the Ball class. Features:
- Creates a white circular ball
- Movement logic
- Bounce methods for both X and Y directions
- Game over reset functionality
- Inherits from Python's Turtle class

### `scoreboard.py`
Defines the Scoreboard class. Features:
- Displays scores for both players
- Updates display after each point
- Tracks left and right player scores
- Inherits from Python's Turtle class

## Game Flow

```
START
  ↓
Initialize paddles, ball, and scoreboard
  ↓
Game Loop:
  ├─ Check for key presses and move paddles
  ├─ Update ball position
  ├─ Check collisions with walls → bounce ball
  ├─ Check collisions with paddles → bounce ball and increase speed
  ├─ Check if ball went out of bounds → score point and reset
  └─ Check if anyone reached 5 points → show winner and end game
```

## Technical Details

### Continuous Key Press Detection

The game implements a key tracking system that:
- Records when a key is pressed with `onkeypress()`
- Records when a key is released with `onkeyrelease()`
- Checks the key state every frame in the game loop
- This allows for smooth, continuous paddle movement

### Collision Detection

**Wall Collision**: 
- Checks if ball's Y coordinate exceeds ±280 pixels
- Reverses Y velocity to bounce

**Paddle Collision**:
- Uses distance calculation between ball and paddle center
- Verifies ball is within correct X range to prevent double bounces
- Reverses X velocity to bounce

**Out of Bounds**:
- Checks if ball passes X coordinates ±385 (beyond paddle positions)
- Triggers score update and ball reset

### Speed Management

- Initial game speed: 0.1 seconds per frame
- Speed multiplier on paddle hit: 0.9 (reduces frame time by 10%)
- Maximum speed: Increases indefinitely as long as the rally continues
- Speed reset: Returns to 0.1 after someone scores

## Tips for Players

1. **Anticipate the Ball**: Watch the ball's trajectory and position your paddle ahead of time
2. **Center Your Paddle**: Keep your paddle near the center for better reaction time
3. **Use the Edges**: Sometimes hitting the ball at the paddle edge creates unpredictable angles
4. **Stay Focused**: As the game speeds up, concentration becomes crucial
5. **Practice**: The difficulty ramps up quickly, so multiple playthroughs improve skill

## Possible Enhancements

- Add difficulty levels or game modes
- Implement AI for single-player mode
- Add sound effects and background music
- Create a pause feature
- Add ball angle variation based on paddle hit location
- Track high scores
- Add power-ups
- Implement networked multiplayer

## Troubleshooting

**Paddles not moving?**
- Ensure the game window is active and focused
- Check that you're using the correct keys (Up/Down arrows and W/S)

**Ball not bouncing off paddle?**
- Make sure your paddle is positioned correctly to intercept the ball
- The ball must be within the detection radius (50 pixels) of the paddle center

**Game running too fast?**
- This is normal after several successful hits. Try to keep your reflexes sharp!
- You can adjust the initial speed value in main.py if desired

**Game window not appearing?**
- Ensure you have Python and Turtle graphics installed correctly
- Try running from a terminal to see any error messages


## License

This project is for educational purposes.

---

Enjoy playing Pong! Have fun and may the best player win! 🎮

