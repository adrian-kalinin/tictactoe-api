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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.CharField(max_length=9)
    status = models.CharField(
        max_length=20, choices=GameStatus.choices, default=GameStatus.RUNNING
    )
    previous_player = models.CharField(
        max_length=1, choices=GamePlayer.choices, default=None, null=True
    )

    def __str__(self):
        """String representation of a game"""
        return f"'{self.board}' ({self.get_status_display()})"
