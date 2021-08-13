
import time, keyboard


# Settings #

autotrap = False # change to true if u want to use
bind = 't' #Auto trap/boost keybind
d = 0.05 #Delay for each heal/placement




def press(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)

autoheal = False

while True:
    if keyboard.is_pressed('`'):
        autoheal = not autoheal
        while keyboard.is_pressed('`'):
                time.sleep(0)
    if autoheal == True:
            press('space', d)
            press('q', d)
            press('space', d)
            press('1', d)
    if autotrap == True:
        if keyboard.is_pressed(bind):
            press('f', d)
            press('space', d)

