import socket
from _thread import *
import time
from .player import Player
from .game import Game
import threading


class Server(object):
    def __init__(self):
        self.connection_queue = []

    def player_thread(self, conn, player):
        """
        handles in gane communication between players
        :param conn: Connection object
        :param ip: str Ip Address
        :param name: str
                    Name of the player
        :return:
        """
        while True:
            try:

            except Exception() as e:
                print(f"[EXCEPTION] {name} disconnected",e)

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player:
        :return:
        """
        self.connection_queue.append(player)


    def authentication(self, conn, addr):

        try:
            data = conn.recv(16)
            name = str(data.decode())
            if not name:
                raise Exception("No Name Received")

            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            threading.Thread(target=self.player_thread, args=(conn, player))

        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()

    def connection_thread(self):
        server = ""
        port = 5555

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            connection.bind(server, port)
        except socket.error as e:
            str(e)

        connection.listen()
        print("Waiting for a connection, Server Started")

        while True:
            conn, addr = connection.accept()
            print("[CONNECT] New Connection")

            self.authentication(conn, addr)


if __name__=="__main__":
    s = Server()
    threading.Thread(target=s.connection_thread())
