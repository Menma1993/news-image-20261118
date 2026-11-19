#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the grader output directory.

Stdlib only. The image is drawn at build time (see
news-image-20261118-v3-work/draw_v3.py in the builder's workspace) and
committed here as entry.png; this program just moves it to the output
directory. The output directory honours MAKEFUN_OUTPUT_DIR when set,
otherwise it defaults to /output. No network, no fonts, no third-party
packages -- it runs in a stock python:3.13 image as `python3 -P -s main.py`.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
