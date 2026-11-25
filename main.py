"""One Line, One Laugh — entry program.

Writes a single original one-liner to /output/entry.txt (or to the directory
named by the OUTPUT_DIR environment variable, for local verification).

The line is a fixed, deterministic string: no randomness, no network, no
input. Running this program twice produces byte-identical output.
"""

import os
import sys

LINE = (
    "My therapist told me to reconnect with my inner child, "
    "so I grounded him for lying about the dog."
)


def main() -> int:
    # Self-check against the gate before writing: 1-200 chars, not
    # whitespace-only, valid UTF-8 by construction (a str literal).
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print("error: line fails the 1-200 character gate", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Single line, no trailing newline: the line itself is the whole entry.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
