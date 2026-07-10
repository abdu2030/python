import math
import os
import customtkinter as ctk
from PIL import Image
import sound_manager

# ----------------------------- CONSTANTS ---------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

COLOR_WORK    = "#2ecc71"   # green
COLOR_SHORT   = "#e91e8c"   # pink
COLOR_LONG    = "#e74c3c"   # red
COLOR_IDLE    = "gray"

FONT_TIMER  = ("Courier", 44, "bold")
FONT_TITLE  = ("Courier", 28, "bold")
FONT_CHECKS = ("Courier", 18)

current_dir = os.path.dirname(os.path.abspath(__file__))
TOMATO_PATH = os.path.join(current_dir, "tomato.png")

# ----------------------------- APP SETUP ---------------------------------- #
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Pomodoro Timer")
app.resizable(False, False)

# Center window
app.update_idletasks()
W, H = 480, 640
x = (app.winfo_screenwidth()  // 2) - (W // 2)
y = (app.winfo_screenheight() // 2) - (H // 2)
app.geometry(f"{W}x{H}+{x}+{y}")

# ----------------------------- STATE ------------------------------------- #
reps       = 0
timer_id   = None    # holds the .after() ID
is_running = False
is_paused  = False
remaining  = 0       # seconds left in the current countdown

# Custom durations (will be updated by sliders in a later commit)
work_min        = WORK_MIN
short_break_min = SHORT_BREAK_MIN
long_break_min  = LONG_BREAK_MIN

# ----------------------------- HELPERS ------------------------------------ #
def fmt_time(total_sec):
    m = math.floor(total_sec / 60)
    s = total_sec % 60
    return f"{m:02d}:{s:02d}"

def get_session_label():
    if reps % 8 == 0 and reps > 0:
        return "Long Break", COLOR_LONG
    elif reps % 2 == 0 and reps > 0:
        return "Short Break", COLOR_SHORT
    else:
        return "Work", COLOR_WORK

def update_checkmarks():
    completed_sessions = reps // 2
    checks_label.configure(text="✔ " * completed_sessions)

# ----------------------------- COUNTDOWN ---------------------------------- #
def count_down():
    """Recursive 1-second countdown using .after(). Stores timer_id for cancellation."""
    global timer_id, remaining, is_running

    timer_text.configure(text=fmt_time(remaining))

    if remaining > 0:
        remaining -= 1
        timer_id = app.after(1000, count_down)
    else:
        # Session finished — disable controls until next rep starts
        is_running = False
        pause_btn.configure(state="disabled", text="Pause")
        sound_manager.play_session_end()
        update_checkmarks()
        start_next_session()

def start_next_session():
    """Automatically advance to the next Pomodoro rep."""
    global reps
    reps += 1
    _begin_countdown()

def _begin_countdown():
    """Set up remaining seconds and kick off count_down for the current rep."""
    global remaining, is_running, timer_id
    label, color = get_session_label()
    session_title.configure(text=label, text_color=color)

    if reps % 8 == 0 and reps > 0:
        remaining = long_break_min * 60
    elif reps % 2 == 0 and reps > 0:
        remaining = short_break_min * 60
    else:
        remaining = work_min * 60

    is_running = True
    pause_btn.configure(state="normal")
    # Lock duration sliders while session is active
    _set_sliders_state("disabled")
    count_down()

# ----------------------------- CONTROLS ----------------------------------- #
def on_start():
    """Start the timer (only if not already running)."""
    global reps, is_running, is_paused
    sound_manager.play_button_click()
    if is_running or is_paused:
        return
    reps += 1
    start_btn.configure(text="Running…", state="disabled")
    pause_btn.configure(state="normal")
    _begin_countdown()

def on_reset():
    """Cancel any active timer and fully reset state."""
    global reps, timer_id, is_running, is_paused, remaining
    sound_manager.play_button_click()
    if timer_id:
        app.after_cancel(timer_id)
        timer_id = None
    reps       = 0
    is_running = False
    is_paused  = False
    remaining  = 0
    timer_text.configure(text="00:00")
    session_title.configure(text="Timer", text_color=COLOR_IDLE)
    checks_label.configure(text="")
    # Restore Start to clickable; Pause must stay disabled until a session starts
    start_btn.configure(text="Start", state="normal")
    pause_btn.configure(text="Pause", state="disabled")
    # Unlock duration sliders when timer is reset
    _set_sliders_state("normal")

def on_pause_resume():
    """Pause a running countdown or resume a paused one."""
    global timer_id, is_running, is_paused
    sound_manager.play_button_click()
    if is_running and not is_paused:
        # Pause
        if timer_id:
            app.after_cancel(timer_id)
            timer_id = None
        is_running = False
        is_paused  = True
        pause_btn.configure(text="Resume")
        start_btn.configure(text="Paused", state="disabled")
    elif is_paused:
        # Resume
        is_paused  = False
        is_running = True
        pause_btn.configure(text="Pause")
        start_btn.configure(text="Running…", state="disabled")
        count_down()

# ----------------------------- UI LAYOUT ---------------------------------- #

# --- Header ---
header_frame = ctk.CTkFrame(app, fg_color="transparent")
header_frame.pack(fill="x", padx=30, pady=(20, 0))

session_title = ctk.CTkLabel(
    header_frame,
    text="Timer",
    font=ctk.CTkFont(family="Courier", size=28, weight="bold"),
    text_color=COLOR_IDLE,
)
session_title.pack()

# --- Tomato canvas area ---
canvas_frame = ctk.CTkFrame(app, fg_color="transparent")
canvas_frame.pack(pady=10)

try:
    tomato_img = ctk.CTkImage(
        light_image=Image.open(TOMATO_PATH),
        dark_image=Image.open(TOMATO_PATH),
        size=(200, 224),
    )
    tomato_label = ctk.CTkLabel(canvas_frame, image=tomato_img, text="")
    tomato_label.pack()
except Exception:
    tomato_label = ctk.CTkLabel(canvas_frame, text="🍅", font=ctk.CTkFont(size=80))
    tomato_label.pack()

timer_text = ctk.CTkLabel(
    canvas_frame,
    text="00:00",
    font=ctk.CTkFont(family="Courier", size=44, weight="bold"),
    text_color="white",
)
timer_text.place(relx=0.5, rely=0.62, anchor="center")

# --- Check marks ---
checks_label = ctk.CTkLabel(
    app,
    text="",
    font=ctk.CTkFont(family="Courier", size=18),
    text_color=COLOR_WORK,
)
checks_label.pack(pady=(0, 5))

# --- Buttons ---
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=10)
btn_frame.grid_columnconfigure((0, 1, 2), weight=1)

start_btn = ctk.CTkButton(
    btn_frame, text="Start", width=120, height=38,
    fg_color=COLOR_WORK, hover_color="#27ae60",
    command=on_start,
)
start_btn.grid(row=0, column=0, padx=12, pady=6)

pause_btn = ctk.CTkButton(
    btn_frame, text="Pause", width=120, height=38,
    state="disabled",
    command=on_pause_resume,
)
pause_btn.grid(row=0, column=1, padx=12, pady=6)

reset_btn = ctk.CTkButton(
    btn_frame, text="Reset", width=120, height=38,
    fg_color="#e74c3c", hover_color="#c0392b",
    command=on_reset,
)
reset_btn.grid(row=0, column=2, padx=12, pady=6)

# ----------------------------- SETTINGS PANEL ---------------------------- #

def _set_sliders_state(state: str):
    """Enable or disable all duration sliders ('normal' or 'disabled')."""
    work_slider.configure(state=state)
    short_slider.configure(state=state)
    long_slider.configure(state=state)

def on_work_slider(value):
    global work_min
    work_min = int(value)
    work_val_label.configure(text=f"{work_min} min")

def on_short_slider(value):
    global short_break_min
    short_break_min = int(value)
    short_val_label.configure(text=f"{short_break_min} min")

def on_long_slider(value):
    global long_break_min
    long_break_min = int(value)
    long_val_label.configure(text=f"{long_break_min} min")

# Slider state helper — defined early so both _begin_countdown and on_reset can
# call it; actual slider widgets are captured in the list below after creation.
_slider_widgets: list = []  # filled once sliders are built

def _set_sliders_state(state: str):
    """Enable or disable all duration sliders ('normal' or 'disabled')."""
    for s in _slider_widgets:
        s.configure(state=state)


settings_frame = ctk.CTkFrame(app)
settings_frame.pack(fill="x", padx=30, pady=(5, 15))

settings_title = ctk.CTkLabel(
    settings_frame,
    text="Session Durations",
    font=ctk.CTkFont(size=14, weight="bold"),
)
settings_title.pack(pady=(10, 4))

def _make_slider_row(parent, label_text, from_, to, default, cmd):
    """Helper to create a labelled slider row; returns (slider, value_label)."""
    row = ctk.CTkFrame(parent, fg_color="transparent")
    row.pack(fill="x", padx=15, pady=4)
    row.grid_columnconfigure(1, weight=1)

    lbl = ctk.CTkLabel(row, text=label_text, width=100, anchor="w",
                        font=ctk.CTkFont(size=12))
    lbl.grid(row=0, column=0, sticky="w")

    slider = ctk.CTkSlider(row, from_=from_, to=to,
                            number_of_steps=to - from_,
                            command=cmd)
    slider.set(default)
    slider.grid(row=0, column=1, sticky="ew", padx=8)

    val_lbl = ctk.CTkLabel(row, text=f"{default} min", width=50, anchor="e",
                            font=ctk.CTkFont(size=12))
    val_lbl.grid(row=0, column=2, sticky="e")
    return slider, val_lbl

work_slider,  work_val_label  = _make_slider_row(
    settings_frame, "🍅 Work",        10, 60, WORK_MIN,        on_work_slider)
short_slider, short_val_label = _make_slider_row(
    settings_frame, "☕ Short Break",  1, 15, SHORT_BREAK_MIN,  on_short_slider)
long_slider,  long_val_label  = _make_slider_row(
    settings_frame, "🛌 Long Break",   5, 45, LONG_BREAK_MIN,   on_long_slider)

# Register sliders so _set_sliders_state can reach them
_slider_widgets.extend([work_slider, short_slider, long_slider])

# Appearance mode toggle
appearance_row = ctk.CTkFrame(settings_frame, fg_color="transparent")
appearance_row.pack(fill="x", padx=15, pady=(6, 10))

ctk.CTkLabel(appearance_row, text="Appearance:",
             font=ctk.CTkFont(size=12)).pack(side="left")
ctk.CTkOptionMenu(
    appearance_row,
    values=["System", "Dark", "Light"],
    command=ctk.set_appearance_mode,
    width=110,
).pack(side="right")


app.mainloop()
