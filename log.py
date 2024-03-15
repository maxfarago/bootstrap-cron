import logging

# create new logger
logger = logging.getLogger(__name__)

# remove propagation to prevent duplicates
# https://docs.python.org/3/library/logging.html#logging.Logger.propagate
logger.propagate = False

# during active development, accept DEBUG level logs
# see: https://sematext.com/blog/logging-levels/
logger.setLevel(logging.DEBUG)

# create handler for console streaming and output
# logs of level DEBUG and up to standard output
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)

# create a log format using Log Record attributes
# https://docs.python.org/3/library/logging.html#logrecord-attributes
log_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# set the log format on each handler
stdout_handler.setFormatter(log_format)

# add each handler to the Logger object
logger.addHandler(stdout_handler)
