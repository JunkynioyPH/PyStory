import pyautogui as pag
import pygetwindow as pgw
import random, time
###################
# FOCUS IS CALLED "Activate"
# Activate, isActive, getActiveWindow
###################
time.sleep(2)
while True:
    try:
        # it will litterally look for a window that has this name, yes even browser tabs
        window = pgw.getWindowsWithTitle('Pos')[0]
        window.activate()
        # print(f"{window.size} - TopLeft_{window.topleft}")
        break
    except Exception as ERR:
        print(ERR)
        print('Retrying in 3s...')
        time.sleep(3)
###
iterations = 5
screenWidth, screenHeight = pag.size()
while iterations > 0:
    window.activate()
    x1, y1 = window.topleft
    x, y = x1 + 42, y1 + 15


    pag.moveTo(x,y,0.5,tween=pag.easeInOutSine, _pause=False)
    window.activate()
    pag.mouseDown()
    pag.moveTo(x-100,y-100,0.5,tween=pag.easeInOutSine, _pause=False)
    pag.mouseUp()

    print(iterations, f"POS:{x1}_{y1}")
    iterations -= 1 
    # time.sleep(1)