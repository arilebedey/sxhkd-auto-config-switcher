# sxhkd-auto-config-switcher
## Brief description:

First I wrote a script (now in arilebedey/sxhkd-config-switcher) that allowed me to switch between sxhkd configurations with a dedicated hotkey, until I realized that the switching should mostly be automatic, then updated it.

This script automatically switches between my two main sxhkd configurations: my terminal configuration, and my browsing one.

This script will automatically switch between properly written sxhkd configs based on the window that is currently in focus, and can also toggle the terminal configuration outside of the terminal (mainly useful in the browser) by quickly excecuting the /helpers/togglepause bash script, set to alt + space, in my case).

## Contents:

1. An automatic sxhkd configuration switcher that can currently switch between 2 sxhkd configurations, potentially much more.
2. A bonus script that adds keybindings to one the three configurations (addLineToSxhkd.py)
3. Helper python and bash scripts needed to run the script (/helpers)

## Warning:

Be carful when this tweaking script and always have fresh backups of your sxhkd configurations.

## CPU Usage:

0.1-0.3% on an intel i5-6300u.

## Bugs:

No currently known bugs.
