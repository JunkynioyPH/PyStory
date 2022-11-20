from tkinter import *
from tkinter import ttk
import pyautogui as pag
root = Tk()
lb = ttk.Label
MousePos = StringVar()

root.resizable(False,False)

header = ttk.Frame(root, relief=RAISED, borderwidth=4)
header.grid(column=0, row=0, sticky=(N, S,W, E))

headercenter = ttk.Frame(root)
headercenter.grid(padx=5, pady=8, column=0, row=0, sticky=(N, S))

headercontent = ttk.Frame(headercenter, relief=SUNKEN, borderwidth=2)
headercontent.grid(column=0, row=0, sticky=N)

lb(headercontent, textvariable=MousePos).grid(column=1, row=1,sticky=(N,S))

def live_update():
    try:
        x, y = pag.position()
        MousePos.set(f"Current MousePos - X: {x}  Y: {y}")
        root.title(f"Pos")
        root.after(50, live_update)
    except Exception as Err:
        print("live_update()",Err)

live_update()
root.mainloop()