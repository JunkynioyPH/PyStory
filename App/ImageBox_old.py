from tkinter import *
from tkinter import ttk
import pyautogui as pag
from App.xpfpath import *


# find a way to open up an image without stalling the main CMD, perhaps threading.
# so that stuff can happen simultaneously while still being associated witht he main CMD

### An attempt to convert this into a class which allows for instancing
### Didnt work out as i am working on this literally [2:30am GMT+8]
### not in the right mindset for this
### Somehow got it to work but it spawns a blank TK window and when i test it it will display the image but also throw an
### error which ImgBox.Close() apparently expects 0 args, but 1 is given, which is confusing; then it softlocks and requires 10 CTRL+C to close
### Maybe because i dont know how "def __init__(self):" works properly
# class ImgBox:
#     global root, lb
#     root = Tk()
#     lb = Label
#     def __init__(self, Identifier: str, Image: str, Duration=15):
#         self.ID = Identifier
#         self.IMG = Image
#         self.DUR = Duration
#     def Close():
#         root.destroy()
#     def CloseTimer(self):
#         Length = int(self.DUR)
#         root.after(Length, self.Close)
#     def Show(self):
#         screenWidth, screenHeight = pag.size()
#         root.geometry(f"{screenWidth}x{screenHeight}")
#         root.overrideredirect(True)
#         root.title(self.ID + " ImageWindow")
#         try:
#             # set the actual window, WITHOUT IMAGE, transparency. Do not make images with #f0f0f0 color.
#             #it's not really transparency, it's just keying out #f0f0f0 only which is tkinter's default color.
#             root.attributes('-transparentcolor','#f0f0f0')
#             container = ttk.Frame(root, borderwidth=0)
#             container.grid(column=0, row=0, sticky=(N, S, E, W))
            
#             # it was meant to remove the gap at the left of the screen + root.geometry() must be set or else this will break
#             container.place(x=-2) 
            
#             canvas = Canvas(container, width=screenWidth, height=screenHeight)
#             canvas.pack()
#             img = PhotoImage(file=self.IMG)
#             canvas.create_image(0, 0, image=img, anchor=NW)
#         except Exception as ERR:
#             mframe = ttk.Frame(root, borderwidth=2)
#             mframe.grid(column=1, row=1, sticky=(N, S, E, W), padx=int(screenWidth*0.1), pady=int(screenHeight*0.1))
#             lb(mframe, text=f"Error: {ERR}", bg="#faa", font=("Tahoma", int(screenWidth*0.01))).grid(column=1, row=1, sticky=(N, S, E, W))
#         self.CloseTimer()
#         root.mainloop()
def ImgBox(Identifier, Image, Duration=5):
    
    root = Tk()
    screenWidth, screenHeight = pag.size()
    root.geometry(f"{screenWidth}x{screenHeight}")
    root.overrideredirect(True)
    root.title(Identifier + " ImageWindow")
    lb = Label
    
    def Close():
        root.destroy()

    def CloseTimer():
            Length = int(Duration) * 1000
            root.after(Length, Close)
    
    try:
        # set the actual window, WITHOUT IMAGE, transparency. Do not make images with #f0f0f0 color.
        #it's not really transparency, it's just keying out #f0f0f0 only which is tkinter's default color.
        
        ## Does not work on Linux... PyQT might fix this, planned switch and overhaul
        # root.attributes('-transparentcolor','#f0f0f0')
        container = ttk.Frame(root, borderwidth=0)
        container.grid(column=0, row=0, sticky=(N, S, E, W))
        
        # it was meant to remove the gap at the left of the screen + root.geometry() must be set or else this will break
        container.place(x=-2) 
        
        canvas = Canvas(container, width=screenWidth, height=screenHeight)
        canvas.pack()
        img = PhotoImage(file=xpfp(Image))
        canvas.create_image(0, 0, image=img, anchor=NW)
    except Exception as ERR:
        mframe = ttk.Frame(root, borderwidth=2)
        mframe.grid(column=1, row=1, sticky=(N, S, E, W), padx=int(screenWidth*0.1), pady=int(screenHeight*0.1))
        lb(mframe, text=f"Error: {ERR}", bg="#faa", font=("Tahoma", int(screenWidth*0.01))).grid(column=1, row=1, sticky=(N, S, E, W))

    CloseTimer()
    root.mainloop()