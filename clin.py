import socket
import time

def Main(dmsg):
    myDict[dmsg]()


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    print("Waiting..")
    msg = s.recv(1024)
    dmsg = msg.decode("utf-8")
    if dmsg != None:
        print(dmsg)
        from a import *
        myDict = {
            "fff": fff,
        }
        Main(dmsg)
