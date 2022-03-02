# source /compv/bin/activate

import cv2
from PIL import Image
from mss import mss
from time import time
import glob
import os
import numpy as np

monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 80}

scs = mss()

lt = time()

while True:
    scsimg = scs.grab(monitor)
    img = Image.frombytes('RGB', (scsimg.size.width, scsimg.size.height), scsimg.rgb)
    bgrimg = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('test', np.array(bgrimg))
    print('FPD {}'.format(1 / (time() - lt)))
    lt = time()
    if cv2.waitKey(33) == ord('a'):
        cv2.destroyAllWindows()
        break

   
