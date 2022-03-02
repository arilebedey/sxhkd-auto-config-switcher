#from pynput import keyboard
import os
import time
#import subprocess
from pynput.keyboard import Key, Controller
from pynput import keyboard 
#import pyautogui

k = Controller()

def Presrel(n):
    k.press(n)
    k.release(n)

def Switch():
    pass

def runsxhkd():
    os.system("runsxhkd")

fl = ''
imw_count = 3

def GetSX():
    global fl
    with open(r'/home/ari/.config/sxhkd/sxhkdrc') as f:
        fl = f.readline()
        print(fl)
        global imw_count
        if fl == '# SX_2\n':
            print("2")
            os.system('setsx2m')
            imw_count = 2
        if fl == '# SX_0\n':
            imw_count = 0
            print("0")
            os.system('setnm')
        if fl == '# SX_1\n':
            imw_count = 1
            os.system('setsxm')
        return(imw_count)


os.system("ksx")

runsxhkd()

GetSX()



def Semicolon():
    global imw_count
    #global imw_count
    print(imw_count)
    if imw_count == 1:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_1')
        os.rename(r'/home/ari/.config/sxhkd/sx_0',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        os.system('setnm')
        imw_count = 0
        print(imw_count)
        return(imw_count)
    if imw_count == 2:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_2')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        os.system('setsxm')
        imw_count = 1
        print(imw_count)
        return(imw_count)
    if imw_count == 0:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_0')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        os.system('setsxm')
        imw_count = 1
        return(imw_count)


def Endprint():
    global imw_count
    #global imw_count
    print(imw_count)
    if imw_count == 2:
        try:
            os.system('ksx')
            os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_2')
            os.rename(r'/home/ari/.config/sxhkd/sx_0',r'/home/ari/.config/sxhkd/sxhkdrc')
            os.system('runsxhkd')
            os.system('setnm')
            imw_count = 0
            return(imw_count)
        except Exception:
            pass
    if imw_count == 0:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_0')
        os.rename(r'/home/ari/.config/sxhkd/sx_2',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        os.system('setsx2m')
        imw_count = 2
        return(imw_count)
    if imw_count == 1:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_1')
        os.rename(r'/home/ari/.config/sxhkd/sx_2',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        os.system('setsx2m')
        imw_count = 2

def SXSwitch1():   
    #Swap sxhkdrc
    os.system("rsx")

sxh_c = 0

def Backslash():
    Presrel("A")
    print("hello")

def Num1():
    os.system("pguppy")

def test():
    print("wow.")
    #os.system("python3 ~/Scripts/sxhkd/pgdn.py")
    #os.system("xdotool key Page_Down")
    #pyautogui.press('pagedown')
    #k.press(Key.page_down)
    #time.sleep(0.3)
    #k.release(Key.page_down)
    #k.press("w")


#with keyboard.pressed(Key.ctrl):
#   keyboard.press(Key.f4)
#   keyboard.release(Key.f4)

# Mouse Browser Control Script
def mouseBCs():
    pass 

def b():
    k.press(Key.cmd)
    k.press("b")

    time.sleep(0.02)
    k.release(Key.cmd)

#'<ctrl>+<alt>+a': IMWheel,
#'<ctrl>+<alt>+s': sxhkd

with keyboard.GlobalHotKeys({    
    '<ctrl>+<alt>+a': Semicolon,
    '<ctrl>+<alt>+1': Num1,
    '<ctrl>+<alt>+<shift>+d': Backslash,
    '<ctrl>+<alt>+g': Endprint,
    }) as h:
    h.join()


if __name__ == "__main__":
    runsxhkd()
    
# MAKE BROWSER MODE
