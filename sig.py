import logging
import signal
import time

logger = logging.getLogger(__name__)


def sigterm_handler(_signo, _stack_frame):
    print("SIGTEM DETECTED!!!!!")
    logging.warning('Script terminated...uploading log files')
    logging.info("Uploading log files")


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    print("Starting script")
    for i in range(0, 300000):
        print(i)
    print("Running script to test job cancellation on platform")
