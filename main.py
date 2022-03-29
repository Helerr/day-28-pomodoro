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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")
window.eval('tk::PlaceWindow . center')

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), background=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

checkmarks_label = Label(fg=GREEN, text="✔", font=(FONT_NAME, 24, "bold"), background=YELLOW)
checkmarks_label.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

window.mainloop()
