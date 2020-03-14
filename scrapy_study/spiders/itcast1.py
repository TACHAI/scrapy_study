# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        for i in range(20):
            logger.warning("itcat")
        pass
