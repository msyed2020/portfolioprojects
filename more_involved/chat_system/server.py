# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:39:03 2022

@author: fredb
"""

import socket
from threading import Thread

host = 'localhost'
port = 8080
clients = {}
addresses = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
def handle_clients(conn, address):
    name = conn.recv(1024).decode()
    welcome = "Welcome " + name + ". Type #quit to leave chat"
    conn.recv(bytes(welcome, "utf8"))
    message = name + " has recently joined the chat room"
    broadcast(bytes(message,"utf8"))
    clients[conn] = name
    while True:
        message = conn.recv(1024)
        if message != bytes("#quit", "utf8"):
            broadcast(message, name + ":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " has left the chat room", "utf8"))
            
def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, " has been connected")
        client_conn.send(" Welcome to the Chat Room, Please Type Your Name to Continue ".encode('utf8'))
        addresses[client_conn] = client_address
        
        Thread(target=handle_clients, args=(client_conn, client_address)).start()
        
def broadcast(message, prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+message)
        
if __name__=="__main__":
    sock.listen(5)
    print("Server is running and listening to client request")
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()

#sock.listen(1)
#print("Server is running and listening to client request")
#conn, address = sock.accept()
#message = "Hey"
#conn.send(message.encode())
#conn.close()