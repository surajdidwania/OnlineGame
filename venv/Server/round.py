from collections import defaultdict
import time as t
from _thread import *
from .game import Game
from .chat import Chat
from .player import Player

class Round(object):

    def __init__(self, word, player_drawing, players):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guesses = []
        self.skips = 0
        self.player_score = defaultdict(int)  # might be wrong
        self.time = 75
        self.start = time.time()
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        Runs in thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is Up!!")

    def get_scores(self):


    def skip(self):
        """
        returns true if round skipped threshold met
        :return:
        """
        self.skips += 1
        if self.skips > len(self.players)-2:
            return True

        return False

    def guess(self, player, wrd):
        """
        :returns bool if player guess correct word
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guesses.append(player)
            # TODO Scoring System here

        return correct

    def player_left(self, player):
        """
        removes players that left from scores and list
        :param player: Player
        :return: None
        """
        if player in self.player_score:
            del self.player_score[player]

        if player in self.player_guesses:
            self.player_guesses.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing Player left!!")

    def end_round(self, msg):
        """

        :param msg: str
        :return:
        """
