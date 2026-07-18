print("hi, the code is starting")

import time
import random
import pyautogui

time.sleep(5)  # gives you 5 seconds to switch to the desired window
SCALE = 1.5  # default 150% bc that's what i have on my comp 150% scaling on Windows

# makes the move_to scaled for easier configuration (ive been using the script cursorCoords.py for coordinates)
def scaled_move_to(x, y):
    pyautogui.moveTo(int(x * SCALE), int(y * SCALE))

def scaled_click(x, y):
    pyautogui.click(int(x * SCALE), int(y * SCALE))

scaled_move_to(567, 389) # where the search bar is on my computer

# searches up somethign different 35 times (35*5 = 175 pts, max pts from search daily is 150.)
# 5 second wait bc there's a cooldown to how fast u can search stuff up
for i in range(35) :
    scaled_click(135, 62)
    a = random.randint(1, 1000000000)
    print(a)

    pyautogui.write(str(a) + " this is for microsoft reward points", interval=0.05)

    time.sleep(5)

    pyautogui.press("enter")

scaled_click(140, 60) # click back on search bar

time.sleep(1)
pyautogui.write("https://rewards.bing.com/", interval=0.05) # go to ms rewards website
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
scaled_click(100, 4)
time.sleep(1)

# daily set sytem
scaled_move_to(150, 570)
print("daily set initalized")
while True:
    x, y = pyautogui.position()
    screen_w, screen_h = pyautogui.size()

    x = max(0, min(x, screen_w - 1))
    y = max(0, min(y, screen_h - 1))

    r, g, b = pyautogui.pixel(x,y )
    print(f"({r}, {g}, {b})")
    
    pyautogui.scroll(-10)
    
    if r == 16 and g == 124 and b == 16:
        print("green detected, exiting loop.")
        break
# clicks the 3 daily set elements
time.sleep(2)
scaled_click(350, 630)
time.sleep(1)
scaled_click(100, 4)
time.sleep(1)
scaled_click(775, 630)
time.sleep(1)
scaled_click(100, 4)
time.sleep(1)
scaled_click(1000, 630)
