# note br linux
import requests
import time
import io
import random
import os
from pynput.keyboard import Key, Controller

keyboard = Controller()

links_dir = 'https://raw.githubusercontent.com/hausuresh/pywinauto-personal/master/links/links.txt'
#brave_dir = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
response = requests.get(links_dir)
lines = io.StringIO(response.text).readlines()
link_random = random.choice(lines)

#brave_start_cmd = "brave-browser  " + link_random
#os.system(brave_start_cmd)
i=1
for i in range(1,120):
    j=1
    # random link
    link_random = random.choice(lines)
    #return app to top window
    # open link
    brave_start_cmd = "brave-browser  " + link_random
    os.system(brave_start_cmd)
    time.sleep(300)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('2')
        keyboard.release('2')
    with keyboard.pressed(Key.ctrl):
        keyboard.press('w')
        keyboard.release('w')

    i=i+1
    print(i)
