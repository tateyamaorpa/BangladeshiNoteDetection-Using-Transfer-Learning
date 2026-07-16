"""Batch-resize Bangladeshi Taka note images to 256x117 before training.

Usage: place source images in ../data/note_dataset/<denomination>/ and run
    python resize.py <denomination>
e.g. `python resize.py twohundred` resizes ../data/note_dataset/twohundred/.
"""
import os
import sys

from PIL import Image


def resize(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if not os.path.isfile(item_path):
            continue
        im = Image.open(item_path)
        f, _ = os.path.splitext(item_path)
        im_resized = im.resize((256, 117), Image.LANCZOS)
        im_resized.save(f + " resized.png", "PNG", quality=90)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize.py <denomination_folder_name>")
        sys.exit(1)
    resize(f"../data/note_dataset/{sys.argv[1]}/")
