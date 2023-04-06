from pathlib import Path
from PIL import Image

directory = Path(r"Path\to\foulder")
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
print(f"There is {len(to_delete)} files that not even HD")
print("Proseed?(y/n)")
if not input("~> ").lower().startswith("y"):
    quit()
else:
    lst = []
    for i, filepath in enumerate(to_delete):
        lst.append(i)
        filepath.unlink()
