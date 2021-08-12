
import time, keyboard

autoheal = False
chat = False
d = 0.0001

def press(a, b):
    keyboard.press(a)
    time.sleep(b)
    keyboard.release(a)
    return

while True:
    if keyboard.is_pressed('enter'):
        chat = not chat
    if chat == False:
        if keyboard.is_pressed('t'):
            autoheal = not autoheal
            while keyboard.is_pressed('t'):
                    time.sleep(0)
        if autoheal == True:
                press('space', d)
                press('3', d)
                press('space', d)
                press('1', d)

