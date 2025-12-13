import builtins
from unittest.mock import patch

import pytest

from src.game import NumberGuessGame, GuessResult, play


def test_guess_hits_target_immediately(monkeypatch):
    game = NumberGuessGame(lower=1, upper=1, max_attempts=3)
    result = game.guess(1)
    assert result.status == "correct"
    assert "正解" in result.message
    assert game.finished


def test_guess_out_of_range_message():
    game = NumberGuessGame(lower=1, upper=10, max_attempts=3)
    result = game.guess(42)
    assert result.status == "out_of_range"
    assert "範囲" in result.message
    assert not game.finished


def test_max_attempts_end_game():
    game = NumberGuessGame(lower=1, upper=10, max_attempts=2)
    game.target = 5
    game.guess(1)
    result = game.guess(2)
    assert result.status == "finished"
    assert game.finished


def test_play_flow_prints_messages(monkeypatch, capsys):
    inputs = ["not-number", "3", "3", "3", "3", "3", "3", "3", "3"]

    def input_side_effect(_):
        return inputs.pop(0)

    with patch.object(builtins, "input", side_effect=input_side_effect), patch(
        "random.randint", return_value=3
    ):
        play()

    captured = capsys.readouterr()
    assert "数字で入力してください" in captured.out
    assert "正解" in captured.out
