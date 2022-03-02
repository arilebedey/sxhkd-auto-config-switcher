import os
from prompter import yesno
import subprocess
import pyperclip


def CountPh():
    count = 0
    e = subprocess.check_output(['slss'], shell=True)
    lss = e.decode().split("\n")
    for lss1 in lss:
        if "png" not in str(lss1):
            continue
        if "total" in lss1:
            continue
            print("hahah")
        if "." not in str(lss1):
            continue
        else:
            count = count + 1
    return("{} Images".format(count))



def photolist(lss, offset, lenght, rev, name):
    lss = lss.split("\n")
    count = 0
    roffset = 0
    flss = ''
    offset = int(offset)
    lenght = int(lenght)
    if rev == False:
        #YesRev
        lss = lss[::-1]
        roffset = 0
    else:
        roffset = 0
    for lss1 in lss:
        if "png" not in str(lss1):
            continue
        if "total" in lss1:
            continue
            print("hahah")
        if "." not in str(lss1):
            continue
        else:
            if offset > roffset:
                    roffset = roffset + 1
                    pass
                    print(lss1)
            else:
                if lenght != count:
                    lss1 = lss1.split(" ")
                    flss = flss + "/home/ari/Images/Screenshots/" + lss1[-1] + "\n"
                    count = count + 1
                    print(lss1)
    print(flss)
    ffile = "/home/ari/Scripts/Photos/Makers/PhGalleries/" + name
    with open(ffile, "w+", encoding='utf-8') as f:
        f.write(flss)
        f.close()
        og = "cat {} | sxiv -i".format(ffile)
        os.system(og)
        pyperclip.copy(og)
        print(og)



def CreateSlideshow():
    print("PHOTO GALLERY UTILITY")
    print(CountPh())
    lenght = CountPh().split(" ")[0]
    offset = 0
    if offset == True:
        offset = input("Offset: ")
    else:
        offset = 0
    rev = 0
    name = "normupdphotos"
    e = subprocess.check_output(['slss'], shell=True)
    lss = e.decode()
#    print(lss)
    photolist(lss, offset, lenght, rev, name)
    

CreateSlideshow()

