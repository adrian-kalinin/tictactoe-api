import random

from rest_framework import serializers

from game.models import Game, GamePlayer, GameStatus


class GameSerializer(serializers.ModelSerializer):
    """A game object"""

    def validate_board(self, board):
        """Check that board is valid"""

        if len(board) != 9 or not all(c in "XO-" for c in board):
            raise serializers.ValidationError(
                "Ensure this field has 9 characters and contains only '-', 'X', or 'O'."
            )

        if self.instance:
            if self.instance.status != GameStatus.RUNNING:
                raise serializers.ValidationError("This game is already finished.")

            diff_indexes = [
                index
                for index in range(len(board))
                if self.instance.board[index] != board[index]
            ]

            if len(diff_indexes) == 0:
                raise serializers.ValidationError("A new move must be made.")

            if len(diff_indexes) >= 2:
                raise serializers.ValidationError(
                    "Only one move can be made at a time."
                )

            if self.instance.board[diff_indexes[0]] != "-":
                raise serializers.ValidationError(
                    "A player can only make a move in an empty cell."
                )

            x_count = board.count("X")
            o_count = board.count("O")
            x_previous = self.instance.board.count("X")
            o_previous = self.instance.board.count("O")

            if x_count > x_previous and o_count > o_previous:
                raise serializers.ValidationError(
                    "Both X and O cannot make a move in the same turn."
                )

            if self.instance.player == GamePlayer.X and (
                x_count == x_previous or o_count > o_previous
            ):
                raise serializers.ValidationError("X must make a move in this turn.")

            if self.instance.player == GamePlayer.O and (
                o_count == o_previous or x_count > x_previous
            ):
                raise serializers.ValidationError("O must make a move in this turn.")

        else:
            if (board.count("X") + board.count("O")) > 1:
                raise serializers.ValidationError(
                    "The board either must be empty or contain only one 'X' or 'O'."
                )

        return board

    def create(self, validated_data):
        """Create game, assign player and autoplay"""
        instance = super().create(validated_data)

        if not instance.player:
            if "X" in instance.board:
                instance.player = GamePlayer.X
            elif "O" in instance.board:
                instance.player = GamePlayer.O
            else:
                instance.player = random.choice(GamePlayer.values)

        instance.autoplay()
        instance.save()

        return instance

    def update(self, instance, validated_data):
        """Update game, autoplay and update status"""
        instance = super().update(instance, validated_data)

        instance.update_status()
        instance.autoplay()
        instance.update_status()
        instance.save()

        return instance

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
