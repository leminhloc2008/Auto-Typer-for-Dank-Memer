#import modules
import pyautogui
import keyboard
from keyboard import press
import time
import threading

#wait 3s before the bot start to typing
time.sleep(3)

beg = 'pls beg'
search = 'pls search'
postmeme = 'pls postmeme'
dig = 'pls dig'
hunt = 'pls hunt'
fish = 'pls fish'

plsbeg = [i for i in beg]
plssearch = [i for i in search]
plspostmeme = [i for i in postmeme]
plsdig = [i for i in dig]
plshunt = [i for i in hunt]
plsfish = [i for i in fish]

while True:
    #type commands
    pyautogui.typewrite(plsbeg)
    press('enter')

    pyautogui.typewrite(plssearch)
    press('enter')

    pyautogui.typewrite(plspostmeme)
    press('enter')

    pyautogui.typewrite(plsdig)
    press('enter')

    pyautogui.typewrite(plshunt)
    press('enter')

    pyautogui.typewrite(plsfish)
    press('enter')

    #wait 40s cooldown
    time.sleep(40)

    #if user press key q then exit
    if keyboard.read_key() == "q":
        print("Quitting...")
        break

