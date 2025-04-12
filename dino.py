import pyautogui
import time
from PIL import ImageGrab, Image
import keyboard

import cv2
import numpy as np


# def detect_obstacle():
#     # منطقه‌ای از صفحه که می‌خواهیم بررسی کنیم (ممکن است نیاز به تنظیم داشته باشد)
#     region = (400, 400, 500, 450)  # مثال: x1, y1, x2, y2
#
#     # تصویر منطقه را بگیر
#     screenshot = ImageGrab.grab(region)
#
#     # بررسی پیکسل‌ها برای تشخیص مانع
#     for x in range(0, screenshot.width, 5):
#         for y in range(0, screenshot.height, 5):
#             pixel = screenshot.getpixel((x, y))
#             # اگر رنگ پیکسل سیاه یا نزدیک به سیاه باشد (مانع)
#             if pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
#                 return True
#     return False


def detect_obstacle():
    currentMouseX, currentMouseY = pyautogui.position()
    screenshot = np.array(ImageGrab.grab(bbox=(currentMouseX, currentMouseY, currentMouseX+10, currentMouseY+10)))
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    print(screenshot)
    # اگر لبه‌های زیادی تشخیص داده شد، احتمالاً مانع وجود دارد
    if np.sum(edges) > 1000:
        return True
    return False


def jump():
    pyautogui.press('space')
    print("Jump!")


def duck():
    pyautogui.keyDown('down')
    time.sleep(0.5)
    pyautogui.keyUp('down')
    print("Duck!")


def main():
    print("Starting Dino bot in 3 seconds...")
    time.sleep(3)

    # ابتدا بازی را شروع کنیم
    pyautogui.press('space')

    try:
        while True:
            if detect_obstacle():
                jump()
                # برای پرندگان ممکن است نیاز به duck() باشد
                time.sleep(0.1)  # تأخیر کوچک برای جلوگیری از پرش‌های متوالی

            # برای توقف اسکریپت با فشار دادن 'q'
            if keyboard.is_pressed('q'):
                print("Stopping bot...")
                break

    except KeyboardInterrupt:
        print("Bot stopped by user")


if __name__ == "__main__":
    main()
