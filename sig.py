import logging
import signal
import time

logger = logging.getLogger(__name__)


def sigterm_handler(_signo, _stack_frame):
    logger.warning('Script terminated...uploading log files')
    logger.info("Uploading log files")

signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    logger.info("Running script to test job cancellation on platform")
    time.sleep(240)

if __name__ == "__main__":
    main()
