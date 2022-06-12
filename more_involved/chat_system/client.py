# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:47:10 2022

@author: fredb
"""
import tkinter
import socket
from tkinter import *
from threading import Thread
def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            message_list.insert(tkinter.END,msg)
        except:
            print("Error")
def send():
    msg = my_message.get()
    my_message.set("")
    sock.send(bytes(msg,"utf8"))
    if msg == "#quit":
        sock.close()
        window.close()
def on_closing():
    my_message.set("#quit")
    send()
    
window = Tk()
window.title("Chat")
window.configure(bg="green")
message_frame = Frame(window, height=100, width=100, bg='red')
message_frame.pack()
my_message = StringVar()
my_message.set("")
scroll_bar = Scrollbar(message_frame)
message_list = Listbox(message_frame, height=15, width=100,bg="red", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
message_list.pack(side=LEFT, fill=BOTH)
message_list.pack()
label = Label(window, text="Enter the message", fg="blue", font="Aeria", bg="red")
label.pack()
entry_field = Entry(window, textvariable=my_message, fg="red", width=50)
entry_field.pack()
send_button = Button(window, text="Send", font="Aerial", fg="white", command=send)
send_button.pack()
quit_button = Button(window, text="Quit", font="Aerial", fg="white", command=on_closing)
quit_button.pack()
host = 'localhost'
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
receive_thread = Thread(target=receive)
receive_thread.start()
message = sock.recv(1024)
while message:
    print("Message: ", message.decode())
    message = sock.recv(1024)
    
sock.close()
mainloop()