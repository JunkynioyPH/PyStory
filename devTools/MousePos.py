from tkinter import *
from tkinter import ttk
import pyautogui as pag
import pygetwindow as pgw
import time

root = Tk()
lb = ttk.Label
MousePos, WindowPos = StringVar(), StringVar()
root.title(f"Pos")

root.resizable(False,False)

header = ttk.Frame(root, relief=RAISED, borderwidth=4)
header.grid(column=0, row=0, sticky=(N, S,W, E))

headercenter = ttk.Frame(root)
headercenter.grid(padx=5, pady=8, column=0, row=0, sticky=(N, S))

headercontent = ttk.Frame(headercenter, relief=SUNKEN, borderwidth=2)
headercontent.grid(column=0, row=0, sticky=N)

lb(headercontent, textvariable=MousePos).grid(column=1, row=1,sticky=(N,S))
lb(headercontent, textvariable=WindowPos).grid(column=1, row=2,sticky=(N,S))

def live_update():
    try:
        window = pgw.getWindowsWithTitle('Pos')[0]
        x1, y1 = pag.position()
        x2, y2 = window.topleft
        MousePos.set(f"Current MousePos - X: {x1}  Y: {y1}")
        WindowPos.set(f"WindowPos TopLeft - X: {x2} Y: {y2}")
        root.after(50, live_update)
    except Exception as Err:
        print("live_update()",Err)
        time.sleep(3)


root.after(1, live_update)
root.mainloop()