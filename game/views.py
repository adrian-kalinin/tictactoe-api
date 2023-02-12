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
                description="Returns an array of games or an empty array",
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
                response=GameSerializer, description="Returns the game"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
    update=extend_schema(
        description="Post a new move to a game.",
        responses={
            200: OpenApiResponse(
                response=GameSerializer, description="Move successfully registered"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    ),
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
        "put",
        "delete",
        "options",
    ]

    def create(self, request, *args, **kwargs):
        """Return location link if game is successfully created"""
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            game = Game.objects.get(id=response.data.get("id"))
            serializer = GameLocationSerializer(game, context={"request": self.request})
            headers = self.get_success_headers(serializer.data)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )

        return response
