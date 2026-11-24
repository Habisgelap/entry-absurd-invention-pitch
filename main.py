#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt. The gate allows at most 220 chars.
"""

import os

ENTRY = "A desk lamp that files a formal noise complaint against your neighbour's leaf blower, then dims itself in protest until the whole street goes quiet."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: one sentence, within the 220-char gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 220, f"entry is {len(written)} chars, gate is 1-220"
    assert written.strip(), "entry must not be only whitespace"
    assert written.count(".") == 1 and written.endswith("."), "entry must be one sentence"
    print(f"wrote {len(written.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
