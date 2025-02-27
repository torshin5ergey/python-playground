#! python3

"""
systemreporter.py - Collects and reports system information (CPU, disk)

Usage:
    systemreporter.py

Written by Sergey Torshin @torshin5ergey
"""

import json
import logging
import re

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)


class SystemReporter:
    """"""
    def __init__(self):
        self.cpuinfo_path = "/proc/cpuinfo"
        self.cpu_info = {}
        self.disk_info = {}


    def read_cpuinfo(self):
        """"""
        with open(self.cpuinfo_path, "r", encoding="utf-8") as f:
            cpuinfo = f.read()
        return cpuinfo


    def report(self, param):
        """"""
        if param == "cpu":
            log.info(json.dumps(self.cpu_info))
            return json.dumps(self.cpu_info, indent=4)
        log.info("No data to report")
        return None


    def print_cpu_info(self):
        """"""
        if not self.cpu_info:
            log.error("No CPU information available")
            return
        print("CPU information:")
        for key, value in self.cpu_info.items():
            print(f"{key}\t: {value}")


    def get_cpu_model(self):
        """"""
        cpuinfo = self.read_cpuinfo()

        cpu_model = re.search(r"model name\s+: (.+)", cpuinfo)
        if not cpu_model:
            log.error("Could not determine the CPU model")
            raise ValueError("CPU model information not found")

        self.cpu_info["model"] = cpu_model.group(1)
        log.info("CPU model: %s", self.cpu_info['model'])


    def get_cpu_cores(self):
        """"""
        cpuinfo = self.read_cpuinfo()

        cpu_cores = len(re.findall(r"processor\s+: \d+", cpuinfo))
        if not cpu_cores:
            log.error("Could not determine the number of CPU cores")
            raise ValueError("CPU cores information not found")

        self.cpu_info["cores"] = cpu_cores
        log.info("CPU cores: %s", self.cpu_info['cores'])


    def get_cpu_threads(self):
        """"""
        cpuinfo = self.read_cpuinfo()

        cpu_threads = re.search(r"cpu cores\s+: (\d+)", cpuinfo)
        if not cpu_threads:
            log.error("Could not determine the number of CPU threads")
            raise ValueError("CPU threads information not found")

        self.cpu_info["threads"] = int(cpu_threads.group(1))
        log.info("CPU threads: %s", self.cpu_info['threads'])
