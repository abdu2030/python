import threading
import winsound

def _play(freq, duration):
    """Play a beep asynchronously so the game loop never stalls."""
    def beep():
        try:
            winsound.Beep(freq, duration)
        except Exception:
            pass
    threading.Thread(target=beep, daemon=True).start()

def play_paddle_hit():
    """Short high click when ball hits a paddle."""
    _play(700, 55)

def play_wall_bounce():
    """Softer mid-tone when ball bounces off the top/bottom wall."""
    _play(450, 45)

def play_score():
    """Descending two-note sound when a point is scored."""
    def tune():
        try:
            winsound.Beep(500, 120)
            winsound.Beep(300, 180)
        except Exception:
            pass
    threading.Thread(target=tune, daemon=True).start()

def play_win():
    """Ascending fanfare melody when a player wins the match."""
    def tune():
        try:
            for freq in [523, 659, 784, 1047]:
                winsound.Beep(freq, 130)
        except Exception:
            pass
    threading.Thread(target=tune, daemon=True).start()
