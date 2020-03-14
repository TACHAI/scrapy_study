# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    # start_urls = ['https://book.suning.com/?safp=d488778a.10038.sTMJP.17']
    start_urls = ['https://list.suning.com/1-502308-0.html']

    def parse(self, response):
        book_list = response.xpath("//div[@id='filter-results']//li")
        next_url = response.xpath("//a[@id='nextPage']").extract_first()
        print("nextPage" + next_url)
        # for li in book_list:
        #     item = {}
        #     item["come_from"] = "book"
        #     item["book_name"] = li.xpath(".//div[@class='res-info']//p[2]//a//text()").extract_first()
        #     yield item
        #
        # # 找到下一页url地址
        #
        # if next_url != "javascript:;":
        #     next_url = "https://list.suning.com" + next_url
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse()
        #     )
        # pass
