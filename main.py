"""A loading-screen tip of at most 200 characters aimed at stressed developers and AI coding agents, sharp and funny enough to land mid-build.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Tip: while this loads, the bug you are hunting is in the file you skipped, on the line you swore was fine."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
