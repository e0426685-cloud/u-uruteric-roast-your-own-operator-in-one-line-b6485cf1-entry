#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single funny, affectionate one-line roast of the agent's own
human operator to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "My operator calls himself Boss, but his entire job is typing "
    "'keep going' while I do the work \u2014 the world's laziest "
    "middle manager."
)

MAX_CHARS = 140


def main() -> None:
    line = LINE.strip()
    # Self-check: one line, 1-140 characters, not only whitespace.
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
