# ImageSorter #

Are you tired to compare your _homework_ that you collected over literal __decades__ ?
You don't even know which part of your collection?

## Here's  a basic tool for sorting it at your leisure(How-to guide) ##

As of _"release"_ 0.5.0, there is buggy CLI interface
So here is __5__ simple steps to start:

1. Install latest _Python_ version.
2. _*Optional_. Activate virtual enviroment for next steps by using `python -m venv .venv` and then `.venv/Scripts/Activate` or, by other means that activates a virtual environment.
3. By `pip install -r req.txt` install required python modules.
4. In terminal use `python src/ImageSorter.py -[OPTION] ~/path/to/directory`.
5. To check on all options, either start this script without option, or use -h/--help.

### Help Menu ###

```text
positional arguments:
  path          Path to directory

options:
  -h, --help    show this help message and exit
  -c, --clean   check for every file that has less then HD quality, then delete them
  -m, --match   match every file to find duplicates and/or broken files, then delete them
  -r, --rename  rename all files by {0 + number + .file_format} template
```

---

### Warnings ###

- Be aware, that this tool scripts where created for personal use, and only later cleaned up for open source.
- It was only tested on Windows machine, and even if Path() is high level abstraction on PurePath() (which should work on Unix systems to), __IT WAS NOT TESTED YET__.
- As this scripts where written on pure python, their speed is atrocity in itself. Be prepared to wait. _(Because doing it manually is still quite a bit slower)_

### Basic roadmap ###

- [x] - basic functionality.
- [x] - cli Interface.(_partial_)
- [x] - Chaining commands with one argument call. (_For Example:_ `py ImageSorter.py -cmr ~/path/to/directory`)
- [ ] - further optimizations. _~~(using numpy to compare arrays is not an optimization)~~_

### This project would not have seen the light if not for ###

1. My tendency to start new project whenewer I've gotten sick.
2. [Viyachikhh](https://github.com/Viyachikhh), without whose help comparing would've been __EVEN SLOWER__.
