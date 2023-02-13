from django.test import TestCase

from game.models import Game, GamePlayer, GameStatus


class GameModelTestCase(TestCase):
    """Test Game model"""

    def test_str(self):
        """Test creating a new game"""
        game = Game.objects.create(board="XO--X--OX", status=GameStatus.X_WON)
        self.assertEqual(str(game), "'XO--X--OX' (X won)")

    def test_autoplay(self):
        """Test autoplay functionality"""
        game = Game.objects.create(board="----X----", player=GamePlayer.X)
        game.autoplay()

        self.assertEqual(game.board.count("-"), 7)
        self.assertEqual(game.board.count("X"), 1)
        self.assertEqual(game.board.count("O"), 1)

    def test_update_status(self):
        """Test updating status"""
        game_1 = Game.objects.create(board="OO-XXXO-X", player=GamePlayer.X)
        game_1.update_status()
        self.assertEqual(game_1.status, GameStatus.X_WON)

        game_2 = Game.objects.create(board="--OXO-OX-", player=GamePlayer.O)
        game_2.update_status()
        self.assertEqual(game_2.status, GameStatus.O_WON)

        game_3 = Game.objects.create(board="OXOOXXXOX", player=GamePlayer.X)
        game_3.update_status()
        self.assertEqual(game_3.status, GameStatus.DRAW)
