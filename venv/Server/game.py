from .player import Player
from .round import Round
from .board import Board
import random

class Game(object):

    def __init__(self, id, players):
        """
        init the game once the player threshold is met
        :param id: int
        :param players: players[]
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0  # where I am at player list after drawing
        self.connected_thread = thread
        self.start_new_round()

    def start_new_round(self):
        """
        starts a nre round
        :return: None
        """
        round_word = self.get_word()
        self.round = Round(round_word, self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()


    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return:
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        Calls to clean up objects when player disconnects
        :param player: Player
        :raises: Exception()
        :return:
        """
        pass

    def skip(self):
        """
        Increments the round skips, if skips are greater than threshold, starts new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No Round started Yet")

    def round_ended(self):
        """
        Iif the round ends call this,
        :return: None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        Calls update method on board
        :param x: int
        :param y: int
        :param color: (int,int,int)
        :return: None
        """
        if not self.board:
            raise Exception("No Board Created")
        self.board.update(x, y, color)

    def end_game(self):
        """
        ends the game should disconnect all player
        :return:
        """
        pass

    def get_word(self):
        """
        Gives a word that has not been used yet
        :return: str
        """
        with open("words.txt", 'r') as f:
            words = []

            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)

            self.words_used.add(wrd)

            r = random.randint(0, len(words))
            return words[r].strip()