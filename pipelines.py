# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# https://www.programcreek.com/python/example/98520/scrapy.exporters.CsvItemExporter
from scrapy import signals
import csv
from scrapy.exporters import CsvItemExporter
import base64
# class CSVPipeline(object):
class PortsalePipeline(object):
    """Get things export"""
    counter = 0
    file_count = 1

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        if spider.name != '':

            file = open('tri111.csv', 'wb+')
            self.files[spider] = file
            self.export_fields = ['Address1', 'Property_ID', 'Land_Type',
                                  'Sale_Date', 'Sale_Type', 'Instrument', 'Sale_Price']
            self.exporter = CsvItemExporter(file, fields_to_export=self.export_fields)
            self.exporter.start_exporting()
            print(self.counter, '*' * 50, file.name)


    def spider_closed(self, spider):
        if spider.name != '':
            self.exporter.finish_exporting()
            file = self.files.pop(spider)
            file.close()

    def process_item(self, items, spider):
        if spider.name != '':
            Property_ID = items.get('Property_ID', None)
            if Property_ID:
                self.exporter.export_item(items)
        return items
