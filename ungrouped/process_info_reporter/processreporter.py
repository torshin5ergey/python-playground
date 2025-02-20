#! python3

# processreporter.py - Collects
#
# Written by Sergey Torshin @torshin5ergey

import os
import json


def get_process_directory(pid:int) -> str:
    proc_dir = f"/proc/{pid}"
    return proc_dir

def count_descriptors(proc_path:str) -> int:
    total_descriptors = len(os.listdir(f"{proc_path}/fd"))
    print()
    return total_descriptors

def get_process_memory(proc_path:str) -> str:
    with open(f"{proc_path}/status", "r") as status:
        for line in status:
            if line.startswith("VmSize:"):
                vmsize = int(line.split()[1])
                break
    return convert_to_humanreadable(vmsize)

def convert_to_humanreadable(kb:int) -> str:
    if kb < 1024:
        return f"{kb} kB"
    elif kb < 1024**2:
        return f"{kb / 1024:.2f} MB"
    elif kb < 1024**3:
        return f"{kb / 1024**2:.2f} GB"
    else:
        return f"{kb / 1024**3:.2f} TB"


def main():
    process = {}
    process["pid"] = os.getpid()
    process["directory"] = get_process_directory(process["pid"])
    process["file_descriptors"] = count_descriptors(process["directory"])
    process["memory"] = get_process_memory(process["directory"])
    print(json.dumps(process, indent=4))

if __name__ == "__main__":
    main()
