import pyautogui as pag
import pygetwindow as pgw
import random, time
###################
# FOCUS IS CALLED "Activate"
# Activate, isActive, getActiveWindow
###################

name = 'Pos'

while True:
    try:
        # it will litterally look for a window that has this name, yes even browser tabs
        window = pgw.getWindowsWithTitle(f'{name}')[0]
        window.activate()
        print(f">>> Found '{name}' window!")
        # print(f"{window.size} - TopLeft_{window.topleft}")
        break
    except Exception as ERR:
        print(f">>> Either '{name}' window is not found or ERROR : '{ERR}' <<<")
        print('>>> Retrying in 3s...')
        time.sleep(3)
###
iterations = 5
screenWidth, screenHeight = pag.size()
try:
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
except Exception as ERR:
    print(f"ERR : {ERR}")
    time.sleep(3)