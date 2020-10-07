import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import tkinter as tk
root = tk.Tk()
import requests
import time
import io
import random
import os
#os.system('cmd /k dir')

links_dir = 'https://raw.githubusercontent.com/hausuresh/pywinauto-personal/master/links/links.txt'
brave_dir = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
response = requests.get(links_dir)
lines = io.StringIO(response.text).readlines()
link_random = random.choice(lines)
# Screen resolution
x = round(root.winfo_screenwidth()*0.92)
y = round(root.winfo_screenheight()*0.92)

# Open VPN connection
# Open browser with tab(s) from with randome links
app = Application(backend='uia').start(brave_dir + ' --force-renderer-accessibility '+link_random)
app.window()
i=1
j=1
for i in range(1,150):
    for j in range(1,20):
        pywinauto.mouse.click(button='left', coords=(x,y))
        time.sleep(15)
        j=j+1
    print(str(i) + ' '  + str(x)+' '+  str(y))
    # random link
    link_random = random.choice(lines)
    # open link
    app = Application(backend='uia').start(brave_dir + ' ' +link_random)
    app.window()
    # go to tab 1 and close it
    #app = Application().connect(path=brave_dir)
    send_keys('^a^1')
    send_keys('^a^w')
    i=i+1
    print(i)
    #pywinauto.mouse.click(button='right', coords=(0, 0))

# Close VPN connection

os.system('cmd /k "nordvpn --disconnect "') 
