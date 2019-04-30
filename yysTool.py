import sys
import time
import pyautogui


pyautogui.FAILSAFE = True # 默认为 False
pyautogui.PAUSE = 0.5 # 默认为 0.1s


def selectMode():
    print('''\n功能选择：
        0 防呆模式          安全退出程序
        1 测试模式          测试模式
        2 刷困难金币        离岛活动
        ''')
    raw = input("选择功能（输入数字，例如：0）：")
    index = int(raw)

    mode = [foolProofing, testMode, goldCoin]
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


def goldCoin():
    try:
        while True:
            pass # 活动操作逻辑
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    selectMode()
