# ImageSorter #

Are you tired to compare your _homework_ that you collected over literal __decades__ ?
You don't even know which part of your collection?

## Here some basic tools for sorting it at your leisure ##

- [cleaner](cleaner.py) - to delete all old stuff (_currently only saving HD and bigger resolutions_)
- [comparator](comparator.py) - to delete all copies of each file and corrupted ones.
- [re-namer](renamer.py) - to rename by `0 + number + .file_format` each and every file.

## How-to guide ##

As of release 0.0.1, there is no cli-interface ___YET.___
So here is __5__ simple steps to start:

1. Install latest _Python_ version.
2. _*Optional_. Activate virtual enviroment for next steps by using `python -m venv .venv` and then `.venv/Scripts/Activate` or, by other means.
3. By `pip install -r req.txt` install required python modules.
4. Change `directory = Path("Path\to\foulder")` to foulder in which you whant this script to work.
5. Run required module by either using IDE or `python path/to/desired/tool.py` in command line.

---

### Warnings ###

- Be aware, that this tool scripts where created for personal use, and only later cleaned up for open source.
- It was only tested on Windows machine, and even if Path() is high level abstraction on PurePath() (which should work on Unix systems to), __IT WAS NOT TESTED YET__.
- As this scripts where written on pure python, their speed is atrocity in itself. Be prepared to wait. _(Because doing it manually is still quite a bit slower)_

### Basic roadmap ###

- [x] - basic functionality.
- [ ] - cli Interface.
- [ ] - further optimizations. ~~(using numpy to compare arrays is not an optimization)~~

### This project would not have seen the light if not for ###

1. My tendency to start new project whenewer I've gotten sick.
2. [Viyachikhh](https://github.com/Viyachikhh), without whose help [comparator](comparator.py) would've been __EVEN SLOWER__.
