#-*-coding:utf-8-*-
## http://www.cppblog.com/jinq0123/archive/2007/09/03/UsingLoggingConfig.html
import logging
import logging.config

logging.config.fileConfig(fname="logconf.conf")
logger = logging.getLogger("logconf")

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

logHello = logging.getLogger("hello")
logHello.info("Hello world!")