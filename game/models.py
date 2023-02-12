import random
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class GameStatus(models.TextChoices):
    """Game status choices"""

    RUNNING = "RUNNING", _("Running")
    X_WON = "X_WON", _("X won")
    O_WON = "O_WON", _("O won")
    DRAW = "DRAW", _("Draw")


class GamePlayer(models.TextChoices):
    """Player choices"""

    X = "X", _("X")
    O = "O", _("O")


class Game(models.Model):
    """Database model for games"""

    WIN_COMBINATIONS = [
        [0, 1, 2],  # Upper row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.CharField(max_length=9)
    status = models.CharField(
        max_length=20, choices=GameStatus.choices, default=GameStatus.RUNNING
    )
    player = models.CharField(
        max_length=1, choices=GamePlayer.choices, default=None, null=True
    )

    def autoplay(self):
        """Make a new move on the board"""
        empty_cells = [index for index, cell in enumerate(self.board) if cell == "-"]
        next_move = random.choice(empty_cells)

        if next_move:
            board = list(self.board)
            board[next_move] = "X" if self.player == GamePlayer.O else "O"
            self.board = "".join(board)

    def update_status(self):
        """Update game status based on the current board"""
        if "-" not in self.board:
            self.status = GameStatus.DRAW

        for combination in self.WIN_COMBINATIONS:
            if all([self.board[index] == "X" for index in combination]):
                self.status = GameStatus.X_WON
            elif all([self.board[index] == "O" for index in combination]):
                self.status = GameStatus.O_WON

    def __str__(self):
        """String representation of a game"""
        return f"'{self.board}' ({self.get_status_display()})"
