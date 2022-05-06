import socket
from _thread import *
import time
from .player import Player
from .game import Game
from queue import Queue
import threading

def connection_thread():
    server = ""
    port = 5555

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.bind(server,port)
    except socket.error as e:
        str(e)

    s.listen()
    print ("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        print ("[CONNECT] New Connection")

        threading.Thread(target=, (addr,""))