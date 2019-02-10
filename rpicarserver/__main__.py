import logging
import sys

import webserver

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.info('Starting rpi-car-server')

    try:
        webserver.start()
        return 1
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        logger.exception(ex)
        raise

if __name__ == "__main__":
    sys.exit(main())