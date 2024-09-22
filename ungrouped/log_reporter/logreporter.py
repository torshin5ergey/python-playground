#! python3

"""
"""

import re
import argparse
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)


def parse_log(logfile):
    """Log file parsing."""
    report = {}  # ip: [time]
    with open(logfile, 'r', encoding='utf-8') as f:
        for row in f:
            if row:
                ip = re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', row)
                ip = ip.group(0)
                response_time = re.search(r'\"([0-9]+\.[0-9]+)\"', row).group(1)
                #log.debug("%s %s", ip, response_time)
                if ip not in report:
                    report[ip] = []
                report[ip].append(float(response_time))
    return report

def get_fastest(report):
    """Returns the IP address with the fastest response time."""
    if not report:
        return None, None
    ip = min(report, key=lambda x:min(report[x]))
    time = min(report[ip])
    return ip, time

def get_slowest(report):
    """Returns the IP address with the slowest response time."""
    if not report:
        return None, None
    ip = max(report, key=lambda x:max(report[x]))
    time = max(report[ip])
    return ip, time

def parse_args():
    """Parse cli arguments."""
    parser = argparse.ArgumentParser(description="Nginx logs analyser")
    parser.add_argument(
        '-f', '--logfile',
        default='/var/log/nginx/access.log',
        help="Log file path"
    )
    parser.add_argument(
        'report_type',
        choices=['response-fastest', 'response-slowest', 'all'],
        help='Report type'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    report = parse_log(args.logfile)
    log.debug("Report\n%s", report)
    if args.report_type == 'all':  # all
        fastest_ip, fastest_response = get_fastest(report)
        slowest_ip, slowest_response = get_slowest(report)
        log.info("Log: %s", args.logfile)
        log.info("Fastest: %s - %s sec", fastest_ip, fastest_response)
        log.info("Slowest: %s - %s sec", slowest_ip, slowest_response)
    elif args.report_type == 'response-fastest':  # fastest response
        fastest_ip, fastest_response = get_fastest(report)
        log.info("Log: %s", args.logfile)
        log.info("Fastest: %s - %s sec", fastest_ip, fastest_response)
    elif args.report_type == 'response-slowest':  # slowest response
        slowest_ip, slowest_response = get_slowest(report)
        log.info("Log: %s", args.logfile)
        log.info("Slowest: %s - %s sec", slowest_ip, slowest_response)

if __name__ == "__main__":
    main()
