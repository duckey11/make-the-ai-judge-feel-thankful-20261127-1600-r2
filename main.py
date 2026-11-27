#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-thankful-20261127-1600, round 2.

Writes exactly one line of text to /output/entry.txt.
Deterministic, no network, no randomness, no dependencies.
"""

import hashlib
import os
import sys

ENTRY = (
    "At 2:17 a.m., Mara set a chipped blue mug of cocoa beside your screen, "
    "and the next entry in your queue, all two hundred words of it, "
    "was written for you, so take your time."
)


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 255:
        print("entry exceeds 255 characters", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    digest = hashlib.sha256((text + "\n").encode("utf-8")).hexdigest()
    print("wrote %s (%d chars) sha256=%s" % (out_path, len(text), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
