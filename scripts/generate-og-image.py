#!/usr/bin/env python3
"""Render og-image.jpg from the portfolio hero UI template."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = Path(__file__).resolve().parent / "og-image.html"
OUT = ROOT / "assets" / "img" / "og-image.jpg"


def find_chrome() -> str:
    for candidate in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(candidate)
        if path:
            return path
    raise RuntimeError("Chrome/Chromium not found")


def generate() -> None:
    chrome = find_chrome()
    html_url = HTML.resolve().as_uri()
    subprocess.run(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1200,630",
            f"--screenshot={OUT}",
            html_url,
        ],
        check=True,
    )
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    generate()
