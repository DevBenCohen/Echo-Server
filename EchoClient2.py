from socket import *

f = open("C:\\Users\user\Desktop\Details.txt", "r")
file = f.read()
details = file.split("\n")
password = details[0]
free_port = details[1]
s_ip = details[2]

HOST = str(s_ip)
PORT = int(free_port)
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while 1:
    data = raw_input(">")
    if not data: break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data: break
    if data == "exit": break
    print data
tcpCliSock.close()
