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