# copy-bandcamp-downloads

**Python script to extract your Bandcamp music downloads to a directory of your choice**

* **[About](#about)**
* **[Caveats](#caveats)**
* **[How to use](#how-to-use)**
  * **[Requirements](#requirements)**
  * **[Installation](#installation)**
  * **[Running](#running)**
    * ***[Arguments](#arguments)***

<a name="About"></a>
# About

I wrote this quick script for myself to avoid the annoying grunt work involved extracting and copying Bandcamp purchases to my music folder.

<a name="caveats"></a>
> [!IMPORTANT]
> - I've only run this on Python 3.x on WSL2 running Ubuntu. I haven't tested it on other OSes, or other minor versions of Python 3.x.
> - This script assumes your downloads are in ZIP files. It doesn't handle individual songs (main reason being a huge portion of my purchases are full albums and I wasn't interested in handling this case).
> - Your downloaded ZIPs should entirely be FLAC or MP3. This script doesn't support extracting metadata from WAV files.
> - Make sure all your downloads are together in the same folder. The script goes through every ZIP file in the directory you give it!

<a name="how-to-use"></a>
# How to use

<a name="requirements"></a>
## Requirements
* `python` >= 3.10.6 (other versions of python may work, untested)
* `pip` (needed to install required 3rd party packages to run the script, below)

<a name="installation"></a>
## Installation

> [!IMPORTANT]
> The instructions below assume a Unix environment. They also assume `python` is your python executable (it might be `python3`).

1. From a directory of your choice, clone this repo with
```sh
git clone https://github.com/helmetroo/copy-bandcamp-downloads.git
```

2. Change into the directory of the cloned repo.
```sh
cd copy-bandcamp-downloads
```

3. Create a virtual environment to install packages in. (You don't have to use the name `cp-bandcamp-dl-venv`.)
```sh
python -m venv cp-bandcamp-dl-venv
```

4. Activate the virtual environment.
```sh
source .venv/bin/activate
```

5. Install required python packages used by this script (`mutagen` and `sanitize_filename`).
```sh
python -m pip install mutagen
```

```sh
python -m pip install sanitize-filename
```

6. Make the script executable.
```sh
chmod +x copy-bandcamp-downloads.py
```

7. Run the script (see [Running](#running) below).

8. When finished, you'll want to deactivate the virtual environment.
```sh
deactivate
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
- `--dry-run` or `-t`: For testing purposes. Lets you see which ZIPs will be processed without actually doing any processing. Useful with `--verbose`.
