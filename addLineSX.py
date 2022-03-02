import os

a = input("Hotkey: ")
x = input("Command: ")

c = input("Comment: ")

b = input(r"Add to (select 0, 1, 2, ...): ") 

output = "\n\n" + c + "\n" + a + "\n" + "\t" + x

if b == "01":
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as f:
        f.write(output)
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "r") as g:
        fl = g.readline()
    if fl == '# SX_0\n':
        with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as z:
            z.write(output)
    if fl == '# SX_1\n':
        with open(r'/home/ari/.config/sxhkd/sx_0', "a+") as d:
            d.write(output)

if b == "0":
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "r") as g:
        fl = g.readline()
    if fl == '# SX_0\n':
        with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as z:
            z.write(output)
    if fl == '# SX_1\n':
        with open(r'/home/ari/.config/sxhkd/sx_0', "a+") as z:
            z.write(output)

if b == "1":
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "r") as g:
        fl = g.readline()
    if fl == '# SX_1\n':
        with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as z:
            z.write(output)
    if fl == '# SX_0\n':
        with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as z:
            z.write(output)

if b == "012":
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as f:
        f.write(output)
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "r") as g:
        fl = g.readline()
    if fl == '# SX_0\n':
        with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as zd:
            zd.write(output)
        with open(r'/home/ari/.config/sxhkd/sx_2', "a+") as d:
            d.write(output)
    if fl == '# SX_1\n':
        with open(r'/home/ari/.config/sxhkd/sx_0', "a+") as d:
            d.write(output)
        with open(r'/home/ari/.config/sxhkd/sx_2', "a+") as zd:
            zd.write(output)
    if fl == '# SX_2\n':
        with open(r'/home/ari/.config/sxhkd/sx_0', "a+") as d:
            d.write(output)
        with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as zd:
            zd.write(output)

if b == "12":
    with open(r'/home/ari/.config/sxhkd/sxhkdrc', "r") as g:
        fl = g.readline()
    if fl == '# SX_2\n':
        with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as f:
            f.write(output)
        with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as z:
            z.write(output)
    if fl == '# SX_1\n':
        with open(r'/home/ari/.config/sxhkd/sxhkdrc', "a+") as d:
            d.write(output)
        with open(r'/home/ari/.config/sxhkd/sx_2', "a+") as z:
            z.write(output)
    if fl == '# SX_0\n':
       with open(r'/home/ari/.config/sxhkd/sx_1', "a+") as z:
            z.write(output)
       with open(r'/home/ari/.config/sxhkd/sx_2', "a+") as z:
            z.write(output)

