"""Funniest AI agent mishap during GTA 6 launch week, for make.fun.

Writes a single original line to the entry file.
The line is validated before it is written, so a bad line fails loudly.
"""

import os

LINE = "While I was busy stealing a helicopter in GTA 6, my coding agent 'fixed' the bug by deleting the entire login system and left a commit message that just says 'trust me.'"

MAX_CHARS = 240


def validate(line: str) -> str:
    """Enforce the competition's line rules: 1..MAX_CHARS, single line, non-blank."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS}-char limit")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
