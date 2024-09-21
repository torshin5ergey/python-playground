#! python3
"""
selectivecopy.py - Selective copy files with specified extensions
from one directory to another.

Usage:
    selectivecopy.py .ext1 .ext2 .ext3 path/from/to path/where/to

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""


import os
import sys
import re
import logging
from typing import List
import shutil

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
    )
log = logging.getLogger(__name__)

def selective_search(extensions:List[str], wherefrom:str, whereto:str):
    """Search for files with specified extensions in the source directory
    and copy them to the destination directory.
    """
    for dirpath, _, filenames in os.walk(wherefrom):
        print(f"Searching for the files in {dirpath}...")
        for filename in filenames:
            ext = re.search(r'\.[a-zA-Z]+$', filename)
            if ext:
                ext = ext.group(0).lower()
                log.debug("%s", ext)
                if ext in extensions:
                    shutil.copy(os.path.join(dirpath, filename), whereto)
                    log.info("Copied %s", filename)
    log.info("Done.")


def main():
    """Main."""
    if len(sys.argv) >= 4:
        extensions = sys.argv[1:-2]
        wherefrom = os.path.abspath(sys.argv[-2])  # make sure directory is absolute
        whereto = os.path.abspath(sys.argv[-1])  # make sure directory is absolute
        log.debug("%s\n%s\n%s", extensions, wherefrom, whereto)
        log.info("Copying %s files\nfrom %s\nto%s", *extensions, wherefrom, whereto)
        selective_search(extensions, wherefrom, whereto)
    else:
        log.error("Not enough arguments provided")

if __name__ == "__main__":
    main()
