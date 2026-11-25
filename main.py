#!/usr/bin/env python3
"""The Tired Dark Lord — a make.fun entry.

The program writes one text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a monologue of exactly 100 words spoken
by a fantasy villain who is secretly just very tired. The tiredness
lives in the voice — the call for tea, the leaning candles, the heavy
cloak, the prophecy postponed until he has sat down — while his doom
engine still wakes at dawn. The text is 526 characters, inside the
competition's gate of 1 to 600 characters of UTF-8 text. Standard
library only, no network, and deterministic: the same bytes every run.
"""

import os

MONOLOGUE = (
    "Ten thousand years I have rehearsed this speech, and still the torches "
    "gutter when I need the light. Guards! Tea, strong tea. No \u2014 the war "
    "council first. I conquered the Nine Valleys on four hours' sleep a "
    "night, and I would conquer them again, if the throne did not creak so "
    "sweetly at midnight. The candles lean. So do I, quietly. My doom engine "
    "wakes at dawn. Everything I own wakes at dawn. Fetch my cloak, the "
    "heavy one. A dark lord's shoulders are so cold, and the prophecy \u2014 "
    "the prophecy can wait until I have sat down."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the monologue: no trailing newline, so
    # the text the judge reads is the monologue itself, byte for byte —
    # the gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(MONOLOGUE)


if __name__ == "__main__":
    main()
