#!/usr/bin/env python3

import logging
import logging.handlers
import socket

stderr_logger = logging.getLogger(__name__)
stderr_logger.setLevel(logging.DEBUG)

syslog_logger = logging.getLogger("syslogtest")
syslog_handler = logging.handlers.SysLogHandler(
#    address="/dev/log", facility=logging.handlers.SysLogHandler.LOG_LOCAL1,
    address=("localhost", 6154), facility=logging.handlers.SysLogHandler.LOG_LOCAL1,
    socktype=socket.SOCK_DGRAM
)
syslog_handler.setLevel(logging.DEBUG)
syslog_logger.addHandler(syslog_handler)

import time
start  = time.time()
count = 0

while True:
    count += 1
    syslog_logger.error(f'message {count}')
    
    if time.time() - start > 1.0:
        stderr_logger.error(f'{count} messages per seconds')
        start = time.time()
        count = 0
