import os
from subprocess import DEVNULL, check_output
import subprocess
import time

# Replace my home path with your path with Vim:
# :%s/\/home\/ari/<your_path>/g
# Hit enter
#
# Quick explanation:
# Replace all instances of a by b in Vim is as follows: :%s/a/b/g
# But since "/" is part of the command it must be "escaped" (or made "invisible"), by writing "\" right before it, thus we write "\/home\/ari"

# IMPORTANT
# the calls to "setsx2m", "setnm", and "setsxm" are calls to bash scripts that all display a different indicator on my window manager statusbar
# It looks something like this:
# xsetroot -name "SXXXX   00000   00000   00000   00000   00000"
# (Which in font 5 looks exactly how I want it to)

##### CONFIG SWAMPING FUNCTIONS #####

def runsxhkd():
    os.system("runsxhkd")

fl = ''
imw_count = 3

def GetSX():
    global fl
    with open(r'/home/ari/.config/sxhkd/sxhkdrc') as f:
        fl = f.readline()
        # print(fl)
        global imw_count
        if fl == '# SX_2\n':
            # print("2")
            os.system('setsx2m')
            imw_count = 2
        if fl == '# SX_0\n':
            imw_count = 0
            # print("0")
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

if imw_count == 0:
    SetStatus(0)
if imw_count == 1:
    SetStatus(1)
if imw_count == 2:
    SetStatus(2)


# print("first imw", imw_count)

def ToSX1():
    global imw_count
    if imw_count == 0:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_0')
        os.rename(r'/home/ari/.config/sxhkd/sx_1',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(1)
        os.system('setsxm')
        imw_count = 1
        # print("success tosx1")
        return(imw_count)

def ToSX0():
    #KITTY
    global imw_count
    #global imw_count
    # print(imw_count)
    # print("ok")
    if imw_count == 1:
        os.system('ksx')
        os.rename(r'/home/ari/.config/sxhkd/sxhkdrc',r'/home/ari/.config/sxhkd/sx_1')
        os.rename(r'/home/ari/.config/sxhkd/sx_0',r'/home/ari/.config/sxhkd/sxhkdrc')
        os.system('runsxhkd')
        SetStatus(0)
        os.system('setnm')
        imw_count = 0
        # print(imw_count)
        return(imw_count)

##### AUTO SWITCHING RELATED FUNCTION #####

def GetWin():
    output = check_output(['getactivewin'], stderr=DEVNULL, stdin=DEVNULL).decode("utf-8").rstrip('\n')
    return(output)

# Retrieve currently active sxhkd configuration
def GetSXConfig():
    with open(r'/home/ari/.sx/status.txt', 'r') as fr:
        fl = fr.readline()
        return(fl)

# Retrieve "pause" status
def GetPause():
    with open(r'/home/ari/.sx/pause.txt', 'r') as fr:
        pause = fr.readline()
        pause = pause.rstrip('\n')
        return(pause)

# For testing with https://github.com/shiro/map2
def Hypr():
    os.system('hyprlock')

# For testing with https://github.com/shiro/map2
def Map2():
    output = subprocess.Popen(['map2', '-d', '/home/ari/.map2/devices.list', '/home/ari/.map2/map.m2'])
    return(output)

def UndoPause():
    os.system("python3 /home/ari/Scripts/sx_undopause.py")
    try:
        os.system("rm /home/ari/.toggle/toggle_pause")
    except Exception:
        pass

UndoPause()

# For testing with https://github.com/shiro/map2
map2 = 'map2 -d /home/ari/.map2/devices.list /home/ari/.map2/map.m2'

# Apps that require sx0 configuration
sx0 = ["kitty", "mpv"]
## Script will change to sx1 configuration when all other windows are focused

##### MAIN LOOP #####

while True:
    time.sleep(0.1)
    win = GetWin()
    status = GetSXConfig()
    pause = GetPause()
    if win in sx0 and status != "sx0":
        # Triggering config change to terminal hotkeys
        # print("status: ", status)
        ToSX0()
        time.sleep(0.15)
        continue
    if pause == "no" and win not in sx0 and status == "sx0":
        # Triggering config change to browsing hotkeys
        ToSX1()
        time.sleep(0.15)
        continue
    if pause == "yes" and win not in sx0:
        ToSX0()
        time.sleep(0.15)
        continue
    else:
        continue
