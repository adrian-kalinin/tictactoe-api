from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.response import Response

from game.models import Game
from game.serializers import GameLocationSerializer, GameSerializer


@extend_schema_view(
    list=extend_schema(
        description="Get all games.",
        responses={
            200: OpenApiResponse(
                response=GameSerializer,
                description=(
                    "Successful response, returns an array of games, "
                    "returns an empty array if no users found"
                ),
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
    create=extend_schema(
        description="Start a new game.",
        responses={
            201: OpenApiResponse(
                response=GameLocationSerializer,
                description="Game successfully started",
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
    retrieve=extend_schema(
        description="Get a game.",
        responses={
            200: OpenApiResponse(
                response=GameSerializer,
                description="Successful response, returns the game",
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
    # update=extend_schema(description="Post a new move to a game."),
    destroy=extend_schema(
        description="Delete a game.",
        responses={
            200: OpenApiResponse(description="Game successfully deleted"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
)
class GameViewSet(viewsets.ModelViewSet):
    """API for games"""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = [
        "get",
        "post",
        # "put",
        "delete",
        "options",
    ]

    def create(self, request, *args, **kwargs):
        """Return location link if game is successfully created"""
        response = super().create(request, *args, **kwargs)

        # Check the game was created
        if response.status_code == status.HTTP_201_CREATED:
            # Fetch created game object
            game = Game.objects.get(id=response.data.get("id"))
            # Use a different serializer for game location
            serializer = GameLocationSerializer(game, context={"request": self.request})
            # Get response headers
            headers = self.get_success_headers(serializer.data)

            # Return response with game location and 201 status
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )

        return response
