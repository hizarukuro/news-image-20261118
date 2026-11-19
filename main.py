"""One Day · One Map — the front page of Wednesday 18 November 2026.

The finished page lives next to this file as entry.png. Running this
program delivers that page, untouched, into the output folder: the
folder named by the MAKEFUN_OUTPUT_DIR environment variable when it is
set, otherwise a folder called "output" in the working directory.

The copy is a plain byte-for-byte transfer, so the page that comes out
is exactly the page that was drawn, on every run. Only the Python
standard library is used.
"""

import os
import shutil
import sys


def deliver() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
