import threading
import winsound

def play_sound_async(freq, duration):
    """Executes winsound.Beep inside a daemon thread to prevent game freezes."""
    def beep():
        try:
            winsound.Beep(freq, duration)
        except Exception:
            pass  # Fallback if audio device is unavailable
    threading.Thread(target=beep, daemon=True).start()

def play_move():
    """Short click sound when moving."""
    play_sound_async(500, 40)

def play_level_up():
    """Ascending melodic sequence on level completion."""
    def melody():
        try:
            winsound.Beep(523, 100)  # C5
            winsound.Beep(659, 100)  # E5
            winsound.Beep(784, 100)  # G5
            winsound.Beep(1047, 180) # C6
        except Exception:
            pass
    threading.Thread(target=melody, daemon=True).start()

def play_crash():
    """Descending buzz sound when losing a life."""
    def melody():
        try:
            winsound.Beep(250, 150)
            winsound.Beep(120, 250)
        except Exception:
            pass
    threading.Thread(target=melody, daemon=True).start()

def play_powerup():
    """Cheerful arcade chime when picking up items."""
    def melody():
        try:
            winsound.Beep(880, 80)
            winsound.Beep(1320, 150)
        except Exception:
            pass
    threading.Thread(target=melody, daemon=True).start()
