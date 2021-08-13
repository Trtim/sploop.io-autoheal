
import time, keyboard

autoheal = False
d = 0.05

def press(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)
    

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

