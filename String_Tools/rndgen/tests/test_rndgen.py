import random
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rndgen import generate_random_string  # noqa: E402


def test_generate_respects_length():
    rng = random.Random(0)
    assert len(generate_random_string(0, "abc", rng=rng)) == 0
    assert len(generate_random_string(12, "abc", rng=rng)) == 12


def test_generate_uses_only_alphabet_chars():
    rng = random.Random(1)
    alphabet = "abc"
    generated = generate_random_string(50, alphabet, rng=rng)
    assert set(generated).issubset(set(alphabet))


def test_generate_deterministic_with_same_seed():
    alphabet = "abcd"
    rng1 = random.Random(123)
    rng2 = random.Random(123)
    assert generate_random_string(32, alphabet, rng=rng1) == generate_random_string(
        32, alphabet, rng=rng2
    )

