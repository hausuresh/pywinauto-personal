from datetime import datetime, timedelta
import pyautogui
import time

#helper function that prints x,y coordinate of my display

def printPosition():
    #the code below prints the x,y coordinates
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionString, end='')
            print('\b' * len(positionString), end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone.')

printPosition()