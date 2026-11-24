#!/usr/bin/env python3
"""Everyday Things, Two Lines — explains a traffic jam to a 10-year-old
through one concrete analogy, then says honestly what the analogy maps
and what it leaves out. Writes the two lines to /output/entry.txt.

Line 1: a traffic jam is a zipper stuck halfway — cars are the zipper's
teeth, locked together so none can slide past the one in front. It
explains the jam's mechanism, not just its look: one stuck tooth holds
the whole zipper still.
Line 2: the analogy maps the locking tooth by tooth and the slow crawl
once the stuck tooth frees itself, and it leaves out the drivers, the
horns, and the hurry — a real zipper has none of those.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

LINE1 = ("A traffic jam is a zipper stuck halfway, its car-teeth locked "
         "together so none of them can slide past the one in front.")
LINE2 = ("It maps how the cars lock together tooth by tooth and only "
         "crawl forward when the stuck one frees itself, but a real "
         "zipper has no drivers, no horns, and no one in a hurry.")

ENTRY = LINE1 + "\n" + LINE2

MAX_CHARS = 400


def validate(text):
    """Enforce the competition gate: 1-400 chars, not only whitespace,
    exactly two lines, no leading or trailing whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-400 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 400-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(
            f"entry must be exactly two lines, got {len(lines)}"
        )
    for i, line in enumerate(lines, 1):
        if line.strip() == "":
            raise ValueError(f"line {i} is empty")
        if line != line.strip():
            raise ValueError(f"line {i} has leading or trailing whitespace")
        if "\r" in line:
            raise ValueError(f"line {i} contains a carriage return")
        if not line.endswith("."):
            raise ValueError(
                f"line {i} must end with a full stop (one sentence)"
            )
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases."""
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 401, "401 chars"),
        ("one line only", "one line"),
        ("a\nb\nc", "three lines"),
        ("trailing \n", "trailing newline"),
        ("\nleading", "leading newline"),
        ("a \nb", "trailing whitespace on line 1"),
        ("a\n b", "leading whitespace on line 2"),
        ("A sentence\nNo full stop", "line 2 without full stop"),
        ("No full stop\nSecond line.", "line 1 without full stop"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundary: exactly 400 chars across two lines must pass
    validate("y" * 198 + "." + "\n" + "z" * 199 + ".")
    print("self-test ok: 400-char boundary accepted")
    # the entry itself must pass
    validate(ENTRY)
    print("self-test ok: entry accepted")
    print("self-test: all cases passed")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the lines
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
