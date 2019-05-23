import time
import pyautogui
import random
import sys


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

    def rand_click(self, x, y, random_range=2):
        rand_x = x + random.randint(-random_range, random_range)
        rand_y = y + random.randint(-random_range, random_range)
        pyautogui.click(rand_x, rand_y)
        self.log("click ({0}, {1})".format(rand_x, rand_y))

    def one_click(self, x, y):
        self.rand_click(x, y)

    def loop_click(self, x, y, sleep_time=1):
        try:
            while True:
                self.rand_click(x, y)
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            self.log("loop click exited!\n")

    def ident_click(self, image_path):
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path)

            self.rand_click(x, y)
        except KeyboardInterrupt:
            self.log("identification click exited!\n")


pyautogui.FAILSAFE = True  # 默认为 False
pyautogui.PAUSE = 0.5  # 默认为 0.1s

if __name__ == "__main__":
    op = Tools()
    op.loop_click(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
