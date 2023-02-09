from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from game.models import Game, GameStatus
from game.serializers import GameSerializer


class GameApiTestCase(TestCase):
    """Test game API"""

    def setUp(self):
        self.client = APIClient()

    def test_list_games(self):
        """Test retrieving all games"""
        Game.objects.create(board="XO--X--OX", status=GameStatus.X_WON)
        Game.objects.create(board="OX--O--XO", status=GameStatus.O_WON)

        game_list_url = reverse("game:game-list")
        response = self.client.get(game_list_url)

        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_game(self):
        """Test creating a new game"""
        data_set = [
            {"board": "---------"},
            {"board": "--X------"},
            {"board": "------O--"},
        ]

        game_list_url = reverse("game:game-list")

        for count, data in enumerate(data_set, start=1):
            response = self.client.post(game_list_url, data)
            games = Game.objects.all()

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data.get("status"), GameStatus.RUNNING)
            self.assertEqual(games.count(), count)

    def test_create_game_invalid_board(self):
        """Test creating a new game with an invalid board"""
        data_set = [
            {"board": "------------------"},
            {"board": "---abc---"},
            {"board": "-X-----O-"},
        ]

        game_list_url = reverse("game:game-list")

        for data in data_set:
            response = self.client.post(game_list_url, data)
            games = Game.objects.all()

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(games.count(), 0)

    def test_retrieve_game(self):
        """Test retrieving a game"""
        game = Game.objects.create(board="---------", status=GameStatus.RUNNING)

        game_detail_url = reverse("game:game-detail", kwargs={"pk": game.id})
        response = self.client.get(game_detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(game.id))

    def test_delete_game(self):
        """Test deleting a game"""
        game = Game.objects.create(board="OXXXOOOXX", status=GameStatus.DRAW)

        game_detail_url = reverse("game:game-detail", kwargs={"pk": game.id})
        response = self.client.delete(game_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertQuerysetEqual(Game.objects.all(), [])
