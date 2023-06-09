from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")


def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

Label(master, font=("Arial", 30), text="Digital Clock", fg="black", bg="white", ).pack()
clock = Label(master, font=("Arial", 100), bg="white", fg="black")
clock.pack()

get_time()

master.mainloop()
