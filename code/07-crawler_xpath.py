# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 19:21
# @Author  : endless
# @FileName: 07-crawler_xpath.py
# @GitHub  ：https://github.com/epover

'''
   使用xpath解析本地文件
'''

from lxml import etree

# etree.parse()读取本地HTMl
tree = etree.parse('07-xpath_test.html')

# 获取body/ul/li标签的内容
# list_li = tree.xpath('body/ul/li/text()')

# 获取body/ul/li标签id为l1的内容
# list_li = tree.xpath('//ul/li[@id="l1"]/text()')

# 获取body/ul/li标签有id属性的内容
# list_li = tree.xpath('//ul/li[@id]/text()')

# 获取body/ul/li标签有class属性的内容
# list_li = tree.xpath('//ul/li[@class]/text()')

# 获取body/ul/li标签有id和有class属性的内容
# list_li = tree.xpath('//ul/li[@id and @class]/text()')

# 获取body/ul/li标签的id以l开头的内容
# list_li = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 获取body/ul/li标签的id包含l的内容
list_li = tree.xpath('//ul/li[contains(@class,"c")]/text()')

# 获取body/ul/li标签id为l1的class属性值
attribute = tree.xpath('//ul/li[@id="l1"]/@class')
print(attribute)
