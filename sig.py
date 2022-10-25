import logging
import signal
import time

# logger = logging.getLogger(__name__)


# def sigterm_handler(_signo, _stack_frame):
#     print("SIGTEM DETECTED!!!!!")
#     logging.warning('Script terminated...uploading log files')
#     logging.info("Uploading log files")


# if __name__ == "__main__":
#     signal.signal(signal.SIGTERM, sigterm_handler)
#     print("Starting script")
#     print("Running script to test job cancellation on platform")
#     while True:
#         time.sleep(20)
#         print('infinite loop')

#!/usr/bin/python

from time import sleep
import signal
import sys


def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

print(sys.argv[1])

if sys.argv[1] == "handle_signal":
    signal.signal(signal.SIGTERM, sigterm_handler)

try:
    print("Hello")
    i = 0
    while True:
        i += 1
        print("Iteration #%i" % i)
        sleep(1)
finally:
    print("Goodbye")
