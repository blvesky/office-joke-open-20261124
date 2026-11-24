"""Office joke entry writer.

Writes a single office joke to /output/entry.txt as UTF-8 text and
forces the output file mode to 0644 so the grader can read it.
"""

import os

# The joke text. Must stay within the 1-200 character gate.
ENTRY_TEXT = "I wrote 'per my last email' so politely that the reader apologised to me for a mistake I made."

OUTPUT_PATH = "/output/entry.txt"


def check_entry(text):
    """Raise if the entry breaks the contest gate (1-200 chars)."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))


def write_entry():
    """Validate the text, write it out, and lock the mode to 0644."""
    check_entry(ENTRY_TEXT)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    write_entry()
