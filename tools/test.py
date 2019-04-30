import pyautogui
import time

pyautogui.FAILSAFE = True # 默认为 False
pyautogui.PAUSE = 0.5 # 默认为 0.1s


if __name__ == "__main__":
    # dist = 10
    # while dist >= 0:
    #     pyautogui.dragRel(dist, 0, duration = 0.5) # 向右
    #     dist -= 5
    #     pyautogui.dragRel(0, dist, duration = 0.5) # 向下
    #     pyautogui.dragRel(-dist, 0, duration = 0.5) # 向左
    #     dist -= 5
    #     pyautogui.dragRel(0, -dist, duration = 0.5) # 向上
    
    # pyautogui.alert('hello') # message + OK button

    # pyautogui.confirm('hello') # message + OK button + Cancel button

    # pyautogui.prompt('input message:') # request user input message

    # pyautogui.screenshot('foo.jpg') # snapshot and save to current dir
    
    pyautogui.locateOnScreen('screen.jpg')