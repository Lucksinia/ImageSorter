from pathlib import Path
from PIL import Image


def clean(path: Path) -> None:
    target_dir = directory
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


directory = Path(r"path:\to\foulder")
clean(directory)
