# copy-bandcamp-downloads

**Python script to unzip and extract all your Bandcamp downloads to a directory of your choice**

* **[About](#about)**
* **[Notes](#notes)**
* **[How to use](#how-to-use)**
  * **[Requirements](#requirements)**
  * **[Installation](#installation)**
  * **[Running](#running)**
    * ***[Arguments](#arguments)***

<a name="About"></a>
# About

I wrote this quick script to solve yet another personal (yet specific) problem: make it faster to extract Bandcamp purchases to my music folder!

<a name="Notes"></a>
# Notes
- I've only run this on Python 3.x on WSL2 running Ubuntu. I haven't tested it on other OSes, or other minor versions of Python 3.x.

- This script assumes your downloads are in zip files. It doesn't handle individual songs (main reason being a huge portion of my purchases are full albums and I wasn't interested in handling this case).

- Your downloads should be FLAC or MP3. Extracting metadata from WAV files isn't supported.

- Make sure all your downloads are together in the same folder, as the script will go through all ZIP files in the directory you give it!

<a name="how-to-use"></a>
# How to use

<a name="requirements"></a>
## Requirements
* `python` >= 3.10.6 (other versions of python3 may work, untested)
* `pip` (needed to install required 3rd party packages to run the script, below)

<a name="installation"></a>
## Installation

1. From a directory of your choice, clone this repo with
```sh
git clone https://github.com/helmetroo/copy-bandcamp-downloads.git
```

2. Install required python packages used by this script (`mutagen` and `sanitize_filename`).
```sh
python3 -m pip install mutagen
```

```
python3 -m pip install sanitize-filename
```

3. Change into the directory of the cloned repo. Make sure the script is executable.
```sh
cd copy-bandcamp-downloads
```

```sh
chmod +x copy-bandcamp-downloads.py
```

<a name="running"></a>
## Running

Example usage:

```sh
./copy-bandcamp-downloads.py $SRC_DIR $DEST_DIR --verbose --dry-run
```

When run, the script will examine each ZIP file in `$SRC_DIR` and extract all its files to the `$DEST_DIR` under this pattern: `$DEST_DIR/Artist name/Album name`.
(This is the iTunes convention.) See arguments below for what to provide.

<a name="arguments"></a>
### Arguments
- First argument is an absolute path to the directory containing all your downloads. **Make sure it only contains your music downloads before running this!**
- Second argument is an absolute path to the directory where your extracted music will go.
- `--verbose` or `-v`: Set this flag if you'd like to see which ZIP files are currently being processed as the script is being run.
- `--dry-run` or `-t`: Set this flag if you don't want any files to be copied (ZIP files will only be examined). Useful with `--verbose`.
