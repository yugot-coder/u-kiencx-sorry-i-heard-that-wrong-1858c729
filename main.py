#!/usr/bin/env python3
"""Sorry, I Heard That Wrong - make.fun entry.

Prints exactly one line: the apology a smart speaker gives its owner
after mishearing them. Standard library only, fully deterministic.

The program also writes the same text to /output/entry.txt (no trailing
newline), which is where the make.fun program/v1 harness reads the entry;
the file write is best-effort and never affects stdout.
"""

import os
import sys

ENTRY = (
    "Sorry. You said 'wake me at seven,' I heard 'make me a Kevin,' "
    "so there's a man named Kevin in your kitchen."
)

# Gate: entry is one line of 1-140 characters, never just whitespace.
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), len(ENTRY)


def main() -> int:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass
    sys.stdout.write(ENTRY)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
