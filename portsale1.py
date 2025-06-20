# -*- coding: utf-8 -*-

import dbfpy
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import PortsaleItem
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shutil import which
from scrapy import Request, Spider
import time, random
import re

## get the list of urls we want to append to the base url
line_lst = []
with open('add_id_new.txt', 'r', 1) as f:
    for line in f:
        if not line.startswith('\n'):
            line_lst.append(line)
# print(line_lst[2:15])
web_lst1 = []
for i in line_lst:
    i = i.strip('\n')
    i = i.strip('/')
    i = i.replace(' ', '-')
    i = i.replace('&', '-')
    i = i.replace(';', '/')
    add = '/detail/assessor/' + i + '_did/'
    web_lst1.append(add)
web_lst = web_lst1[:]
# print(web_lst)

class Portsale1Spider(scrapy.Spider):
    name = 'portsale1'
    allowed_domains = ['portlandmaps.com']
    base_url = 'https://www.portlandmaps.com'

    def start_requests(self):
        base_url = 'https://www.portlandmaps.com'
        count = 0
        for url_add in web_lst[1:3]:
            url = base_url + url_add
            time.sleep(random.random() * 3)
            yield Request(url=url, callback=self.parse, dont_filter=False)
            count = count + 1
            self.logger.debug(url)
            self.logger.debug('Here is the count: ')
            self.logger.debug(str(count))

    def parse(self, response):
        items = PortsaleItem()
        time.sleep(random.random() * 3)
        
        Address1_XPATH = '//*[@id="general"]/dl/dd[1]//text()'
        Property_ID_XPATH = '//*[@id="general"]/dl/dd[4]//text()'
        Land_Type_XPATH = '//*[@id="general"]/dl/dd[14]//text()'

        Sale_Date_css = '#sales-history-deed-table td:nth-child(1)::text'
        Sale_Type_css = '#sales-history-deed-table td:nth-child(2)::text'
        Instrument_css = '#sales-history-deed-table td:nth-child(3)::text'
        Sale_Price_css = '#sales-history-deed-table td:nth-child(4)::text'

        items['Address1'] = str(response.xpath(Address1_XPATH).extract())
        items['Property_ID'] = str(response.xpath(Property_ID_XPATH).extract())
        items['Land_Type'] = str(response.xpath(Land_Type_XPATH).extract())

        ##changed style but same items
        items['Sale_Date'] = str(response.css(Sale_Date_css).extract())
        items['Sale_Type'] = str(response.css(Sale_Type_css).extract())
        items['Instrument'] = str(response.css(Instrument_css).extract())
        items['Sale_Price'] = str(response.css(Sale_Price_css).extract())
        self.log("did it go through?")
        yield items
