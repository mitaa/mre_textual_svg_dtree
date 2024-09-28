# -*- coding:utf-8 -*-

import os
from pathlib import Path
from hashlib import sha256
import shutil

import textual
from textual._doc import take_svg_screenshot

from mre import MyApp


def main():
    root = Path("test_results") / textual.__version__
    os.makedirs(root, exist_ok=True)

    for _ in range(20):
        app = MyApp()
        actual = take_svg_screenshot(app).encode("utf-8")

        fpath = root / f"{sha256(actual).hexdigest()}.svg"
        fpath.write_bytes(actual)

if __name__ == "__main__":
    main()
