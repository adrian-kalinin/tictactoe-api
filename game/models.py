import uuid

from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class GameStatus(models.TextChoices):
    """Game status choices"""

    RUNNING = "RUNNING", _("Running")
    X_WON = "X_WON", _("X won")
    O_WON = "O_WON", _("O won")
    DRAW = "DRAW", _("Draw")


class Game(models.Model):
    """Database model for games"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.CharField(
        max_length=9, validators=[RegexValidator(regex=r"^[XO-]{9}$")]
    )
    status = models.CharField(
        max_length=20, choices=GameStatus.choices, default=GameStatus.RUNNING
    )

    def __str__(self):
        """String representation of a game"""
        return f"'{self.board}' ({self.get_status_display()})"
