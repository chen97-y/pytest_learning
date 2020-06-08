# -*- coding:utf-8 -*-
import logging


def test_logging():
    logger = logging.getLogger(__name__)
    logger.info("this is an information")
    logger.debug("this is bug level")
    logger.warn("this is an warning")
    logger.error("this is an error")
    logger.critical("this is an critical")