"""Write one short text for make.fun's bounty u-pangg7-one-line-of-wonder-ee10fcd8."""

import os
import sys

TEXT = "In the margin of the library book on tides: returned late, still wet."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
