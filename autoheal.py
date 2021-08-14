
import time, keyboard


# Settings #

autotrap = False # change to true if u want to use autotrap/boost
bind = 't' # autotrap/boost keybind
d = 0.035 # Delay for autoheal


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
            time.sleep(0)
    if autotrap == True:
        if keyboard.is_pressed(bind):
            press('f', 0.001)
            press('space', 0.001)
            press('1', 0.001)
