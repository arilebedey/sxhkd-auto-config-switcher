# sxhkd-autoswitcher
The description:

1. A SXHKD swithcher script that switches between 3 sxhkd binding configurations with specific hotkeys (MainSwitcher.py)
2. An automatic keybindings switcher that can be paused that relies on MainSwitcher.py (AutoChSX.py)
3. A script that adds keybindins to one the three configurations (addLineToSxhkd.py)
4. Helper python and bash scripts (the rest) 

The talk about AutoChSX.py:

To avoid manually switching between sxhkd configurations with (MainSwitcher.py) and a dedicated hotkey (which was semicolon in my case), I wrote an additional script (AutoChSX.py) that automacally switches to the terminal sxhkd config (referred to as sx0/sx_0) when in the terminal window, and switches back to the web browsing config (sx1/sx_1) when in other apps.
