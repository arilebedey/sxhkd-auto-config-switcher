import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Waiting...")
    sendthis = input("Fire function: ")
    clientsocket.send(bytes(sendthis, "utf-8"))

