#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
@version: python 3.7.0
@author: liuxuchao
@contact: liuxuchao1129@foxmail.com
@software: PyCharm
@file: huawa.py
@time: 2020-07-20 17:21
"""

import scrapy
import copy
import json
from ..items import Huawa1Item
import re

class KsshopSpider(scrapy.Spider):
    name = 'huawa1'
    base_url = 'https://www.huawa.com/api2.0/store/index?provinceid=0&cityid=0&areaid=0&x_axis=115.49481017&y_axis=38.88656455&pagesize=10&curpage=%s&order=&desc=&keyword='

    def start_requests(self):

        print('*****正在爬取第300页用户信息*****')
        yield scrapy.Request(url=self.base_url % '300',method ="GET",callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        page = re.search('curpage=(.*?)&',response.url).group(1)
        if data['status'] == 1:
            data_list = data['data']['store_list']
            for data in data_list:
                item = Huawa1Item()
                try:
                    item['store_id'] = data['store_id']
                except:
                    item['store_id'] = ""
                else:
                    item['store_id'] = data['store_id']
                try:
                    item['store_grade'] = data['store_grade']
                except:
                    item['store_grade'] = ""
                else:
                    item['store_grade'] = data['store_grade']
                try:
                    item['store_name'] = data['store_name']
                except:
                    item['store_name'] = ""
                else:
                    item['store_name'] = data['store_name']
                try:
                    item['member_id'] = data['member_id']
                except:
                    item['member_id'] = ""
                else:
                    item['member_id'] = data['member_id']
                try:
                    item['member_name'] = data['member_name']
                except:
                    item['member_name'] = ""
                else:
                    item['member_name'] = data['member_name']
                try:
                    item['order_count'] = data['order_count']
                except:
                    item['order_count'] =""
                else:
                    item['order_count'] = data['order_count']
                try:
                    item['score'] = data['score']
                except:
                    item['score'] = ""
                else:
                    item['score'] = data['score']
                try:
                    item['phone'] = '、'.join(data['phoneArr'])
                except:
                    item['phone'] = ""
                else:
                    item['phone'] = '、'.join(data['phoneArr'])
                try:
                    item['store_qq'] = data['store_qq']
                except:
                    item['store_qq'] =""
                else:
                    item['store_qq'] = data['store_qq']
                try:
                    item['store_email'] = data['store_email']
                except:
                    item['store_email'] = ""
                else:
                    item['store_email'] = data['store_email']
                try:
                    item['store_email'] = data['store_email']
                except:
                    item['store_email'] = ""
                else:
                    item['store_email'] = data['store_email']
                try:
                    item['store_address'] = data['store_address']
                except:
                    item['store_address'] = ""
                else:
                    item['store_address'] = data['store_address']
                try:
                    item['area_info'] = data['area_info']
                except:
                    item['area_info'] = ""
                else:
                    item['area_info'] = data['area_info']
                item['page'] = page
                yield item

            if int(page) <767:
                print('*****正在爬取第'+str(int(page)+1)+'页的商家数据*****')
                yield scrapy.Request(url=self.base_url % str(int(page)+1),method ="GET",callback=self.parse)

        else:
            print(data['msg'])
