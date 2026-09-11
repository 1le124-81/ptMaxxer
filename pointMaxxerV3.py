#made it so it aligned with daily poll. very brute forcy. I was thinking of using pytesseract text recognition but works for now.
print("code starting")

import time
import random
import pyautogui

import subprocess

shutdown_after = input("Shut down computer when finished? (y/n): ").strip().lower() == "y" # asks if u wanna shutdown computer after

time.sleep(5)  # gives you 5 seconds  to switch to the desired window
SCALE = 1.5  # default 150% bc that's what i have on my comp 150% scaling on Windows

# makes the move_to scaled for easier configuration (ive been using the script cursorCoords.py for coordinates)
def scaled_move_to(x, y):
    pyautogui.moveTo(int(x * SCALE), int(y * SCALE))

def scaled_click(x, y):
    pyautogui.click(int(x * SCALE), int(y * SCALE))

scaled_move_to(567, 389) # where the search bar is on my computer

# searches up somethign different 20 times (20*5 = 100 pts, max pts from search daily is 100.)
# 5 second wait bc there's a cooldown to how fast u can search stuff up
for i in range(20) :
    scaled_click(135, 62)
    a = random.randint(1, 1000000000)
    print(a)

    pyautogui.write(str(a) + " this is for microsoft reward points", interval=0.05)

    pyautogui.press("enter")

    time.sleep(5)

scaled_click(140, 60) # click back on search bar

time.sleep(1)
pyautogui.write("https://rewards.bing.com/dashboard", interval=0.05) # go to ms rewards website
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)

def dailySet():
    # daily set sytem
    scaled_move_to(900, 570)
    print("daily set initalized")
    while True:
        x, y = pyautogui.position()

        r, g, b = pyautogui.pixel(x,y)
        print(f"({r}, {g}, {b})")
        
        pyautogui.scroll(-10)
        
        if b > r + 150 and b > g + 100: #detects blue color of speech bubbles in daily set
            print("blue detected, exiting loop.")
            break
        
dailySet()

print("clickign elemenents")
time.sleep(2)
scaled_click(350, 600)
time.sleep(1)
scaled_click(100, 4)
time.sleep(1)
scaled_click(775, 600)
time.sleep(1)
scaled_click(100, 4)
time.sleep(1)
scaled_click(1000, 600)

scaled_move_to(191, 583)


if shutdown_after:
    print("Turning off monitor...")
    subprocess.run([ # shuts down monitor using ControlMyMonitor.exe
        r"C:\Users\lukes\OneDrive\Desktop\controlmymonitor\ControlMyMonitor.exe",
        "/SetValue",
        r"\\.\DISPLAY2\Monitor0",
        "D6",
        "5"
    ])

    time.sleep(5)

    print("Shutting down...")
    subprocess.run([ # shuts down computer using powershell
        "powershell",
        "-Command",
        "Stop-Computer"
    ])
