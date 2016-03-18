# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from urlparse import urljoin

from ootsdw.items import OotsItem

class OotsSpider(Spider):
    name = "ootsspider"
    allowed_domains = [
        "www.giantitp.com",
    ]
    start_urls = (
        'http://www.giantitp.com',
    )

    def parse(self, response):
        for sel in response.xpath("(//a[@class='SideBar' and contains(@href,'comics/oots') and not(contains(@href,'comics/oots.rss'))])"):
            url = response.urljoin(sel.xpath('@href').extract_first())
            yield Request(url, callback=self.parse_comics_page)

    def parse_comics_page(self,response):
        for sel in response.xpath("//img[contains(@src,'/comics/images/')]"):
            item = OotsItem()
            item['name'] = 'test'
            item['image_urls'] = [ urljoin( response.url , sel.xpath('@src').extract_first() ) ]
            yield item
