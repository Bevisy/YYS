import time
import random
import os
import aircv as ac
import pyautogui
import sys


class Tools(object):
    def __init__(self):
        # Screen Resolution 1024 x 640
        self.SCREEN_X = 1024
        self.SCREEN_Y = 640

        # connect to Android Simulator
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
    def loop_click(self, x, y, interval=1):
        try:
            while True:
                self.rand_click(x, y)
                time.sleep(interval)
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
            return True

    # Android Simulator 截图并取回本地
    @staticmethod
    def screenshot_adb(img):
        cmd = "adb exec-out screencap -p > {0}".format(img)
        if os.path.exists(img):
            os.remove(img)
            os.system(cmd)
        else:
            os.system(cmd)

    # 主机屏幕截图
    @staticmethod
    def screenshot(img):
        pyautogui.screenshot(img)

    def yao_qi(self):
        img = "screen.png"
        try:
            while True:
                time.sleep(random.randint(1, 3))
                self.screenshot_adb(img)
                if self.is_exists(img, "images/zudui.png"):
                    self.ident_click(img, "images/zudui.png")
                    self.log("进入组队页面")
                elif self.is_exists(img, "images/zidongpipei.png"):
                    if self.is_exists(img, "images/pipeizhong.png"):
                        self.log("匹配中...")
                        time.sleep(random.randint(5, 10))
                    else:
                        self.ident_click(img, "images/zidongpipei.png")
                        self.log("点击自动匹配")
                elif self.is_exists(img, "images/zhunbei.png"):
                    self.ident_click(img, "images/zhunbei.png")
                    self.log("点击准备开始")
                elif self.is_exists(img, "images/shengli.png"):
                    self.ident_click(img, "images/shengli.png")
                    self.log("结算过场动画")
                elif self.is_exists(img, "images/jiesuan.png"):
                    self.ident_click(img, "images/jiesuan.png")
                    self.log("结算并退出")
                else:
                    time.sleep(random.randint(1, 5))
                    self.log("等待下一次开始...")
        except KeyboardInterrupt:
            self.log("Ctrl-C Exited.")

    # 悬赏请求处理，默认接受
    def accept_or_refuse_xuanshang(self, img="screen.png", flag=True):
        if self.is_exists(img, "images/xuanshang.png") and flag:
            self.ident_click(img, "images/accept_xs.png")
            self.log("发现悬赏邀请并接受")
        elif self.is_exists(img, "images/xuanshang.png") and not flag:
            self.ident_click(img, "images/refuse_xs.png")
            self.log("发现悬赏要求并拒绝")
        else:
            self.log("未收到悬赏任务邀请")


# 御灵副本：查询副本门票；选取副本难度；式神录切换；
def yu_lin(self):
    pass


# 探索副本：单人和组队模式；狗粮自动换取；经验buff；输出式神切换；
def tan_suo(self):
    pass


# 御魂副本：副本难度选择；单人和组队模式；式神录切换；
def yu_hun(self):
    pass


# 悬赏任务：每日悬赏任务类型判断；悬赏任务查询数据库；
def xuan_shang(self):
    # TODO 考虑使用机器学习来做
    pass


if __name__ == "__main__":
    op = Tools()
    if sys.argv[1] == "loop":
        op.loop_click(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "yaoqi":
        op.yao_qi()
