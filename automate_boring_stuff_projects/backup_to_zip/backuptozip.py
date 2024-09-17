#! python3
"""
backuptozip.py - Copies an entire folder and its contents into
a ZIP file whose filename increments.

Usage:
    backuptozip.py /path/to/directory

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""


import os
import sys
from datetime import date
import zipfile


def generate_zip_filename(directory:str):
    """Generate a unique ZIP filename."""
    directory = os.path.abspath(directory)  # make sure directory is absolute
    
    suffix = "01"
    while True:
        zip_filename = f"{date.today()}_{os.path.basename(directory)}-{suffix}.zip"
        if not os.path.exists(zip_filename):
            break
        else:
            suffix = str(int(suffix)+1).rjust(2, "0")
    return zip_filename

def create_backup(directory:str, zip_filename:str):
    """Backup the entire contents of 'directory' into a ZIP file."""
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    # Walk the entire directory tree and compress the files
    for dirpath, _, filenames in os.walk(directory):
        print(f"Adding files in {dirpath}...")
        # Add current directody to the ZIP file
        backup_zip.write(dirpath)
        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = f"{os.path.basename(directory)}_"
            if filename.startswith(new_base) and filename.endswith(".zip"):
                continue  # Don't backup other ZIP files
            backup_zip.write(os.path.join(dirpath, filename))
    backup_zip.close()
    print("Done.")


def main():
    """Main."""
    path = sys.argv[1]
    zip_filename = generate_zip_filename(path)
    create_backup(path, zip_filename)

if __name__ == "__main__":
    main()
