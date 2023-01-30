import logging
import sys

from autologging import TRACE

logging.basicConfig(level=TRACE, stream=sys.stdout,
                    format="%(asctime)s.%(msecs)04d ┃ %(filename)+20s ┃ %(funcName)-30s ┃ %(levelname)+8s ┃ %(message)s")

log = logging.getLogger(__name__)
log.debug("To je debug %s", '123')
log.info("To je info %s", '123')
log.warning("To je warning %s", '123')
log.error("To je debug %s", '123')
