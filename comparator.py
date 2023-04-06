from pathlib import Path
from PIL import Image
import numpy as np


def difference(baseimg: Image, compared: Image) -> bool:
    try:
        np1 = np.asarray(baseimg)
        np2 = np.asarray(compared)
        return np.equal(np1, np2).all()
    except:
        return False


def check_cmp(path: Path) -> None:
    to_delete = set()  # final list for files that needed to be deleted
    to_skip = set()
    gen = list(path.iterdir())
    for file in range(len(gen)):
        img = Image.open(gen[file])
        subgen = gen[file + 1 :]
        for second_file in subgen:
            img2 = Image.open(second_file)
            cond2 = img.size == img2.size and img.mode == img2.mode
            cond3 = second_file not in to_delete and second_file not in to_skip
            if cond2 and cond3:  # if they are the same dimensions
                if difference(img, img2):  # if their bytearrays are NOT equal
                    to_delete.add(second_file)
                    to_skip.add(second_file)
            img2.close()
        img.close()
        print(f"worked file: @{file} {gen[file]}")
        to_skip.add(file)
    print(f"There is {len(to_delete)} files that are broken or a copy of another")
    print("Proseed?(y/n)")
    if not input("~> ").lower().startswith("y"):
        quit()
    else:
        for filepath in to_delete:
            filepath.unlink()


directory = Path(r"Path\to\foulder")
check_cmp(directory)
