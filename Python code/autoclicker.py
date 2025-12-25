import pyautogui
import keyboard
import time
x=1625
y=237
a=1
while a==0:
    keyboard.press('space')  # Press the space bar 
    time.sleep(1)
    keyboard.release('space')  # Release the space bar
    time.sleep(1)  # Adjust the delay as needed
    if keyboard.is_pressed('q'):
        a=5
while a==1:
    time.sleep(0.1)  # Adjust the delay as needed
    pyautogui.click()
    if keyboard.is_pressed('q'):
        a=6
print(a)