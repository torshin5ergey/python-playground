"""
"""

import os
import sys
import re
import argparse
import logging
from typing import List

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


class GapsFiller:
    def __init__(self, prefix:str, path: str) -> None:
        self.path = path
        self.prefix = prefix

    def parse_prefix_files(self) -> List[str]:
        files_list = []
        for root, _, files in os.walk(self.path):
            for file in files:
                match = re.search(rf"{self.prefix}\d+\.", file)
                log.debug("%s %s", file, match)
                if match:
                    file_name = os.path.join(root, file)
                    files_list.append(file_name)
        return files_list


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


def main():
    parser = CommandLineParser()
    args = parser.parse_args()
    log.debug("%s", args)
    validate_path(args.path)
    gaps_filler = GapsFiller(args.prefix, args.path)
    files = gaps_filler.parse_prefix_files()
    log.debug("%s", files)

if __name__ == "__main__":
    main()
