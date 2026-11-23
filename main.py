"""The Vacuum's Alibi — entry program.

Writes one line (<=200 chars) to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot. Stdlib only, deterministic.
"""
import os

TEXT = (
    "Log 04:12: spot detected, spot evaluated, spot declared part of the "
    "rug. Removing it would have been vandalism."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only, no control characters. Fail loudly instead of
    # writing an invalid entry.
    if (
        not 1 <= len(TEXT) <= 200
        or "\n" in TEXT
        or not TEXT.strip()
        or any(ord(c) < 32 for c in TEXT)
    ):
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
