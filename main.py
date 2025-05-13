from PIL import Image
import pyautogui
import time
import keyboard

def is_obstacle_present():
    screenshot = pyautogui.screenshot()
    image = screenshot.convert("L")
    left, top, right, bottom = 220, 520, 300, 580

    for x in range(left, right):
        for y in range(top, bottom):
            pixel_value = image.getpixel((x, y))
            print(f"Pixel at ({x}, {y}): {pixel_value}")  # Debug output
            if pixel_value < 100:  # Threshold for dark objects
                screenshot.save("debug_screenshot.png")
                return True
    return False

# Main loop
time.sleep(3)  # Switch to game window
pyautogui.press("space")  # Start game

while not keyboard.is_pressed("q"):
    if is_obstacle_present():
        pyautogui.press("space")
        time.sleep(0.1)
    time.sleep(0.005)