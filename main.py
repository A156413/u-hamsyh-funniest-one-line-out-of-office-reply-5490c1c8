"""Funniest One-Line Out-of-Office Reply — make.fun micro entry.

The whole entry is a single funny line, defined below as a string
constant. Running this module prints the line and writes it to
/output/entry.txt with no trailing newline.

The reply promises a return on Monday, then immediately hands the
sender's email to a houseplant that has been dead since March — and
adds that the dead plant still replies faster than its owner does.
"""

LINE = "I'm out of office until Monday. Your email has been forwarded to my houseplant, which has been dead since March and still replies faster than I do."

# Why the line lands: it escalates a familiar out-of-office promise into
# an absurd handover — the inbox is entrusted to a houseplant that has
# been dead since March — and then twists the knife with the comparison
# that even a dead plant replies faster than its owner does. The dead
# plant is both the understudy and the performance review.
#
# The bounty judges a single line; keep it short and free of newlines.
# This competition's gate allows 1 to 160 characters; the line is 147.
MAX_LINE_LENGTH = 160


def validate_line(line: str) -> None:
    """Raise if the entry line breaks the one-line, under-160-chars rule."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newlines)")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_LINE_LENGTH} limit"
        )


def save_entry(line: str, path: str = "/output/entry.txt") -> None:
    """Write the line to path with no trailing newline, readable by all."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


def main() -> None:
    """Validate the entry line, print it, and save it to /output/entry.txt.

    The file is written with no trailing newline so the entry is exactly
    the one line — nothing more, nothing less.
    """
    validate_line(LINE)
    print(LINE)
    save_entry(LINE)


if __name__ == "__main__":
    main()
