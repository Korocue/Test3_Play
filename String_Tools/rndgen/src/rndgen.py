"""
Random string generator utility.

Usable as a standalone CLI and optionally able to integrate with `revstr`
by reversing the generated string via `revstr/src/reverse.py`.
"""

from __future__ import annotations

import argparse
import random
import secrets
import string
import sys
from pathlib import Path
from typing import Callable


def generate_random_string(
    length: int,
    alphabet: str,
    *,
    rng: random.Random | None = None,
) -> str:
    if length < 0:
        raise ValueError("length must be >= 0")
    if not alphabet:
        raise ValueError("alphabet must be non-empty")

    rng = rng or secrets.SystemRandom()
    return "".join(rng.choice(alphabet) for _ in range(length))


def build_alphabet(preset: str, *, no_ambiguous: bool) -> str:
    presets: dict[str, str] = {
        "alnum": string.ascii_letters + string.digits,
        "letters": string.ascii_letters,
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "digits": string.digits,
        "hex": "0123456789abcdef",
        "base64url": string.ascii_letters + string.digits + "-_",
        "printable": "".join(ch for ch in string.printable if not ch.isspace()),
    }

    try:
        alphabet = presets[preset]
    except KeyError as exc:
        raise ValueError(f"unknown preset: {preset}") from exc

    if no_ambiguous:
        ambiguous = set("0O1lI")
        alphabet = "".join(ch for ch in alphabet if ch not in ambiguous)

    if not alphabet:
        raise ValueError("alphabet became empty (check options)")
    return alphabet


def _import_revstr_reverse_string() -> Callable[[str], str]:
    string_tools_dir = Path(__file__).resolve().parents[2]
    revstr_src = string_tools_dir / "revstr" / "src"
    if not revstr_src.exists():
        raise RuntimeError(f"revstr src not found: {revstr_src}")
    if str(revstr_src) not in sys.path:
        sys.path.insert(0, str(revstr_src))

    try:
        from reverse import reverse_string  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("failed to import revstr's reverse_string") from exc

    return reverse_string


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate random strings")
    parser.add_argument(
        "length",
        type=int,
        nargs="?",
        default=16,
        help="Length of the generated string (default: 16)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="How many strings to generate (default: 1)",
    )
    parser.add_argument(
        "--preset",
        choices=[
            "alnum",
            "letters",
            "lower",
            "upper",
            "digits",
            "hex",
            "base64url",
            "printable",
        ],
        default="alnum",
        help="Predefined character set (default: alnum)",
    )
    parser.add_argument(
        "--alphabet",
        help="Custom character set (overrides --preset)",
    )
    parser.add_argument(
        "--no-ambiguous",
        action="store_true",
        help="Remove ambiguous characters like 0/O and 1/l/I",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Seed for deterministic output (not cryptographically secure)",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Reverse the generated string locally",
    )
    parser.add_argument(
        "--revstr",
        action="store_true",
        help="Reverse the generated string via revstr (imports revstr/src/reverse.py)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.count < 1:
        raise SystemExit("--count must be >= 1")

    alphabet = args.alphabet or build_alphabet(args.preset, no_ambiguous=args.no_ambiguous)
    rng: random.Random | None = random.Random(args.seed) if args.seed is not None else None

    revstr_reverse = _import_revstr_reverse_string() if args.revstr else None

    for _ in range(args.count):
        generated = generate_random_string(args.length, alphabet, rng=rng)
        if args.reverse:
            generated = generated[::-1]
        if revstr_reverse is not None:
            generated = revstr_reverse(generated)
        print(generated)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

