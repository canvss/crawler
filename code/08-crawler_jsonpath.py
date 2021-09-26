# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 21:02
# @Author  : endless
# @FileName: 08-crawler_jsonpath.py
# @GitHub  ：https://github.com/epover

import json,jsonpath

object = json.load(open('08-crawler_jsonpath.json','r',encoding='utf-8'))

# 获取所有书的作者
# author_list = jsonpath.jsonpath(object,'$.store.book[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(object,'$..author')
# print(author_list)

# store下面的所有元素
# tag_list = jsonpath.jsonpath(object,'$.store.*')
# print(tag_list)

# store里面所有东西的price
# price = jsonpath.jsonpath(object,'$.store..price')
# print(price)

# 第三本书
# book = jsonpath.jsonpath(object,'$..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(object,'$..book[(@.length-1)]')
# print(book)

# 前面两本书
# book_list = jsonpath.jsonpath(object,'$..book[:2]')
# book_list = jsonpath.jsonpath(object,'$..book[0,1]')
# print(book_list)

# 过滤出所有包含isbn的书
# book_list = jsonpath.jsonpath(object,'$..book[?(@.isbn)]')
# print(book_list)

# 哪本书价格超过了10快
book_list = jsonpath.jsonpath(object,'$..book[?(@.price>10)]')
print(book_list)