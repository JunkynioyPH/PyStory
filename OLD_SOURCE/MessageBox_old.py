from tkinter import *
from tkinter import ttk


# find a way to open up an image without stalling the main CMD, perhaps threading.
# so that stuff can happen simultaneously while still being associated witht he main CMD
# but for this one, i have the option to have it stall the main CMD or not. perhaps a threaded/non-threaded popup.
#
# Works on linux, but planned PyQT replacement is inevitable.
#
def MsgBox(wTitle, Subtitle, Message, Button="OK", Duration=120):
    
    root = Tk()

    # root.resizable(False,False)
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    

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
        Length = int(Duration) * 1000
        root.after(Length, Close)

    lb(Title, text=f"{Subtitle:<55}", wraplength=300).grid(column=2, row=1,sticky=(N,E,W,S))
    lb(SubTitle, text=Message, wraplength=300).grid(column=1, row=1,sticky=(N,E,W,S))
    btn(mframe, text=f"\n{Button}\n",command=Close).grid(column=1,row=3,sticky=(N,S,E,W))

    root.eval("tk::PlaceWindow . center") # windows only

    CloseTimer()
    root.mainloop()
