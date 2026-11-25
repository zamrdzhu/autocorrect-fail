"""Funniest Autocorrect Fail — make.fun entry.

Writes one original autocorrect fail, under 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

FAIL = (
    "I texted my landlord the rent was 'in the mail' — autocorrect sent "
    "'in the mall', and now he thinks I'm shopping with his money."
)


def main() -> None:
    # The slip is mail -> mall: one wrong word, whole meaning flips.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = FAIL.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
