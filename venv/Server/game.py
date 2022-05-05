from .player import Player
from .round import Round
from .board import Board

class Game(object):

    def __init__(self, id, players):
        """

        :param id:
        :param players:
        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0  # where I am at player list after drawing
        self.start_new_round()

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind += 1
        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        """

        :param player:
        :param guess:
        :return:
        """
        pass

    def player_disconnected(self, player):
        """

        :param player:
        :return:
        """
        pass

    def skip(self):
        pass

    def round_ended(self):
        pass

    def update_board(self):
        pass

    def end_game(self):
        pass

    def get_word(self):
        """
        Gives a word that has not been used yet
        :return:
        """
        # todo to get list of words from somewhere