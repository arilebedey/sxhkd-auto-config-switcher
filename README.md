# sxhkd-autoswitcher
## The contents:

1. An automatic sxhkd configuration switcher that can currently switch between 2 sxhkd configurations, potentially much more.
2. A script that adds keybindins to one the three configurations (addLineToSxhkd.py)
3. Helper python and bash scripts needed to run the script (/helpers)

## Brief description:

I first wrote MainSwitcher.py which allowed me to switch between sxhkd configurations with a dedicated hotkey (which was semicolon in my case), but I realized that the switching should mostly be automatic, so I wrote AutoChSX.py. It automatically switches between my two main sxhkd configurations based on the window that is currently in focus (and it can also be paused by excecuting the /helpers/togglepause bash script)
