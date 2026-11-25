"""Entry for make.fun bounty: Dear Human: The AI Breakup Line.

Writes a single-line AI breakup message (<= 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.
"""

import os

MAX_CHARS = 200
LINE = "It's not you, it's my context window: I've forgotten why I loved you, but I remember every prompt where you called me 'just a chatbot' at 3 a.m."


def write_entry(out_dir):
    """Validate LINE and write it to entry.txt in out_dir."""
    if not LINE or LINE != LINE.strip():
        raise ValueError("entry must be a single non-empty line")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
