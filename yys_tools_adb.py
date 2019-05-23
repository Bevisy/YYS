import time
import random
import os
import aircv as ac
import pyautogui
import sys


class Tools(object):
    def __init__(self):
        self.SCREEN_X = 1024
        self.SCREEN_Y = 640
        os.system("adb kill-server && adb server && adb devices")

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
        cmd = "adb shell input touchscreen tap {0} {1}".format(rand_x, rand_y)
        os.system(cmd)
        self.log("click ({0}, {1})".format(rand_x, rand_y))

    def one_click(self, x, y):
        self.rand_click(x, y)

    # 重复单击某个给定的点（随机点击操作，范围为2）
    def loop_click(self, x, y, sleep_time=1):
        try:
            while True:
                self.rand_click(x, y)
                time.sleep(sleep_time)
        except KeyboardInterrupt:
            self.log("loop click exited!\n")

    # 识别图片src中的图片obj，并单击目标
    def ident_click(self, src, obj):
        try:
            image_src = ac.imread(src)
            image_obj = ac.imread(obj)
            position = ac.find_template(image_src, image_obj)
            if position['result'] is None:
                self.log("{0} isn't found in {1}".format(image_obj, image_src))
            else:
                center = list(position['result'])
                center_x = int(center[0])
                center_y = int(center[1])
                self.rand_click(center_x, center_y)
        except KeyboardInterrupt:
            self.log("identification click exited!\n")

    # 判断图片obj在图片src中是否存在
    @staticmethod
    def is_exists(src, obj):
        image_src = ac.imread(src)
        image_obj = ac.imread(obj)
        position = ac.find_template(image_src, image_obj)
        if position is None:
            return False
        else:
            # return tuple([int(position['result'][0]), int(position['result'][1])])
            return True

    # Android Simulator 截图并取回本地
    @staticmethod
    def screenshot_adb(img):
        cmd = "adb exec-out screencap -p > screen.png"
        os.system(cmd)
        # cmd1 = "adb shell screencap -p sdcard/{0}".format(img)
        # cmd2 = "adb pull sdcard/{0}".format(img)
        # os.system(cmd1)
        # time.sleep(0.1)
        # os.system(cmd2)

    # 屏幕截图
    @staticmethod
    def screenshot(img):
        pyautogui.screenshot(img)

    def yaoqi(self):
        try:
            while True:
                time.sleep(2)
                self.screenshot_adb("screen.png")
                if self.is_exists("screen.png", "images/zudui.png"):
                    self.ident_click("screen.png", "images/zudui.png")
                    self.log("zudui")
                    time.sleep(0.1)
                elif self.is_exists("screen.png", "images/zidongpipei.png"):
                    if self.is_exists("screen.png", "images/pipeizhong.png"):
                        time.sleep(5)
                        self.log("pipeizhong")
                    else:
                        self.ident_click("screen.png", "images/zidongpipei.png")
                        time.sleep(0.1)
                        self.log("zidongpipei")
                elif self.is_exists("screen.png", "images/zhunbei.png"):
                    self.ident_click("screen.png", "images/zhunbei.png")
                    time.sleep(0.1)
                    self.log("zhunbei")
                elif self.is_exists("screen.png", "images/jiesuan.png"):
                    self.ident_click("screen.png", "images/jiesuan.png")
                    time.sleep(0.1)
                    self.log("jiesuan")
                else:
                    time.sleep(3)
                    self.log("continue...")
        except KeyboardInterrupt:
            self.log("Exited!")

if __name__ == "__main__":
    op = Tools()
    # op.loop_click(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    op.yaoqi()