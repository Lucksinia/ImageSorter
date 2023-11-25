from pathlib import Path
from PIL import Image, ImageFile
import numpy as np
import argparse

# for specific images, whoose bytes are correct, but one part of data is broken
ImageFile.LOAD_TRUNCATED_IMAGES = True


def cleaning(path: Path) -> None:
    """Function that finds all files in given directory and prompts to delete them
       if they are at leas HD quality

    :param Path path: Path to the worked on directory
    """
    target_dir = path
    to_save = []
    to_delete = []
    for i, file in enumerate(target_dir.iterdir()):
        with Image.open(file) as img:  # TODO: find a way to not open images(fully)
            amount = img.size[0] * img.size[1]
            if amount >= 921600:  # minimal HD px amount
                to_save.append(file)
            else:
                to_delete.append(file)

    if not len(to_delete):
        print("There is no files that are not at least HD")
    else:
        print(f"There is {len(to_delete)} files that not at least HD")
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
    """Function to compare difference in data between two images.

    :param Image baseimg: Pillow Image that is compared with others
    :param Image compared: Pillow image that is compared to the base one.
    :return bool: if equal return False
    """
    try:
        np1 = np.asarray(baseimg)
        np2 = np.asarray(compared)
        return np.equal(np1, np2).all()
    except:
        return False


def matching(path: Path) -> None:
    """Function that contains matching logic for files.

    :param Path path: Path to the worked on directory
    """
    to_delete = set()  # final set for files that needed to be deleted
    to_skip = set()
    gen = list(path.iterdir())
    for file in range(len(gen)):
        with Image.open(gen[file]) as img:
            subgen = gen[file + 1 :]
            for second_file in subgen:
                with Image.open(second_file) as img2:
                    cond2 = img.size == img2.size and img.mode == img2.mode
                    cond3 = second_file not in to_delete and second_file not in to_skip
                    if cond2 and cond3:  # if they are the same dimensions
                        if difference(img, img2):  # if their bytearrays are NOT equal
                            to_delete.add(second_file)
                            to_skip.add(second_file)
        print(f"worked file: @{file} {gen[file]}")
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
    """Function that renames all files as a `0 + number of file + file suffix`

    :param Path path: Path to the worked on directory
    """
    # TODO: Implement naming template change
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
    """Cli interface for this Sorter"""
    parser = argparse.ArgumentParser(prog="image-sort")
    parser.add_argument(
        "path",
        type=Path,
        nargs="?",
        help="Path to directory",
        default=Path.cwd(),
    )
    parser.add_argument(
        "-c",
        "--clean",
        action="store_true",
        help="check for every file that has less then HD quality, then delete them",
    )
    parser.add_argument(
        "-m",
        "--match",
        action="store_true",
        help="match every file to find duplicates and/or broken files, then delete them",
    )
    parser.add_argument(
        "-r",
        "--rename",
        action="store_true",
        help="rename all files by {0 + number + .file_format} template",
    )
    args = parser.parse_args()
    if args.clean:
        cleaning(args.path)
    if args.match:
        matching(args.path)
    if args.rename:
        renaming(args.path)


if __name__ == "__main__":
    main()
