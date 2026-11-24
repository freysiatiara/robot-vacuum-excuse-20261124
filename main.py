#!/usr/bin/env python3
"""Write the robot vacuum's one-line excuse to /output/entry.txt.

Stdlib only. No trailing newline: the entry is exactly the line.
"""

import os

LINE = (
    "I didn't miss that spot \u2014 my cliff sensor saw the rug fringe, "
    "screamed 'stairs,' and I reversed before I fell to my death."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(
            "entry must be 1..140 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line, no newline characters")

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
