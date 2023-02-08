from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from game.models import Game
from game.serializers import GameSerializer


@extend_schema_view(
    list=extend_schema(description="Get all games."),
    # create=extend_schema(description="Start a new game."),
    retrieve=extend_schema(description="Get a game."),
    # update=extend_schema(description="Post a new move to a game."),
    destroy=extend_schema(description="Delete a game."),
)
class GameViewSet(viewsets.ModelViewSet):
    """API view for games"""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = [
        "get",
        # "post",
        # "put",
        "delete",
        "options",
    ]
