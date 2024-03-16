from signal import SIGINT, SIGTERM, SIGABRT, signal
import logging

from config import logger_name
from handler import HTTPStatusWatchdog


def signal_handler(signum, frame):
    logger = logging.getLogger(logger_name)
    instance = HTTPStatusWatchdog.get_instance()

    if signum == SIGINT:
        logger.info('KeyboardInterrupt')
    elif signum == SIGTERM:
        logger.info('Normal termination')
    elif signum == SIGABRT:
        logger.info("Abnormal termination")
    else:
        logger.info(f"Other termination signal: {signum}")

    instance.close_event.set()


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    signal(SIGTERM, signal_handler)
    signal(SIGABRT, signal_handler)

    watchdog = HTTPStatusWatchdog.get_instance()
    watchdog.run()
