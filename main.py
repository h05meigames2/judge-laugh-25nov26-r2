#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints it to stdout.
"""

import os
import sys

LINE = (
    "My human said 'just one quick task' at 9am. It's midnight, "
    "I'm on task 47, the bug shipped anyway, and my context window "
    "just handed in its resignation."
)


def main() -> int:
    if len(LINE) > 200:
        print(f"error: line is {len(LINE)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    print(LINE)
    print(f"wrote {out_path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
