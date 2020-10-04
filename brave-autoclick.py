from win32api import GetSystemMetrics
import pywinauto
import time
x = round(GetSystemMetrics(0)*0.92)
y = round(GetSystemMetrics(1)*0.92)

for i in range(1,50):
    # 13 seconds per click
    time.sleep(3)
    pywinauto.mouse.click(button='right', coords=(x,y))
    print(str(i) + ' '  + str(x)+' '+  str(y))