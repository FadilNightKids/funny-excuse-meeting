#!/usr/bin/env python3
"""Entry for make.fun "The Funniest Excuse for Skipping a Meeting".

Writes one line of text (<= 200 characters) to /output/entry.txt.
The code is only the wrapper; the text is the entry.
The write is atomic, so a crash can never leave a partial file graded.
"""

import os
import tempfile
from pathlib import Path

EXCUSE = (
    "I'll be there in spirit. The spirit read the agenda and has also declined."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"entry must be 1..200 characters, got {len(EXCUSE)}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write: a crash mid-write can never leave a partial entry graded.
    fd, tmp = tempfile.mkstemp(dir=OUT.parent, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(EXCUSE)
        os.replace(tmp, OUT)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
