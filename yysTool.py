import time
import pyautogui


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
        pyautogui.screenshot()
        chromeX, chromeY = pyautogui.locateCenterOnScreen('chrome/icon.png')
        pyautogui.click(chromeX, chromeY)
        time.sleep(1)

        pyautogui.screenshot()
        chromeX, chromeY = pyautogui.locateCenterOnScreen('chrome/close.png')
        pyautogui.click(chromeX, chromeY)
    except KeyboardInterrupt:
        print('\n')


def loopClick():
    try:
        buttonx = 1300
        buttony = 780
        while True:
            for i in range(buttonx, buttonx+2, 1):
                for j in range(buttony, buttony+2, 1):
                    pyautogui.click(i, j)
                    print("click ({x}, {y})".format(x=i, y=j))
                    time.sleep(3)
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    selectMode()
