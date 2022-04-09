import os
from subprocess import DEVNULL, check_output
import time

def GetWin():
    output = check_output(['getactivewin'], stderr=DEVNULL, stdin=DEVNULL).decode("utf-8").rstrip('\n')
    return(output)

def GetSx():
    with open(r'/home/ari/.sx/status.txt', 'r') as fr:
        fl = fr.readline()
        return(fl)

def GetPause():
    with open(r'/home/ari/.sx/pause.txt', 'r') as fr:
        pause = fr.readline()
        pause = pause.rstrip('\n')
        return(pause)

resetpause = "python3 /home/ari/Scripts/sx_undopause.py"

os.system(resetpause)

tokitty = 'ionice -c 3 nice xdotool keydown control keydown alt key b; ionice -c 3 nice sleep 0.03; ionice -c 3 nice xdotool keyup control keyup alt'
tosx = 'ionice -c 3 nice xdotool keydown control keydown alt key c; ionice -c 3 nice sleep 0.03; ionice -c 3 nice xdotool keyup control keyup alt'

global lastwin
lastwin = GetWin()
# status = GetSx()
# pause = GetPause()

while True:
    time.sleep(0.1)
    win = GetWin()
    status = GetSx()
    pause = GetPause()
    # only run on window change
    if win == "kitty" and win != lastwin and status != "sx0":
        # time.sleep(0.5)
        os.system(tokitty)
        time.sleep(0.3)
        # print("kitty")
        lastwin = win
        continue
    if pause == "no" and win != "kitty" and status == "sx0":
        os.system(tosx)
        time.sleep(0.3)
        # print("no kitty")
        lastwin = win
        continue
    else:
        # print("ok")
        continue