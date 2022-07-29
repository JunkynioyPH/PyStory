import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.title(sys.argv[1])
root.resizable(False,False)

mframe = ttk.Frame(root, relief=SUNKEN, borderwidth=10)
mframe.grid(column=1, row=1, sticky=(N, S, E, W))

Title = ttk.Frame(mframe, relief=RAISED, borderwidth=10)
Title.grid(column=1, row=1, sticky=(N, S, E, W))

SubTitle = ttk.Frame(mframe, relief=SUNKEN, borderwidth=25)
SubTitle.grid(column=1, row=2, sticky=(N, S, E, W))

btn = ttk.Button
lb = ttk.Label

def Close():
    root.destroy()

def CloseTimer():
    try:
        Duration = int(sys.argv[4]) * 1000
        root.after(Duration, Close)
    except:
        print("fucked")

MESSAGE = sys.argv[3]

lb(Title, text=f"{sys.argv[2]}                                                       ", wraplength=300).grid(column=2, row=1,sticky=(N,E,W,S))
lb(SubTitle, text=MESSAGE, wraplength=300).grid(column=1, row=1,sticky=(N,E,W,S))
btn(mframe, text=f"\n{sys.argv[5]}\n",command=Close).grid(column=1,row=3,sticky=(N,S,E,W))

root.eval("tk::PlaceWindow . center")

CloseTimer()
root.mainloop()
