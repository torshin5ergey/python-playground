#! python3



import re
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)
log = logging.getLogger(__name__)

LOGFILE = 'access.log'  # /var/log/nginx/access.log

with open(LOGFILE, 'r', encoding='utf-8') as f:
    logs = f.read().split('\n')

report = {}  # ip: []

for row in logs:
    if row:
        ip = re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', row).group(0)
        response_time = re.search(r'\"([0-9]+\.[0-9]+)\"', row).group(1)
        log.debug("%s %s", ip, response_time)
        if ip not in report:
            report[ip] = []
        report[ip].append(response_time)
log.debug("%s", report)

fastest_ip = min(report, key=lambda k:min(report[k]))
log.info("Fastest: %s - %s", fastest_ip, min(report[fastest_ip]))