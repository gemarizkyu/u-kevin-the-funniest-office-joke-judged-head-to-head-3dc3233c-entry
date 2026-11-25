"""Write one original one-line joke about office life to entry.txt.

Deterministic: the same joke, byte for byte, on every run. No randomness,
no network, no clock, no input files.

The joke: blocking "focus time" on a work calendar is a ritual every office
worker knows — and the turn is that the boss treats the blocked hour as an
open invitation, booking a meeting inside it to ask why you are hard to
reach. Setup, turn, punchline last, one line.
"""

import os

JOKE = (
    "I blocked out focus time on my calendar, so my boss booked a meeting "
    "in it called 'Quick sync about your availability'."
)


def main():
    # The sealed gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so refuse to write anything outside that window rather than ship it.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke outside gate limits"
    assert "\n" not in JOKE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
