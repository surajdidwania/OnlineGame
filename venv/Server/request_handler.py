import socket
from _thread import *
import time
from tkinter import E
from .player import Player
from .game import Game
import threading
import json


class Server(object):
    PLAYERs = 8
    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        handles in gane communication between players
        :param conn: Connection object
        :param ip: str Ip Address
        :param name: str Name of the player
        :return: None
        """
        while True:
            try:
                #receive request
                data = conn.recv(1024)
                data = json.loads(data)

                # Player is not apart of game
                keys = [key for key in data.keys()]
                send_msg = {key:[] for key in keys}

                for key in keys:
                    if key == -1:   #Get Game

                    elif key == 0:    #Guess

                    elif key == 1:    #skip

                    elif key == 2:    # Get Chat

                    elif key == 3:    # Get baord

                    elif key == 4:    # Get Score

                    elif key == 5:    # Get round

                    elif key == 6:    # Get word

                    elif key == 7:    # Get Skips

                    elif key == 8:    # Update Board

                    elif key == 9:    # Get Round Time

                    else:
                        raise Exception("Not a valid request")
                    
                conn.sendall(json.dumps(send_msg))
                
            except Exception() as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected",e)
                conn.close()
                #todo call player game disconnected

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player:
        :return: None
        """
        self.connection_queue.append(player)

        if len(self.connection_queue) >= 8:
            
            game = Game(self.connection_queue[:], self.game_id)

            for p in self.connection_queue:
                p.set_game(game)

            
            self.game_id +=1
            self.connection_queue = []

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
