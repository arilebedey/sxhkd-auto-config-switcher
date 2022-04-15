import os
from subprocess import DEVNULL, check_output
import subprocess
import time

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
    os.system('hyprlock2')
    os.system('hyprlock2')
    os.system('hyprlock2')

# For testing with https://github.com/shiro/map2
def Map2():
    output = subprocess.Popen(['map2', '-d', '/home/ari/.map2/devices.list', '/home/ari/.map2/map.m2'])
    return(output)

resetpause = "python3 /home/ari/Scripts/sx_undopause.py"

os.system(resetpause)

# Commands that trigger config switching (detected via ./MainSwitcher.py)
tosx0 = 'ionice -c 3 nice xdotool keydown control keydown alt key b; ionice -c 3 nice sleep 0.03; ionice -c 3 nice xdotool keyup control keyup alt'
tosx1 = 'ionice -c 3 nice xdotool keydown control keydown alt key c; ionice -c 3 nice sleep 0.03; ionice -c 3 nice xdotool keyup control keyup alt'
map2 = 'map2 -d /home/ari/.map2/devices.list /home/ari/.map2/map.m2'

global lastwin
lastwin = GetWin()
# Apps that require sx0 configuration
## Script with change to sx1 configuration in all other windows
sx0 = ["kitty", "mpv"]

while True:
    time.sleep(0.1)
    win = GetWin()
    status = GetSXConfig()
    pause = GetPause()
    if win in sx0 and win != lastwin and status != "sx0":
        # Triggering config change to terminal hotkeys
        os.system(tosx0)
        time.sleep(0.15)
        lastwin = win
        continue
    if pause == "no" and win not in sx0 and status == "sx0" and win != lastwin:
        # Triggering config change to browsing hotkeys
        os.system(tosx1)
        time.sleep(0.15)
        lastwin = win
        continue
    else:
        continue
