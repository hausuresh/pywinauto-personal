
# note br linux
import requests
import time
import io
import random
import os
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as mouse_controller
keyboard = Controller()
mouse = mouse_controller()
links_dir = 'https://raw.githubusercontent.com/hausuresh/pywinauto-personal/master/links/links.txt'
response = requests.get(links_dir)
lines = io.StringIO(response.text).readlines()
link_random = random.choice(lines)
i=1
#brave_status = r'/home/brave/Downloads/brave_status.txt'
brave_status = '/home/brave/Downloads/brave_status.txt'
print('File readable')
def click_position(x,y,sleep_time):
    mouse.position = (x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(sleep_time)
def access_new_tab(address,sleep_time):
    with keyboard.pressed(Key.ctrl):
        keyboard.press('t')
        keyboard.release('t')
    keyboard.type(address)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(sleep_time)

def setup_brave():
    #Welcome Page
#    f = open(brave_status, "r")
#    status = f.read(1)
#    f.close()
    if 1==0:
    #if status=='0':
        time.sleep(10)
        #start brave maximized
        #Lets go
        click_position(390,505,2)
        #Skip welcome tour
        mouse.scroll(0, 2)  
        click_position(211,558,2)
        #Create Wallet
        #---Click reward
        click_position(692,51,2)
        #---Creat wallet
        click_position(512,345,2)
        #Maximum ads
        access_new_tab('brave://rewards',1)
        click_position(502,347,1)
        #---Dropdown list
        click_position(556,424,1)        
        #---Choose 5 ads per hour
        mouse.scroll(0, 2)  
        click_position(316,512,1)   
        #Turn off contribute
        mouse.scroll(0, 1)  
        click_position(572,537,1)
        #Open new tab page
        access_new_tab('brave://settings',1)
        click_position(207,410,1)
        #Default web browser
        click_position(689,308,1)
        #Turn off static
        access_new_tab('brave://settings/?search=privacy',2)
        click_position(702,357,1)

        f = open(brave_status, "w")
        status = f.write('1')
        f.close()
    else: 
        print('Setup already!')
    
def automation():
    for i in range(1,120):
        j=1
        # random link
        link_random = random.choice(lines)
        #return app to top window
        # open link
        #brave_start_cmd = "brave-browser  " + link_random
        #os.system(brave_start_cmd)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('t')
            keyboard.release('t')    
        keyboard.type(link_random)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(240)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('2')
            keyboard.release('2')
        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')

        i=i+1
        print(i)

setup_brave()
automation()
