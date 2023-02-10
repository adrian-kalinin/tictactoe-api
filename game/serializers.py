from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from game.models import Game
from game.services import GameService


class GameSerializer(serializers.ModelSerializer):
    """A game object"""

    def validate_board(self, value):
        """Check that board is valid"""

        # Validate board field contents
        if not GameService.is_board_valid(value):
            raise ValidationError(
                "Ensure this field has 9 characters and contains only '-', 'X', or 'O'."
            )

        # Validate first move on the board if it's a new game
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


class GameLocationSerializer(serializers.HyperlinkedModelSerializer):
    """A game location object"""

    location = serializers.HyperlinkedIdentityField(view_name="game:game-detail")

    class Meta:
        model = Game
        fields = ("location",)
