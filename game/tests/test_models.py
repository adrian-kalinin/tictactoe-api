from django.test import TestCase

from game.models import Game, GameStatus


class GameModelTestCase(TestCase):
    """Test Game model"""

    def test_create_game(self):
        """Test creating a new game"""
        game = Game.objects.create(board="XO--X--OX", status=GameStatus.X_WON)
        game_display = f"'{game.board}' ({game.get_status_display()})"
        self.assertEqual(str(game), game_display)
