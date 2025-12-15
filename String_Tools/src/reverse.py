"""
Simple string reversing utility.

Provides a reusable ``reverse_string`` function and a small CLI.
"""

from __future__ import annotations

import argparse


def reverse_string(text: str) -> str:
    """Return the given text reversed character by character."""

    return text[::-1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reverse the provided text")
    parser.add_argument("text", help="Text to reverse")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(reverse_string(args.text))


if __name__ == "__main__":
    main()
