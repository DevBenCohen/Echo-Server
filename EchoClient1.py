from socket import *
from Tkinter import *
import tkFont

def close_tkwindow(root):
    root.destroy()

root = Tk()
fnt = tkFont.Font(family="Fira Code", size=16)
root.title("Inputs and Outputs")
root.geometry("500x350")
root.resizable(width=FALSE, height=FALSE)
listbox = Listbox(root, font=fnt)
listbox.see(END)
listbox.pack(side=LEFT,expand="YES", fill="both")
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill =Y)

f = open("C:\\Users\Ben\Desktop\Details.txt", "r")
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
try:
    while 1:
        data = raw_input(">")
        listbox.insert(END,">"+data)
        listbox.itemconfig(END, bg="#336d9d")
        if not data: break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data: break
        if data == "exit": break
        listbox.insert(END,data)
        listbox.itemconfig(END, bg ="#ffd847")

    root.close_tkwindow()
    tcpCliSock.close()
    root.mainloop()
except:
    print "Finished"
