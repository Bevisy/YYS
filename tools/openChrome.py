import time
import pyautogui
import sys

def openChrome(chromeX, chromeY):
    pyautogui.click(chromeX, chromeY)


def closeChrome(chromeX, chromeY):
    pyautogui.click(chromeX, chromeY)


if __name__ == "__main__":
    openChrome(404, 15)
    time.sleep(3)
    closeChrome(230, 45)
    time.sleep(1)
