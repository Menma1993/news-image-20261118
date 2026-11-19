"""Move the pre-rendered entry image into the grader output directory."""
from os import environ, makedirs
from pathlib import Path
from shutil import copyfile


def run():
    root = Path(__file__).resolve().parent
    target = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    makedirs(target, exist_ok=True)
    copyfile(root / "entry.png", target / "entry.png")


run()
