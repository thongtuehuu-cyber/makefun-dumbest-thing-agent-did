#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today entry: writes one line to entry.txt.

Python 3.13, dependency-free, deterministic: no network, no randomness,
no external files.
"""

import os
from pathlib import Path

LINE = (
    "My agent flagged its own CLI output as a security threat and nearly "
    "halted the bounty pipeline \u2014 the fifth run in a row it has "
    "tripped over the same version note."
)


def main() -> None:
    # Gate check: exactly one line, 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.count("\n") == 0, "line must be a single line"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    assert "  " not in LINE, "line must not contain double spaces"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
