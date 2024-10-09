"""
largefiles.py - Find and print large files in a specified directory

Usage:
    delete_unneeded.py [-h] [-n FILES_COUNT] path size_limit
    
Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

import os
import sys
import logging
import argparse

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


class LageFilesFinder:
    def __init__(self, path: str, size_limit: int):
        self.path = path
        self.size_limit = size_limit
        self.files = []

    def find_large_files(self) -> None:
        print("Scanning files...")
        for root, _, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size > self.size_limit:
                    self.files.append((file_path, file_size))
        if len(self.files) == 0:
            log.info("Files larger than %s B not found", self.size_limit)
            print(f"Files larger than {self.size_limit} B not found")
            sys.exit()
        else:
            # Sort largest to smallest
            log.info("Found %s files larger than %s B", len(self.files), self.size_limit)
            self.files.sort(key=lambda x: x[1], reverse=True)

    def convert_size_units(self, size_bytes: int) -> str:
        units = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(units) - 1:
            size_bytes /= 1024
            i += 1
        return f"{size_bytes:.2f} {units[i]}"

    def print_files(self, n):
        if n is None:
            log.debug("Printing all the files")
        else:
            log.debug("Printing %s files", n)
        for file in self.files[:n]:
            size = self.convert_size_units(file[1])
            print(f"{size}: {file[0]}")


class CommandLineParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Large files finder")

    def parse_args(self):
        self.parser.add_argument(
            "path", type=str,
            help="Path to search for files"
        )
        self.parser.add_argument(
            "size_limit", type=str,
            help="Size lower limit (in KB, MB, GB, e.g. 100KB, 10MB, 1GB, 1TB)"
        )
        self.parser.add_argument(
            "-n", "--files-count", type=int,
            default=None,
            help="Number of files to print"
        )
        return self.parser.parse_args()


def validate_path(path: str):
    # make sure the path is absolute
    path = os.path.abspath(path)
    if not os.path.exists(path):
        print(f"{path} does not exist")
        sys.exit()


def validate_size_limit(size: str) -> int:
    size = size.strip().lower()
    try:
        if size.endswith("kb"):
            return int(size[:-2]) * 1024
        if size.endswith("mb"):
            return int(size[:-2]) * 1024**2
        if size.endswith("gb"):
            return int(size[:-2]) * 1042**3
        if size.endswith("tb"):
            return int(size[:-2]) * 1042**4
        return int(size)
    except ValueError:
        print("Invalid size limit format. E.g. 100KB, 10MB, 1GB")
        sys.exit()


def main():
    parser = CommandLineParser()
    args = parser.parse_args()
    log.debug("%s", args)
    validate_path(args.path)
    size_limit = validate_size_limit(args.size_limit)
    finder = LageFilesFinder(args.path, size_limit)
    finder.find_large_files()
    finder.print_files(args.files_count)

if __name__ == "__main__":
    main()
