"""
cfgtool.py - command-line utility for processing JSON configuration file.

Written by Sergey Torshin @torshin5ergey
"""


import json
import argparse
from typing import Dict, Any


def read_config(file_path: str) -> Dict[str, Any]:
    """
    Read the configuration JSON file.
        
    Args:
        file_path (str) -- path to config JSON file.
    Returns:
        config (Dict[str, Any]) -- parsed configuration data.
    """
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def write_config(file_path: str, config: Dict[str, Any]) -> None:
    """
    Write the JSON configuration file.

    Args:
        file_path (str) -- path to configuration JSON file.
        config (Dict[str, Any]) -- configuration data to write.
    """
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)


def update_nested_config(config: Dict[str, Any], param_path: str, value: str) -> None:
    """
    Update the nested configuration parameter.

    Args:
        config (Dict[str, Any]) -- configuration data to update.
        param_path (str) -- path to parameter in format parameter.subparameter.
        value (str) -- updated (new) parameter value.
    """
    keys = param_path.split('.')  # Split path to parameter
    d = config  # Start from root
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


def main():
    # Create command-line arguments parser
    parser = argparse.ArgumentParser(description='Process JSON configuration file')
    # Add arguments
    parser.add_argument('action', type=str, choices=['read', 'write'], help='Action to perform: read or write')
    parser.add_argument('file_path', type=str, help='Path to the JSON configuration file')
    parser.add_argument('--param', type=str, help='Path and value for parameter in format path=value (only for write)')
    # Parsin arguments
    args = parser.parse_args()

    if args.action == 'read':
        config = read_config(args.file_path)
        print("Configuration file content:")
        print(json.dumps(config, indent=4))
    
    elif args.action == 'write':
        config = read_config(args.file_path)
        if args.param:
            param_path, value = args.param.split('=')
            update_nested_config(config, param_path, value)
        write_config(args.file_path, config)
        print("Configuration file has been updated.")


if __name__ == "__main__":
    main()
