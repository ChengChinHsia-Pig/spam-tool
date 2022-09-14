import pyautogui
import time
import math
times = input("騷擾次數:")
interval = input("間隔時間(整數):")

print("Starting...")
time.sleep(3)
for i in range(int(times)):
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
    time.sleep(int(interval))
