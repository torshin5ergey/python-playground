#! python3

# processreporter.py - Collects
#
# Written by Sergey Torshin @torshin5ergey

import os
import sys
import logging
import json

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)


def get_process_directory(pid:int) -> str:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        log.error(f"Process with PID {pid} does not exist")
        return None
    except PermissionError:
        log.error("No permission to access the process")
        return None
    return f"/proc/{pid}"

def count_descriptors(proc_path:str) -> int:
    try:
        total_descriptors = len(os.listdir(f"{proc_path}/fd"))
        return total_descriptors
    except (PermissionError, FileNotFoundError) as e:
        log.error(f"Failed to count the process file descriptors: {e}")
        return None

def get_process_memory(proc_path:str) -> str:
    try:
        with open(f"{proc_path}/status", "r") as status:
            for line in status:
                if line.startswith("VmSize:"):
                    vmsize = int(line.split()[1])
                    break
        return convert_to_humanreadable(vmsize)
    except (FileNotFoundError, PermissionError) as e:
        log.error(f"Failed to read process status: {e}")
        return None

def convert_to_humanreadable(kb:int) -> str:
    if kb < 1024:
        return f"{kb} kB"
    elif kb < 1024**2:
        return f"{kb / 1024:.2f} MB"
    elif kb < 1024**3:
        return f"{kb / 1024**2:.2f} GB"
    else:
        return f"{kb / 1024**3:.2f} TB"

def get_process_exe_file(proc_path:str) -> str:
    try:
        exe_file = os.readlink(f"{proc_path}/exe")
        return exe_file
    except (PermissionError, FileNotFoundError) as e:
        log.error(f"Failed to get the process exe file: {e}")
        return None

def main():
    process = {}
    if len(sys.argv) == 2:
        try:
            process["pid"] = int(sys.argv[1])
        except ValueError:
            log.error(f"Invalid PID: {sys.argv[1]}. Must be an integer.")
            sys.exit(1)
    elif len(sys.argv) == 1:
        process["pid"] = os.getpid()
    else:
        log.error("Usage: processreporter.py [pid]")
        sys.exit(1)

    process["directory"] = get_process_directory(process["pid"])
    if process["directory"] is None:
        sys.exit(1)

    process["file_descriptors"] = count_descriptors(process["directory"])
    process["memory"] = get_process_memory(process["directory"])
    process["exe_file"] = get_process_exe_file(process["directory"])

    print(json.dumps(process, indent=4))

if __name__ == "__main__":
    main()
