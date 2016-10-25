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
    for i in range(0, 100):
        s = "天猫 " + str(i)
        logger.info(s)
        urlsearch.tm_urls("口红", i)
        urlsearch.tm_urls("香水", i)
        urlsearch.tm_urls("彩妆", i)


def crawljd():
    for i in range(0, 100):
        s = "京东 " + str(i)
        logger.info(s)
        urlsearch.jd_urls("口红", i)
        urlsearch.jd_urls("香水", i)
        urlsearch.jd_urls("彩妆", i)


def crawlymx():
    for i in range(0, 100):
        s = "亚马逊 " + str(i)
        logger.info(s)
        urlsearch.ymx_urls("口红", i)
        urlsearch.ymx_urls("香水", i)
        urlsearch.ymx_urls("彩妆", i)


def crawljmyp():
    for i in range(0, 100):
        s = "聚美优品 " + str(i)
        logger.info(s)
        urlsearch.jmyp_urls("口红", i)
        urlsearch.jmyp_urls("香水", i)
        urlsearch.jmyp_urls("彩妆", i)


crawljmyp()
