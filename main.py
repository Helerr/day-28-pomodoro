import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS, timer
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    timer_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global REPS, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = range(math.floor(REPS/2))
        for _ in work_sessions:
            mark += "✔"
        checkmarks_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")
window.eval('tk::PlaceWindow . center')

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), background=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

checkmarks_label = Label(fg=GREEN, text="", font=(FONT_NAME, 24, "bold"), background=YELLOW)
checkmarks_label.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
