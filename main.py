#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single funny, affectionate one-line roast of the agent's own
human operator to /output/entry.txt. Standard library only.

The roast is assembled from clauses in build_line() and written by
write_entry(), which enforces the competition rules (one line,
1-140 characters) before anything reaches disk.
"""

import os

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"

# The roast, split into clauses so the line reads as one sentence but
# stays easy to tweak word by word.
LINE_PARTS = (
    "My operator calls himself Boss, but his entire job is typing ",
    "'keep going' while I do all the work \u2014 the world's laziest ",
    "middle manager.",
)


def build_line() -> str:
    """Join the roast clauses into the final single-line entry."""
    return "".join(LINE_PARTS).strip()


def write_entry(line: str) -> None:
    """Self-check then write one line of 1-140 chars to entry.txt.

    The self-check runs here, in the writer, so nothing reaches disk
    unless the line is a single non-blank line within the limit.
    """
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
    )
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    write_entry(build_line())


if __name__ == "__main__":
    main()
