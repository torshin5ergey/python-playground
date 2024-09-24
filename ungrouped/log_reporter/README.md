# Log Reporter

Nginx logs analyser.

## Description

Log Reporter analyzes Nginx logs and provides information about the fastest and slowest response times, the most frequent IP address.

## Algorithm

The script uses regular expressions to parse the log file and extract the IP addresses and response times. It then uses Python's built-in data structures to store and analyze the data.

## How to run

1. Clone this repository
```code
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```code
cd python-playground/ungrouped/log_reporter
```
3. Run Python file with desired arguments (e.g.)
```
python logreporter.py -f access.log all
```

## Usage

The command, if run with `-h` or `--help`, will show the available options:

```
logreporter.py [-h] [-f LOGFILE] {response-fastest,response-slowest,most-frequent-ip,all}

positional arguments:
  {response-fastest,response-slowest,most-frequent-ip,all}     
                        Report type (choose from available)

optional arguments:
  -h, --help            show this help message and exit        
  -f LOGFILE, --logfile LOGFILE
                        Log file path (default is
                        /var/log/nginx/access.log)
```

### Examples

-  Analyze the log file `/var/log/nginx/access.log` and display all information (fastest and slowest response times, most frequent IP addresses)
    ```code
    python logreporter.py all
    ```
- Analyze the log file `access.log` and display only the fastest response time
    ```code
    python logreporter.py -f access.log response-fastest
    ```

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)
