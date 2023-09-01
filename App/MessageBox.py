from tkinter import *
from tkinter import ttk

def MsgBox(wTitle, Subtitle, Message, Button="OK", Duration=120):
    
    root = Tk()

    root.resizable(False,False)

    mframe = ttk.Frame(root, relief=SUNKEN, borderwidth=10)
    mframe.grid(column=1, row=1, sticky=(N, S, E, W))

    Title = ttk.Frame(mframe, relief=RAISED, borderwidth=10)
    Title.grid(column=1, row=1, sticky=(N, S, E, W))

    SubTitle = ttk.Frame(mframe, relief=SUNKEN, borderwidth=25)
    SubTitle.grid(column=1, row=2, sticky=(N, S, E, W))

    btn = ttk.Button
    lb = ttk.Label

    root.title(wTitle)
    def Close():
        root.destroy()

    def CloseTimer():
        try:
            Length = int(Duration) * 1000
            root.after(Length, Close)
        except:
            print("fucked")

    lb(Title, text=f"{Subtitle:<55}", wraplength=300).grid(column=2, row=1,sticky=(N,E,W,S))
    lb(SubTitle, text=Message, wraplength=300).grid(column=1, row=1,sticky=(N,E,W,S))
    btn(mframe, text=f"\n{Button}\n",command=Close).grid(column=1,row=3,sticky=(N,S,E,W))

    root.eval("tk::PlaceWindow . center")

    CloseTimer()
    root.mainloop()
