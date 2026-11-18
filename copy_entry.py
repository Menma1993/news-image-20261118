#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the grader's output directory.

The image (entry.png, 1024x1024) is drawn at build time with Pillow and
committed beside this file. This program only copies bytes: no network,
no fonts, no third-party packages, standard library only.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
