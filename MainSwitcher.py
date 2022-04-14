# WHO SAID REFACTORING..?
import os
import time
from pynput.keyboard import Key, Controller
from pynput import keyboard 

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

def SetStatus(n):
    if n == 0:
        fout = open("/home/ari/.sx/status.txt", "w", encoding="utf-8")
        fout.write("sx0")
        fout.close()
    if n == 1:
        fout = open("/home/ari/.sx/status.txt", "w", encoding="utf-8")
        fout.write("sx1")
        fout.close()
    if n == 2:
        fout = open("/home/ari/.sx/status.txt", "w", encoding="utf-8")
        fout.write("sx2")
        fout.close()

os.system("ksx")

runsxhkd()

GetSX()

print(imw_count)

def ToSX():
    global imw_count
    print(imw_count)
    if imw_count == 0:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_0')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(1)
        os.system('setsxm')
        imw_count = 1
        return(imw_count)

def ToKitty():
    #KITTY
    global imw_count
    #global imw_count
    print(imw_count)
    if imw_count == 1:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_1')
        os.rename(r'/home/ari/.config/sxhkd/sx_0',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(0)
        os.system('setnm')
        imw_count = 0
        print(imw_count)
        return(imw_count)

def Semicolon():
    global imw_count
    #global imw_count
    print(imw_count)
    if imw_count == 1:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_1')
        os.rename(r'/home/ari/.config/sxhkd/sx_0',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(0)
        os.system('setnm')
        imw_count = 0
        print(imw_count)
        return(imw_count)
    if imw_count == 2:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_2')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(1)
        os.system('setsxm')
        imw_count = 1
        print(imw_count)
        return(imw_count)
    if imw_count == 0:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_0')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(1)
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
            print(Exception)
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

def Test1():
    pass
    # os.system("pguppy")


def Bar():
    k.press(Key.cmd)
    k.press("b")
    time.sleep(0.02)
    k.release(Key.cmd)

#'<ctrl>+<alt>+a': IMWheel,
#'<ctrl>+<alt>+s': sxhkd

## SX_2
#'<ctrl>+<alt>+g': Endprint,

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+a': Semicolon,
    '<ctrl>+<alt>+b': ToKitty,
    '<ctrl>+<alt>+c': ToSX,
    }) as h:
    h.join()


if __name__ == "__main__":
    runsxhkd()
