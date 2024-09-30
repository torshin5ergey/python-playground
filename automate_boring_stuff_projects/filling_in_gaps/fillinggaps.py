"""
fillinggaps.py Ffind and fill gaps in a sequence of files with a given prefix

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import os
import sys
import re
import argparse
import logging
from typing import List, Tuple

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class GapsFiller:
    def __init__(self, prefix:str, path: str) -> None:
        self.path = path
        self.prefix = prefix

    def parse_prefix_files(self) -> List[str]:
        files_list = []
        for root, _, files in os.walk(self.path):
            for file in files:
                match = re.search(rf"^{self.prefix}\d+", file)
                # log.debug("%s %s", file, match)
                if match:
                    file_name = os.path.join(root, file)
                    files_list.append(file_name)
        files_list.sort()
        log.info("Files found: %s", files_list)
        return files_list

    def find_gaps(self, files_list) -> List[Tuple[int]]:
        """
        Returns:
            [(gap, how_many_files_gapped)]
        """
        gaps = []
        prev = None
        gap_start = None
        gap_count = 0
        for file in files_list:
            match = re.search(rf"{self.prefix}(\d+)", file).groups()[0]
            num = int(match)
            # if the current file num is not consecutive with the previous one
            if prev is not None and num != prev + 1:
                if gap_start is None:
                    gap_start = prev + 1
                    gap_count = 1
                else:
                    gap_count += 1
            else:
                if gap_start is not None:
                    gaps.append((gap_start, gap_count))
                    gap_start = None
                    gap_count = 0
            prev = num
            if gap_start is not None:
                gaps.append((gap_start, gap_count))
        gaps = list(set(gaps))
        log.info("Gaps found: %s", gaps)
        return gaps

    def rename_files(self, files_list):
        next_num = 1
        renamed_count = 0
        for file in files_list:
            match = re.search(rf"(.+){self.prefix}(\d+)(\..+)$", file).groups()
            wd_path = match[0]
            num = int(match[1])
            if num == 0:
                next_num = 0
                continue
            ext = match[2]
            if num != next_num:
                new_file_name = os.path.join(
                    wd_path, f"{self.prefix}{next_num:03d}{ext}"
                )
                log.debug("%s", new_file_name)
                try:
                    os.rename(file, new_file_name)
                    log.info("%s renamed to %s", file, new_file_name)
                    renamed_count += 1
                except FileExistsError:
                    pass
                next_num += 1
        log.info("%s files renamed", renamed_count)

class CommandLineParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Large files finder")

    def parse_args(self):
        self.parser.add_argument(
            "prefix", type=str,
            help=""
        )
        self.parser.add_argument(
            "path", type=str,
            help="Path to search for files with the prefix"
        )
        return self.parser.parse_args()


def validate_path(path: str):
    # make sure the path is absolute
    path = os.path.abspath(path)
    if not os.path.exists(path):
        print(f"{path} does not exist")
        sys.exit()
    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        sys.exit()


def main():
    parser = CommandLineParser()
    args = parser.parse_args()
    log.debug("%s", args)
    validate_path(args.path)
    gaps_filler = GapsFiller(args.prefix, args.path)
    files = gaps_filler.parse_prefix_files()
    log.debug("%s", files)
    if not files:
        print(f"No files with '{args.prefix}' prefix found")
        sys.exit()
    print(f"Found {len(files)} '{args.prefix}' files")
    gaps = gaps_filler.find_gaps(files)
    log.debug("%s", gaps)
    if not gaps:
        print("No gaps found")
        sys.exit()
    gaps_filler.rename_files(files)
    print(f"{len(gaps)} gaps filled in")

if __name__ == "__main__":
    main()
