import logging
import signal
import time

logger = logging.getLogger(__name__)


def sigterm_handler(_signo, _stack_frame):
    print("SIGTEM DETECTED!!!!!")
    logging.warning('Script terminated...uploading log files')
    logging.info("Uploading log files")

signal.signal(signal.SIGTERM, sigterm_handler)


if __name__ == "__main__":
    print("Starting script")
    print("Running script to test job cancellation on platform")
#     time.sleep(300)
