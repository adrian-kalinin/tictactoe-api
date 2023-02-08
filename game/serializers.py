from rest_framework import serializers

from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    """Serializer for games"""

    def validate_board(self, value):
        """Check that board is valid"""
        value = "---------" if value == "" else value

        return value

    class Meta:
        model = Game
        fields = ("id", "board", "status")
        extra_kwargs = {"status": {"read_only": True}}
