from tkinter import *
from tkinter import ttk
import pyautogui as pag


# find a way to open up an image without stalling the main CMD, perhaps threading.
# so that stuff can happen simultaneously while still being associated witht he main CMD
def ImgBox(Identifier, Image, Duration=15):
    
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
        root.attributes('-transparentcolor','#f0f0f0')
        container = ttk.Frame(root, borderwidth=0)
        container.grid(column=0, row=0, sticky=(N, S, E, W))
        
        # Somehow, this broke the image render and now i need to set root.geometry() to render properly.
        # it was meant to remove the gap at the left of the screen
        container.place(x=-2) 
        
        canvas = Canvas(container, width=screenWidth, height=screenHeight)
        canvas.pack()
        img = PhotoImage(file=Image)
        canvas.create_image(0, 0, image=img, anchor=NW)
    except Exception as ERR:
        mframe = ttk.Frame(root, borderwidth=2)
        mframe.grid(column=1, row=1, sticky=(N, S, E, W), padx=int(screenWidth*0.1), pady=int(screenHeight*0.1))
        lb(mframe, text=f"Error: {ERR}", bg="#faa", font=("Tahoma", int(screenWidth*0.01))).grid(column=1, row=1, sticky=(N, S, E, W))

    CloseTimer()
    root.mainloop()