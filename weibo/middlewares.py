# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import logging


class CookiesMiddleware():
    def __init__(self, cookies):
        self.logger = logging.getLogger(__name__)
        self.cookies = cookies

    def process_request(self, request, spider):
        self.logger.debug('正在获取Cookies')
        if self.cookies:
            request.cookies = self.cookies
            self.logger.debug('使用Cookies ')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies=crawler.settings.get('COOKIES')
        )
