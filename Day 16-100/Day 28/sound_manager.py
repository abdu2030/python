import threading
import winsound

def play_async(freq, duration):
    """Run winsound Beep inside a background thread so the GUI does not freeze."""
    def beep():
        try:
            winsound.Beep(freq, duration)
        except Exception:
            pass
    threading.Thread(target=beep, daemon=True).start()

def play_session_end():
    """Alarm sound when a work or break session finishes."""
    def play_tune():
        try:
            # Classic retro alarm sequence
            for _ in range(3):
                winsound.Beep(880, 150)
                winsound.Beep(1100, 150)
        except Exception:
            pass
    threading.Thread(target=play_tune, daemon=True).start()

def play_button_click():
    """Short click sound when buttons are clicked."""
    play_async(600, 45)
