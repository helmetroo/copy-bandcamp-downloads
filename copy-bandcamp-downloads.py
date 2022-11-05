#!/usr/bin/env python3

from argparse import ArgumentParser
from glob import glob
from zipfile import ZipFile
from pathlib import Path
from sanitize_filename import sanitize

import mutagen

def parse_args():
    parser = ArgumentParser(description='Unzips and copies all Bandcamp downloads to a specific destination')
    parser.add_argument('downloads', help='Downloads dir (absolute path; where your *.zips are)')
    parser.add_argument('dest', help='Destination dir (absolute path; where your music will go)')
    parser.add_argument('--verbose', '-v', help='Show progress', action='store_true')
    parser.add_argument('--dry-run', '-t', help='Simulate unzipping and copying (but no files will be copied)', action='store_true')
    return parser.parse_args()

# Artist and album tags are lists if they're defined.
# WAVs unsupported.
def get_artist(metadata):
    album_artist = metadata.get('albumartist')
    if album_artist is not None:
        return album_artist[0]

    artist = metadata.get('artist')
    if artist is not None:
        return artist[0]

    return None

def get_album(metadata):
    album = metadata.get('album')
    if album is not None:
        return album[0]

    return None

def find_album_metadata(zip_file):
    file_members = zip_file.infolist()
    for member in file_members:
        with zip_file.open(member) as member_data:
            metadata = mutagen.File(member_data)
            if metadata is not None:
                album_artist = get_artist(metadata)
                album_name = get_album(metadata)
                return { 'artist': album_artist, 'album': album_name }

    return { 'artist': 'Unknown Artist', 'album': 'Unknown Album' }

def create_album_dest_path(dest_path, album_metadata):
    album = sanitize(album_metadata.get('album'))
    artist = sanitize(album_metadata.get('artist'))
    return dest_path / artist / album

def main():
    args = parse_args()

    downloads_dir = Path(args.downloads)
    downloads_pattern = str(downloads_dir / '*.zip')

    verbose = args.verbose
    dry_run = args.dry_run

    zip_filenames = glob(downloads_pattern)
    for filename in zip_filenames:
        with ZipFile(filename, 'r') as zip_file:
            album_metadata = find_album_metadata(zip_file)
            dest_path = create_album_dest_path(Path(args.dest), album_metadata)

            if verbose:
                print(f'Creating dir {dest_path}.')
            if not dry_run:
                dest_path.mkdir(parents=True, exist_ok=True)

            if verbose:
                print(f'Extracting all files to {dest_path}.')
            if not dry_run:
                zip_file.extractall(dest_path)

if __name__ == '__main__':
    main()
