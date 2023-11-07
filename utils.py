from pathlib import Path
from PIL import Image
import numpy as np
import argparse


def cleaning(path: Path) -> None:
    target_dir = path
    to_save = []
    to_delete = []
    for i, file in enumerate(target_dir.iterdir()):
        img = Image.open(file)  # TODO: find a way to not open images
        w, h = img.size
        amount = w * h
        if amount >= 921600:  # minimal HD px amount
            to_save.append(file)
        else:
            to_delete.append(file)
        img.close()

    if not len(to_delete):
        print("There is no files that are not at least HD")
    else:
        print(f"There is {len(to_delete)} files that not even HD")
        print("Proseed?(y/n)")
        if not input("~> ").lower().startswith("y"):
            print("Good bye then!")
            quit()
        else:
            lst = []
            for i, filepath in enumerate(to_delete):
                lst.append(i)
                filepath.unlink()


def difference(baseimg: Image, compared: Image) -> bool:
    try:
        np1 = np.asarray(baseimg)
        np2 = np.asarray(compared)
        return np.equal(np1, np2).all()
    except:
        return False


def matching(path: Path) -> None:
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
        # print(f"worked file: @{file} {gen[file]}")
        to_skip.add(file)

    if not len(to_delete):
        print("There is no files that are copies or broken")
    else:
        print(f"There is {len(to_delete)} files that are broken or a copy of another")
        print("Proseed?(y/n)")
        if not input("~> ").lower().startswith("y"):
            quit()
        else:
            for filepath in to_delete:
                filepath.unlink()


def renaming(path: Path) -> None:
    for i, file in enumerate(path.iterdir()):
        suff = file.suffix
        new_name = str(file)
        new_name = new_name.split("\\")
        new_name[-1] = f"0{i}{suff}"
        new_name = new_name[-1]
        filepath = path.joinpath(new_name)
        try:
            file.rename(filepath)
        except:
            continue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        type=Path,
        nargs="?",
        help="Path to directory",
        default=Path.cwd(),
    )
    parser.add_argument(
        "-c, -clean",
        action="store_true",
        help="Check for every file that has less then HD quality, then delete them",
    )
    parser.add_argument(
        "-m, -match",
        action="store_true",
        help="Matxh every file to find duplicates and/or broken files, then delete them",
    )
    args = parser.parse_args()
    if args.clean:
        cleaning(args.path)
    elif args.match:
        matching(args.path)


if __name__ == "__main__":
    main()
