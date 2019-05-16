import time
import pyautogui
import random


pyautogui.FAILSAFE = True # 默认为 False
pyautogui.PAUSE = 0.5 # 默认为 0.1s


def selectMode():
    print('''\n功能选择：
        0 防呆模式          安全退出程序
        1 测试模式          测试模式
        2 重复点击模式      重复点击固定范围（默认间隔3s）
        ''')
    raw = input("选择功能（输入数字，例如：0）：")
    index = int(raw)

    mode = [foolProofing, testMode, loopClick]
    comand = mode[index]
    comand()


def foolProofing():
    try:
        print(time.ctime(), '[INFO]: just for you, cute boy!')
    except KeyboardInterrupt:
        print('\n')


def testMode():
    try:
        img = pyautogui.screenshot()
        chromeX, chromeY = pyautogui.locateCenterOnScreen('chrome/icon.png')
        pyautogui.click(chromeX, chromeY)
        time.sleep(1)

        img = pyautogui.screenshot()
        chromeX, chromeY = pyautogui.locateCenterOnScreen('chrome/close.png')
        pyautogui.click(chromeX, chromeY)
    except KeyboardInterrupt:
        print('\n')


def loopClick():
    try:
        button_x = 745
        button_y = 221
        while True:
            rand_x = random.randint(0, 2)
            rand_y = random.randint(0, 2)
            click_x = button_x + rand_x
            click_y = button_y + rand_y
            pyautogui.click(click_x, click_y)
            time.sleep(2)
            print("click({x}, {y})".format(x = click_x, y = click_y))
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    selectMode()
