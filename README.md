# sxhkd-autoswitcher
The contents:

1. A SXHKD swithcher script that can switche between 3 sxhkd keybinding configurations (MainSwitcher.py) (keybinding configs not included)
2. An automatic keybindings switcher that can be paused that relies on MainSwitcher.py (AutoChSX.py)
3. A script that adds keybindins to one the three configurations (addLineToSxhkd.py)
4. Helper python and bash scripts (/helpers) 

Brief description:

I first wrote MainSwitcher.py which allowed me to switch between sxhkd configurations with a dedicated hotkey (which was semicolon in my case), but I realized that the switching should mostly be automatic, so I wrote AutoChSX.py. It automatically switches between my two main sxhkd configurations based on the window that is currently in focus (and it can also be paused by excecuting the /helpers/togglepause bash script)
