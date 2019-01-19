#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import logging_config
from logging_config import RotatingFileNameHandler

# set logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LEVEL = "ERROR"
LOGGING = logging_config.LOGGING
LOGGING["root"]["level"] = LOGGING["handlers"]["default"]["level"] = LEVEL
logging.config.dictConfig(logging_config.LOGGING)

# create logger
logger = logging.getLogger()
logger.addHandler(RotatingFileNameHandler(__file__, "./log"))

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

try:
    print( "AAAAA" + 1+90 )
except Exception, e:
    logger.error(e)