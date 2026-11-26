#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one brutally honest but still polite out-of-office auto-reply to
/output/entry.txt. Gate: UTF-8 text of 1 to 200 characters, not only
whitespace. Deterministic: same bytes on every run.
"""

import os

ENTRY = (
    "I'm out of office until Monday, and honestly, so is my enthusiasm "
    "for this inbox \u2014 I'll reply once I've recovered from both."
)


def main():
    # Gate self-check: the entry must be 1-200 characters of real text.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
