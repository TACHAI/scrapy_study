# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 开始的url

    def parse(self, response):
        # 处理start_url地址对应的响应
        # xpath 得到的是一个select对象列表  然后用extract提取数据
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)
        # pass

        # 先分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item["come_from"] = "itcast"
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            yield item