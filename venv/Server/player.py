from .game import Game

class Player(object):
    def __init__(self, ip, name):
        """
        init the player object
        :param ip:
        :param name:
        """
        self.ip = ip
        self.name = name
        self.score = 0
        self.game = None

    def set_game(self, game):
        """
        sets the player game association
        :param game: Game
        :return:
        """
        self.game = game

    def update_score(self, x):
        """
        updates a player score
        :param x: int
        :return:
        """
        self.score += x

    def guess(self, wrd):
        """
        makes a player guess
        :param wrd: str
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        call to disconnect player
        :return:
        """
        self.game.player_disconnected(self)

    def get_score(self):
        """
        gets player score
        :return:
        """
        return self.score

    def get_name(self):
        """
        gets player name
        :return:
        """
        return self.name

    def get_ip(self):
        """
        gets player ip address
        :return:
        """
        return self.ip

