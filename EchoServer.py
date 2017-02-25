from socket import *
import threading
import thread
import datetime
import time

def get_ip():
    import socket
    return socket.gethostbyname(socket.getfqdn())

def get_open_port():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname() [1]
    s.close()
    return port

def save_information(serversock):
    import socket
    f = open("C:\\Users\Ben\Desktop\Details.txt", "w")
    f.write("pass123"+"\n"+str(PORT)+"\n"+get_ip())

def Set_A_Timer():
    clientsock.send("How much time in seconds? ")
    data = clientsock.recv(BUFSIZ)
    try:
        time.sleep(int(data))
        return"Timer Done"
    except:
        return ("Invalid Input, Going back for the echo function")

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFSIZ)
        print data
        if not data: break
        if data == "exit": break
        if data == "Current Time":
            data = "current time (of the server PC): " + str(datetime.datetime.now())
        if data == "Set a Timer":
                data = Set_A_Timer()
        clientsock.send(data)
    print "ending communication with",addr
    clientsock.close()

BUFSIZ = 1024
HOST = get_ip()
PORT = get_open_port()
ADDR = (HOST, PORT)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(2)
save_information(serversock)
print "Type This into the Client:\n IP = get_ip\n PORT = "+str(PORT)

while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    print '...connected from:', addr
    thread.start_new_thread(handler, (clientsock, addr))
serversock.close()
