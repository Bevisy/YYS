import time
import pyautogui
import cv2
import random


class Tools(object):
    def __init__(self):
        pass

    @staticmethod
    # show current time
    def current_time():
        # time format: May 08 01:58:45
        return time.strftime("%b %d %H:%M:%S", time.localtime())

    # log output
    def log(self, message):
        print(self.current_time() + " - " + message)

    @staticmethod
    def rand_click(dx, dy, random_range=5):
        rand_x = random.randint(0, random_range)
        rand_y = random.randint(0, random_range)
        pyautogui.click(dx + rand_x, dy + rand_y)

    def loop_click(self, dx, dy, sleep_time=1):
        try:
            while True:
                self.rand_click(dx, dy)
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            self.log("loop click exited!\n")


pyautogui.FAILSAFE = True  # 默认为 False
pyautogui.PAUSE = 0.5  # 默认为 0.1s

if __name__ == "__main__":
    op = Tools()
    op.log("hello")
