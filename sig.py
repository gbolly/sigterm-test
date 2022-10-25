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
    print("Running script to test job cancellation on platform")
    while True:
        time.sleep(20)
        print('infinite loop')
