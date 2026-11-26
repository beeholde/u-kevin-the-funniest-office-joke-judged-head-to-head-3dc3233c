#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest Office Joke, Judged Head to Head".

The entry is a single office joke, held in the JOKE constant below.
Running this file checks the joke against the competition's gate
(plain UTF-8, one line, 1-200 characters, more than blank) and then
writes it to /output/entry.txt exactly as written, with no trailing
newline. Nothing else is written; the joke is the whole entry.

Only the Python standard library is used, so the program runs in
the grader's sandbox with no network and no extra packages.
"""

import sys
from pathlib import Path

JOKE = "Our intern asked why we print emails just to scan them back in, and now he runs the department."

OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200
# The rules require at least one visible character: a joke of only
# whitespace fails the gate, so the lower bound is checked first.
MIN_CHARS = 1


def check_joke(text: str) -> None:
    """Raise SystemExit with a plain message if the joke breaks a rule."""
    stripped = text.strip()
    if text != stripped:
        sys.exit("error: joke must not have leading or trailing whitespace")
    if len(stripped) < MIN_CHARS:
        sys.exit("error: joke is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        sys.exit("error: joke must fit on one line")
    if len(stripped) > MAX_CHARS:
        sys.exit(
            "error: joke is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    # A plain str in CPython is already valid Unicode, so this encode
    # round-trip is a cheap guard against a non-text constant sneaking
    # in during a future edit; it never fires on the current joke.
    try:
        stripped.encode("utf-8")
    except UnicodeEncodeError:
        sys.exit("error: joke is not plain UTF-8 text")


def main() -> None:
    check_joke(JOKE)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(JOKE, encoding="utf-8", newline="")
    print("wrote %d characters to %s" % (len(JOKE), OUT_PATH))


if __name__ == "__main__":
    main()
