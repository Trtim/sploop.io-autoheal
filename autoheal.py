
import time, keyboard


# Settings #

boostspike = True # change to True if u want a boost spike macro
bind = 't' # boostspike macro keybind
d = 0.035 # Delay for autoheal


def press(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)
    return

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
    if boostspike == True:
        if keyboard.is_pressed(bind):
            press('f', 0.001)
            press('space', 0.001)
            press('shift', 0.4)
            press('space', 0.001)
            press('shift', 0.3)
            press('space', 0.001)
            press('1', 0.001)
            time.sleep(0)

