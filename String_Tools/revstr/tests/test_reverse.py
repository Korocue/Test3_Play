import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from reverse import reverse_string  # noqa: E402


def test_reverse_basic():
    assert reverse_string("hello") == "olleh"


def test_reverse_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_empty_string():
    assert reverse_string("") == ""


@pytest.mark.parametrize(
    "original, expected",
    [
        ("12345", "54321"),
        ("パイソン", "ンソイパ"),
        ("AaBbCc", "cCbBaA"),
    ],
)
def test_reverse_various_inputs(original, expected):
    assert reverse_string(original) == expected
