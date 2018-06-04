# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ExamplePipeline(object):

    # 英镑兑换人民币汇率
    exchange_rate = 8.5714

    def process_item(self, item, spider):
        # 提取 item 的 price 字段 （如£53.74）
        # 去掉前面英镑符号£，转换为float类型，乘以汇率
        price = float(item['price'][1:]) * self.exchange_rate

        # 保留2位小数，赋值回item的price字段
        item['price']='￥%2f'%price
        
        return item

