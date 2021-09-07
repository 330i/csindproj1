import pyautogui
import sys

width, height = pyautogui.size()
x, y = 0
print('Press Ctrl-C to quit.')
try:
    while True:
        if int(pyautogui.position().x/(width/10))==int(x/(width/10)) and int(pyautogui.position().y/(height/10))==int(y/(height/10)):
            print("not using mouse")
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(int(x/(width/10))).rjust(4) + ' Y: ' + str(int(y/(height/10))).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        pyautogui.sleep(2)
except KeyboardInterrupt:
    print('\n')