# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from selenium.webdriver.support import expected_conditions as EC
import time,random
from selenium.common.exceptions import TimeoutException
from loggingpy.log import Logger

class PortsaleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def __init__(self, timeout=7, service_args=[]):
        self.logger = Logger(__name__)
        self.timeout = timeout

        options1 = webdriver.ChromeOptions()
        options1.add_argument('headless')
        self.browser = webdriver.Chrome(
            executable_path=r'D:\01study\01 UW study\Hazard mitigation lab\summer research\code\venv\chromedriver.exe',
            options=options1)

        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def __del__(self):
        time.sleep(2)
        self.browser.close()

    def process_request(self, request, spider):
        """
        Use Chrome to get the web content
        :param request: Request
        :param spider: Spider portsale1
        :return: HtmlResponse
        """

        self.logger.debug("chrome starting headless")
        try:

            self.browser.get(request.url)
            assess_xpath = '//*[@id="detail-collapse-assessment-history"]'
            self.wait.until(EC.presence_of_element_located((By.XPATH, assess_xpath)))
            time.sleep(random.random() * 2)
            a = HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                             status=200)
            self.logger.debug('Nice!!!!')
            return a

        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
            self.logger.debug("What just happened?")
            self.logger.debug("check this address: ", request.url)
            self.logger.debug('-(0)-' * 17)
        time.sleep(1)

    @classmethod
    def from_crawler(cls, crawler):
        # return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
        #            service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class PortsaleDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
