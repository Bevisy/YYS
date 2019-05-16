import pyautogui

pyautogui.FAILSAFE = True  # 默认为 False
pyautogui.PAUSE = 0.5  # 默认为 0.1s

print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
