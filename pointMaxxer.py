print("hi")

# figure out how to make daily set more consistent bc too unreliable
import time
import random
import pyautogui
import keyboard
time.sleep(5)  # gives you 3 seconds to switch to the desired window
SCALE = 1.5  # e.g., 150% scaling on Windows

def scaled_move_to(x, y):
    pyautogui.moveTo(int(x * SCALE), int(y * SCALE))

def scaled_click(x, y):
    pyautogui.click(int(x * SCALE), int(y * SCALE))

#1150, 65
scaled_move_to(567, 389)

for i in range(35) :
    scaled_click(135, 62)
    a = random.randint(1, 1000000000)
    print(a)

    pyautogui.write(str(a) + " this is for microsoft reward points", interval=0.05)

    time.sleep(3)

    pyautogui.press("enter")

scaled_click(140, 60)

time.sleep(1)
pyautogui.write("https://rewards.bing.com/", interval=0.05)
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
scaled_click(100, 4)
time.sleep(1)

scaled_move_to(150, 570)
print("a")
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
