#!/usr/bin/env python3
"""Entry for make.fun "The Funniest Excuse for Skipping a Meeting".

Writes one line of text (<= 200 characters) to /output/entry.txt.
The code is only the wrapper; the text is the entry.
"""

from pathlib import Path

EXCUSE = (
    "I'd join, but I've been staring at the invite so long "
    "I've started identifying as an optional guest."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()