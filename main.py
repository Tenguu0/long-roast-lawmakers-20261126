"""Long Roast entry: write one satirical sentence to /output/entry.txt.

The competition (make.fun, program/v1) runs this program in a sandbox with
no network. The program writes a single sentence (1-320 chars) roasting
lawmakers who would regulate AI, crypto or the internet but cannot convert
a file to PDF. The sealed gate scorer checks /output/entry.txt is UTF-8
text of 1 to 320 characters.
"""

import os

ENTRY = (
    "The senator who wrote the bill to regulate artificial intelligence "
    "just emailed his staff a Word file called FINAL_final_v2_ACTUALLY_FINAL "
    "and asked if someone could turn it into a PDF for him."
)


def main() -> None:
    # The grader expects the text at /output/entry.txt. Fall back to a
    # local ./output directory when /output is not writable (local runs).
    text = ENTRY
    assert 1 <= len(text) <= 320, "entry must be 1-320 characters"
    assert text.strip(), "entry must not be only whitespace"
    for out_dir in ("/output", "output"):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"wrote {len(text)} chars to {path}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
