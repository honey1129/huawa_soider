# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class Huawa1Pipeline(object):
    fp = None

    def open_spider(self, spider):
        self.fp = open('huawa_data2.csv', 'w', encoding='utf_8_sig', newline="" )
        writer = csv.writer(self.fp)
        writer.writerow(["store_id", "store_grade", "store_name", "member_id ", "member_name", "order_count",
                         "score", "phone", "store_qq","store_email","area_info","store_address","page"])

    def process_item(self, item, spider):
        writer = csv.writer(self.fp)
        writer.writerow(
            [item['store_id'], item['store_grade'], item['store_name'], item['member_id'], item['member_name'],
             item['order_count'], item['score'], item["phone"], item["store_qq"],item["store_email"],item["area_info"],item["store_address"],item["page"]])
        return item

    def close_spider(self, spider):
        self.fp.close()