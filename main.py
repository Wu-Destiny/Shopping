import logging  
import logging.config
import urlsearch
import driver
import shop
import threading

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
logger = logging.getLogger('main')

def crawltm():
    for i in range(0,100):
        root_logger.info(i)
        urlsearch.tm_urls("口红",i)
        urlsearch.tm_urls("香水",i)
        urlsearch.tm_urls("彩妆",i)