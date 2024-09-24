#! python3

"""
logreporter.py - Nginx logs analyser

Usage:
    logreporter.py [-h] [-f LOGFILE] {response-fastest,response-slowest,all}

Written by Sergey Torshin @torshin5ergey
"""

import re
import sys
import json
from typing import Dict, List, Union, Tuple
import argparse
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)


def parse_log(logfile:str) -> Dict[str, Dict[str, Union[List[float], int]]]:
    """Log file parsing."""
    report = {}  # ip: {response_time: [time], rate_count: rate}
    try:
        with open(logfile, 'r', encoding='utf-8') as f:
            for row in f:
                if row:
                    ip_match = re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', row)
                    if ip_match:
                        ip = ip_match.group(0)
                    else:
                        continue
                    response_time = re.search(r'\"([0-9]+\.[0-9]+)\"', row)
                    if response_time:
                        try:
                            response_time = float(response_time.group(1))
                        except ValueError:
                            continue
                    else:
                        continue
                    # log.debug("%s %s", ip, response_time)
                    report.setdefault(ip, {})
                    report[ip].setdefault('response_time', []).append(response_time)
                    report[ip]['rate_count'] = report[ip].get('rate_count', 0) + 1
        return report
    except FileNotFoundError:
        log.info("File %s not found", logfile)
        sys.exit()

def get_fastest(report:Dict) -> Tuple[str, float]:
    """Returns the IP address with the fastest response time."""
    if not report:
        return None, None
    ip = min(report, key=lambda x:min(report[x]['response_time']))
    time = min(report[ip]['response_time'])
    return ip, time

def get_slowest(report:Dict) -> Tuple[str, float]:
    """Returns the IP address with the slowest response time."""
    if not report:
        return None, None
    ip = max(report, key=lambda x:max(report[x]['response_time']))
    time = max(report[ip]['response_time'])
    return ip, time

def get_most_frequent_ip(report:Dict) -> str:
    """"""
    if not report:
        return None
    ip = max(report, key=lambda x:report[x]['rate_count'])
    return ip

def parse_args():
    """Parse cli arguments."""
    parser = argparse.ArgumentParser(description="Nginx logs analyser")
    parser.add_argument(
        '-f', '--logfile', type=str,
        default='/var/log/nginx/access.log',
        help="Log file path (default is /var/log/nginx/access.log)"
    )
    parser.add_argument(
        'report_type', type=str,
        choices=['response-fastest', 'response-slowest',
                 'most-frequent-ip', 'all'],
        help='Report type (choose from available)'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    report = parse_log(args.logfile)
    log.debug("Report\n%s", report)
    
    if args.report_type == 'all':  # all
        fastest_ip, fastest_response = get_fastest(report)
        slowest_ip, slowest_response = get_slowest(report)
        most_frequent_ip = get_most_frequent_ip(report)
        log.info("Log: %s", args.logfile)
        log.info("Fastest: %s - %s sec", fastest_ip, fastest_response)
        log.info("Slowest: %s - %s sec", slowest_ip, slowest_response)
        log.info("Most frequent IP: %s", most_frequent_ip)
    elif args.report_type == 'response-fastest':  # fastest response
        fastest_ip, fastest_response = get_fastest(report)
        log.info("Log: %s", args.logfile)
        log.info("Fastest: %s - %s sec", fastest_ip, fastest_response)
    elif args.report_type == 'response-slowest':  # slowest response
        slowest_ip, slowest_response = get_slowest(report)
        log.info("Log: %s", args.logfile)
        log.info("Slowest: %s - %s sec", slowest_ip, slowest_response)
    elif args.report_type == 'most-frequent-ip':  # most frequent ip
        most_frequent_ip = get_most_frequent_ip(report)
        log.info("Log: %s", args.logfile)
        log.info("Most frequent IP: %s", most_frequent_ip)
    sys.exit()

if __name__ == "__main__":
    main()
