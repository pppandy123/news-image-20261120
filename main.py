#!/usr/bin/env python3
"""news-image-20261120: output a one-page summary of world news on 20 Nov 2026.

The front page was rendered offline during development (see render.py) and
is stored in this repository as entry.png. At run time this program only
copies those bytes to /output/entry.png: no network, no randomness, no
clock, no environment input. The output is byte-identical on every run.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
