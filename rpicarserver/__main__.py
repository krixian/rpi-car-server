import logging
import sys

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.info('Starting rpi-car-server')
    return 1

if __name__ == "__main__":
    sys.exit(main())