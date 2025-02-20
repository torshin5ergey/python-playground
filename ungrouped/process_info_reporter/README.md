# Process Info Reporter

This Python script collects and reports information about a specified process or the current process.

## Description

The `processreporter.py` script retrieves various details about a process, including its directory, file descriptors, memory usage, and executable file. It can be run for a specific process by providing its PID (Process ID) as an argument, or it can report information about the current process if no PID is specified.

## How to Run

1. Clone this repository
```code
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```code
cd python-playground/ungrouped/process_info_reporter
```
3. Run Python file with desired arguments (e.g.)
```
python processreporter.py
```

## Usage

```
processreporter.py [PID]

optional arguments:
  PID: The Process ID of the process you want to report on. If not provided, the script will report on the current process.
```

### Examples

- Report on the current process
    ```bash
    python processreporter.py
    ```
- Report on a specific process with PID 123
    ```bash
    python processreporter.py 123
    ```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
