"""Front page of Wednesday 18 November 2026: forty-four stories, one image.

Copies the pre-rendered front page (entry.png, which sits beside this
program in the repository) into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable, falling back to a directory
named "output" when that variable is unset. The copy is byte-for-byte
identical on every run: the same file is read and written unchanged.
"""

import os
import shutil
import sys


def main() -> int:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base_dir, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    # copyfile moves bytes unchanged, so the output is identical every run.
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
