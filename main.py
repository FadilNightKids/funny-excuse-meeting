#!/usr/bin/env python3
"""Entry for make.fun "The Funniest Excuse for Skipping a Meeting".

Writes one line of text (<= 200 characters) to /output/entry.txt.
The code is only the wrapper; the text is the entry.
"""

from pathlib import Path

EXCUSE = (
    "I'd join, but I've been marked optional so many times "
    "I've started taking it personally."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"entry must be 1..200 characters, got {len(EXCUSE)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()