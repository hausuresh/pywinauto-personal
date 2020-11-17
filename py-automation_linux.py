import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import mouse

import tkinter as tk
root = tk.Tk()
import requests
import time
import io
import random
import os


links_dir = 'https://raw.githubusercontent.com/hausuresh/pywinauto-personal/master/links/links.txt'
#brave_dir = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
response = requests.get(links_dir)
lines = io.StringIO(response.text).readlines()
link_random = random.choice(lines)
# Screen resolution
x = round(root.winfo_screenwidth()*0.92)
y = round(root.winfo_screenheight()*0.92)

# Open VPN connection
# Open browser with tab(s) from with randome links
#app = Application(backend='uia').start(brave_dir + ' --force-renderer-accessibility '+link_random)
#app = Application().connect(path=brave_dir)
#app.window()
brave_start_cmd = "brave-browser " + link_random
os.system(brave_start_cmd)
i=1
for i in range(1,120):
    j=1
    print(str(x)+' '+  str(y))
    # go to tab 1 and close it
    # random link
    link_random = random.choice(lines)
    #return app to top window
    # open link
    brave_start_cmd = "brave-browser " + link_random
    os.system(brave_start_cmd)
    send_keys('^a^1')
    send_keys('^a^w')
        
    i=i+1
    print(i)