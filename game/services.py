import re

from game.models import Game


class GameService:
    """Service class to handle game objects"""

    def __int__(self, game: Game):
        self.game = game

    @staticmethod
    def is_board_valid(board):
        pattern = re.compile(r"^[XO-]{9}$")
        return pattern.match(board)

    @staticmethod
    def is_first_move_valid(board):
        return (board.count("X") + board.count("O")) <= 1
