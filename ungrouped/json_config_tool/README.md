# JSON Configuration Tool

This script is a **command-line utility** for processing JSON configuration file.

## Description

This script is a command-line Python tool that simplifies and automates **JSON configuration files** processing. It provides functionality to read and write configuration files, with option to modify, and update specific parameters within the file.

## Algorithm

1. The script uses the argparse module for parsing command-line arguments, enabling users to specify the action (read or write), the file path of the JSON configuration file, and an optional parameter to modify when writing to the file.
2. Depending on the specified action, the script reads the configuration file using `json.load()` or updates the configuration parameter using a custom `update_nested_config()` function, and then writes the updated configuration to the file using `json.dump()`.

## How to run

1. Clone this repository
```bash
git clone https://github.com/torshin5ergey/python-playground.git
```
2. Go to this project directory
```bash
cd python-playground/ungrouped/json_config_tool
```
3. Run Python file. For example: reading configuration file.
```bash
python cfgtool.py read config.json
```

## Contents

- `cfgtool.py`: command-line utility for processing JSON configuration file.
- `config.json`: Example configuration JSON file.
- `README.md`: This readme file.

### Functions

The main file `cfgtool.py` contains functions:
- `read_config()`: Read the configuration JSON file.
- `write_config()`: Write the JSON configuration file.
- `update_nested_config()`: Update the nested configuration parameter.

## Usage examples

### Read configuration data

```
>>> python cfgtool.py read config.json
Configuration file content:
{
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "debug": "true"
    },
    "database": {
        "type": "postgresql",
        "host": "localhost",
        "port": 5432,
        "username": "db_user",
        "password": "db_password",
        "database_name": "my_database"
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/myapp.log"
    },
    "api": {
        "key": "my_api_key",
        "endpoint": "https://api.example.com/v1/"
    },
    "email": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "username": "email_user",
        "password": "email_password",
        "from_email": "no-reply@example.com",
        "to_email": "admin@example.com"
    },
    "features": {
        "enable_feature_x": true,
        "enable_feature_y": false
    }
}
```

### Update configuration data

```
>>> python cfgtool.py write config.json --param server.port=3000
Configuration file has been updated.
```
Before:
```json
...
"server": {
        "host": "0.0.0.0",
        "port": "8080",
        "debug": "true"
    },
...
```

After:
```json
...
"server": {
        "host": "0.0.0.0",
        "port": "3000",
        "debug": "true"
    },
...
```

### Print help

```
>>> python cfgtool.py -h
usage: cfgtool.py [-h] [--param PARAM]
                  {read,write} file_path       

Process JSON configuration file

positional arguments:
  {read,write}   Action to perform: read or    
                 write
  file_path      Path to the JSON
                 configuration file

optional arguments:
  -h, --help     show this help message and    
                 exit
  --param PARAM  Path and value for parameter  
                 in format path=value (only    
                 for write)
```

## *Notes*

- The script utilizes the `json` module for working with **JSON files**. It uses functions such as `json.load()` to read JSON data from a file and `json.dump()` to write JSON data to a file. Additionally, the `json.dumps()` function is used for pretty-printing JSON content with indentation for improved readability.
-- The script contains optional command-line argument `--param` that allows users to specify the path and value for a parameter to be updated when writing to the configuration file.

## Author

Sergey Torshin [@torshin5ergey](https://github.com/torshin5ergey)