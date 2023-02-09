from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from game.models import Game
from game.services import GameService


class GameSerializer(serializers.ModelSerializer):
    """Serializer for games"""

    def validate_board(self, value):
        """Check that board is valid"""
        if not GameService.is_board_valid(value):
            raise ValidationError(
                "Ensure this field has 9 characters and contains only '-', 'X', or 'O'."
            )

        if not self.instance:
            if not GameService.is_first_move_valid(value):
                raise ValidationError(
                    "Ensure the board is either empty or contains only one 'X' or 'O'."
                )

        return value

    class Meta:
        model = Game
        fields = ("id", "board", "status")
        extra_kwargs = {"status": {"read_only": True}}
