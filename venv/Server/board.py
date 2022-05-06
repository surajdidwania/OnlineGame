class Board(object):
    ROWS = COLS = 720

    def __init__(self):
        """
        Init the board by creating empty board
        """
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        Updates the singular pixel of the board
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return:
        """
        self.data[y][x] = color

    def _create_empty_board(self):
        """
        Creates an empty board
        :return: None
        """
        return [[(255, 255, 255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def clear(self):
        """
        Clears board to all white
        :return: None
        """
        self.data = self._create_empty_board()

    def fill(self, x, y):
        """
        Fills in a specific shape or area using recursion
        :param x: int
        :param y: int
        :return: Nine
        """
        pass

    def get_board(self):
        """
        gets the data of the board
        :return: (int, int, int)
        """
        return self.data