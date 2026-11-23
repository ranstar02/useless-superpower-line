#!/usr/bin/env python3
"""Write one original, hilariously useless superpower one-liner to /output/entry.txt.

Entry for make.fun's "One Line, Zero Use: The Useless Superpower Sprint".
The power: stop time, but only while asleep -- so it never helps,
and the punchline lands on the last words: late anyway.
"""

import os

LINE = "I can stop time, but only while I'm asleep, so I always wake up exactly as late as I was going to be anyway."

assert len(LINE) <= 200, f"line too long: {len(LINE)} chars"
assert LINE.strip(), "line must not be blank"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-char one-liner to /output/entry.txt")


if __name__ == "__main__":
    main()
