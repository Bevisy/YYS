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
            self.log("Ctrl-C Exited.")

    # 识别图片src中的图片obj，并单击目标
    def ident_click(self, src, obj):
        try:
            image_src = ac.imread(src)
            image_obj = ac.imread(obj)
            position = ac.find_template(image_src, image_obj, threshold=0.8)
            if position['result'] is None:
                self.log("{0} isn't found in {1}".format(image_obj, image_src))
            else:
                center = list(position['result'])
                center_x = int(center[0])
                center_y = int(center[1])
                self.rand_click(center_x, center_y)
        except KeyboardInterrupt:
            self.log("Ctrl-C Exited.")

    # 判断图片obj在图片src中是否存在
    @staticmethod
    def is_exists(src, obj):
        image_src = ac.imread(src)
        image_obj = ac.imread(obj)
        position = ac.find_template(image_src, image_obj, threshold=0.8)
        if position is None:
            return False
        else:
            # return tuple([int(position['result'][0]), int(position['result'][1])])
            return True

    # Android Simulator 截图并取回本地
    @staticmethod
    def screenshot_adb(img):
        cmd = "adb exec-out screencap -p > {0}".format(img)
        os.system(cmd)

    # 屏幕截图
    @staticmethod
    def screenshot(img):
        pyautogui.screenshot(img)

    def yao_qi(self):
        try:
            while True:
                time.sleep(random.randint(1, 3))
                self.screenshot_adb("screen.png")
                if self.is_exists("screen.png", "images/zudui.png"):
                    self.ident_click("screen.png", "images/zudui.png")
                    self.log("进入组队页面")
                elif self.is_exists("screen.png", "images/zidongpipei.png"):
                    if self.is_exists("screen.png", "images/pipeizhong.png"):
                        self.log("匹配中...")
                        time.sleep(random.randint(5, 10))
                    else:
                        self.ident_click("screen.png", "images/zidongpipei.png")
                        self.log("点击自动匹配")
                elif self.is_exists("screen.png", "images/zhunbei.png"):
                    self.ident_click("screen.png", "images/zhunbei.png")
                    self.log("点击准备开始")
                elif self.is_exists("screen.png", "images/shengli.png"):
                    self.ident_click("screen.png", "images/shengli.png")
                    self.log("结算过场动画")
                elif self.is_exists("screen.png", "images/jiesuan.png"):
                    self.ident_click("screen.png", "images/jiesuan.png")
                    self.log("结算并退出")
                else:
                    time.sleep(random.randint(1, 5))
                    self.log("等待下一次开始...")
        except KeyboardInterrupt:
            self.log("Ctrl-C Exited.")


if __name__ == "__main__":
    op = Tools()
    # op.loop_click(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    op.yao_qi()
