#! python3

# systemreporter.py - Collects and reports system information (CPU, disk)
#
# Usage:
#   systemreporter.py
#
# Written by Sergey Torshin @torshin5ergey

import json
import logging
import re
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)


class SystemReporter:
    def __init__(self):
        self.cpu_info = {}
        self.disk_info = {}


    def report(self, param):
        if param == "cpu":
            log.info(json.dumps(self.cpu_info))
            return json.dumps(self.cpu_info, indent=4)
        pass


    def print_cpu_info(self):
        if not self.cpu_info:
            log.error("No CPU information available")
            return
        print("CPU information:")
        for key, value in self.cpu_info.items():
            print(f"{key}\t: {value}")


    def get_cpu_model_name(self):
        # TODO
        pass


    def get_cpu_cores(self):
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo = f.read()

        cpu_cores = len(re.findall(r"processor\s+: \d+", cpuinfo))
        if not cpu_cores:
            log.error("Could not determine the number of CPU cores")
            raise ValueError("CPU cores information not found.")

        self.cpu_info["cores"] = cpu_cores
        log.info(f"CPU cores: {self.cpu_info['cores']}")


    def get_cpu_threads(self):
        with open("/proc/cpuinfo", "r") as f:
            cpuinfo = f.read()

        cpu_threads = re.search(r"cpu cores\s+: (\d+)", cpuinfo).group(1)
        if not cpu_threads:
            log.error("Could not determine the number of CPU threads")
            raise ValueError("CPU threads information not found.")

        self.cpu_info["threads"] = cpu_threads
        log.info(f"CPU threads: {self.cpu_info['threads']}")


def main():
    reporter = SystemReporter()
    reporter.get_cpu_cores()
    reporter.get_cpu_threads()
    reporter.print_cpu_info()
    reporter.report("cpu")

if __name__ == "__main__":
    main()
