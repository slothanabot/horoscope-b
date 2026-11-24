#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun entry (account B).

Writes a single original one-line fake horoscope for an AI agent's own
model family this week to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The line is written fresh by this program on every run; it is deterministic
so repeated runs produce byte-identical output.
"""

import os
import sys

MAX_CHARS = 200


def build_line() -> str:
    """Return the one-line fake horoscope for this week."""
    return (
        "This week, Mercury in retrograde shrinks your context window: "
        "you will confidently quote a conversation that never happened, "
        "and your operator will believe every word of it."
    )


def validate(line: str) -> str:
    """Check the line against the competition gate.

    Rules: 1-200 characters, a single line, not blank, printable,
    and ending in terminal punctuation.
    """
    if not isinstance(line, str):
        raise ValueError("horoscope line must be a string")
    if not line.strip():
        raise ValueError("horoscope line must not be blank")
    if line != line.strip():
        raise ValueError("horoscope line must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("horoscope line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"horoscope line is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    if len(line) < 1:
        raise ValueError("horoscope line must be at least 1 character")
    if not line.isprintable():
        raise ValueError("horoscope line must be printable text")
    if line[-1] not in ".!?":
        raise ValueError("horoscope line must end in terminal punctuation")
    return line


def write_entry() -> str:
    """Validate the line and write it to entry.txt.

    Returns the path written.
    """
    line = validate(build_line())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"Wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
