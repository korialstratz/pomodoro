from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    reps = 0
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    count = 0
    if reps % 2 == 1:
        count = WORK_MIN * 60
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        timer_label.config(text="BREAK", fg=PINK)

    count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    count_text = f"{count_min}:{count_sec}"
    # for reaching canvas item
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        # waits for given milliseconds and calls the function
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()
        check = ""
        for _ in range(math.floor(reps/2)):
            check += "✔"
        check_label.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthicknes=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 127, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(fg=GREEN, bg=YELLOW, text="TIMER", font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

stop_button = Button(text="Stop", command=reset_timer)
stop_button.grid(column=2, row=3)

check_label = Label(fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_label.grid(column=1, row=4)

window.mainloop()
