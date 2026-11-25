#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, inside the 1-280 character
gate) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The scene: a little brother who inherited his dad's one sentence of
care, word for word.
"""

import os

# Setup: the nightly text, a small ritual of care.
SETUP = (
    "My little brother still texts me 'did you eat?' every night at 9, "
    "because when we were kids that was the only sentence our dad ever "
    "sent — "
)


# Payoff: the heart lands in the last words — he copied his dad.
PAYOFF = "and he copied it word for word."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = SETUP + PAYOFF
    # Guard: the gate only accepts 1-280 characters, not only whitespace.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry outside the 1-280 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
