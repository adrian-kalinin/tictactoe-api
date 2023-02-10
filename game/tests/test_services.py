from django.test import TestCase

from game.services import GameService


class GameServiceTestCase(TestCase):
    def test_is_board_valid(self):
        """Test validating board contents"""
        self.assertTrue(GameService.is_board_valid("---------"))
        self.assertTrue(GameService.is_board_valid("XO--X--OX"))

        self.assertFalse(GameService.is_board_valid("123456789"))
        self.assertFalse(GameService.is_board_valid("----a----"))
        self.assertFalse(GameService.is_board_valid("X---------O"))

    def test_is_first_move_valid(self):
        """Test validating board with a possible first move"""
        self.assertTrue(GameService.is_first_move_valid("---------"))
        self.assertTrue(GameService.is_first_move_valid("--X------"))
        self.assertTrue(GameService.is_first_move_valid("-----O--"))

        self.assertFalse(GameService.is_first_move_valid("-------XO"))
        self.assertFalse(GameService.is_first_move_valid("OX--O--XO"))
