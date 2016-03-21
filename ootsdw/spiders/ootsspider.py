# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from urlparse import urljoin
import re

from ootsdw.items import OotsItem

class OotsSpider(Spider):
    name = "ootsspider"
    allowed_domains = [
        "www.giantitp.com",
    ]
    start_urls = (
        #'http://www.giantitp.com',
        'http://www.giantitp.com/comics/oots.html',
    )
    regex_name = re.compile('.*oots(\d{4})\.html.*')
    current_num = None

    def parse(self, response):
        # This method uses the archive page
        for sel in response.xpath("(//p[@class='ComicList']/a[contains(@href,'comics/oots') and not(contains(@href,'comics/oots.rss'))])"):
            url = response.urljoin(sel.xpath('@href').extract_first())
            yield Request(url, callback=self.parse_comics_page)

        # This method parses page by page instead of using the archive list
        #for sel in response.xpath("(//a[@class='SideBar' and contains(@href,'comics/oots') and not(contains(@href,'comics/oots.rss'))])"):
        #    url = response.urljoin(sel.xpath('@href').extract_first())
        #    yield Request(url, callback=self.parse_comics_page)

    def parse_comics_page(self,response):
        for sel in response.xpath("//img[contains(@src,'/comics/images/')]"):
            item = OotsItem()
            name = self.regex_name.match(str(response)).group(1)
            item['name'] = name
            self.current_num = int(name)
            src = sel.xpath('@src').extract_first()
            item['image_urls'] = [ urljoin( response.url , src ) ]
            yield item
        
        previous_num = '{:04d}'.format( self.current_num - 1 )
        sel = response.xpath("//a[contains(@href,'comics/oots{}.html')]".format(previous_num))
        if sel:
            url = response.urljoin(sel.xpath('@href').extract_first())
            yield Request(url, callback=self.parse_comics_page)
