from pathlib import Path


def rename(path: Path) -> None:
    for i, file in enumerate(path.iterdir()):
        suff = file.suffix
        new_name = str(file)
        new_name = new_name.split("\\")
        new_name[-1] = f"0{i}{suff}"
        new_name = new_name[-1]
        filepath = directory.joinpath(new_name)
        try:
            file.rename(filepath)
        except:
            continue


directory = Path(r"path:\to\foulder")
rename(directory)
