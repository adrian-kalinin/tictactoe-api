from rest_framework import serializers

from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    """Serializer for games"""

    class Meta:
        model = Game
        fields = ("id", "board", "status")
        extra_kwargs = {"status": {"read_only": True}}
