# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 20:44
# @Author  : endless
# @FileName: 09-crawler_bs4.py
# @GitHub  ：https://github.com/epover

from bs4 import BeautifulSoup

# 通过bs4解析本地文件,默认读取文件方式为gbk,所以需要指定utf-8编码
soup = BeautifulSoup(open('09-crawler_bs4.html','r',encoding='utf-8'),'lxml')

# 根据标签名查找到第一个符合条件的数据
# print(soup.a)

# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# (1) find
# 返回的是第一个符合条件的数据
# print(soup.find('li'))

# 根据title的值来找到对应的标签
# print(soup.find('a',title='a2'))

# 根据class属性值来找到对应的标签,class语法已经纯在所以需要添加_
# print(soup.find('p',class_='p1'))

# (2)find_all 返回所有匹配的标签list
# print(soup.findAll('li'))

# 查找多个标签
# print(soup.findAll(['a','span']))

# limit的作用是查找的前几个数据
# print(soup.findAll('li',limit=2))

# (3) select
# select查询返回一个list
# print(soup.select('li'))

# 通过类选择器
# 查找class属性为a1的标签
# print(soup.select('.a1'))
# print(soup.select('#l2'))

# 属性选择器
# 查找li标签中id=l2的标签
# print(soup.select('li[id="l2"]'))
# 查找li标签中有id的标签
# print(soup.select('li[id]'))

# 层级选择器
# 后代选择器
# 找到div下面的li
# print(soup.select('div li'))

# 子代选择器:某标签的第一级标签
# print(soup.select('div > ul > span'))

# 找到a标签和li标签的所有对象
# print(soup.select('a,li'))

# 节点信息
# tag_l1 = soup.select('#l1')[0]
# print(tag_l1)
# 获取标签内容
# print(tag_l1.get_text())
# 获取标签对象中，存在标签那么string就获取不到数据，使用get_text()就能获取数据
# print(tag_l1.string)

# 节点属性
tag_obj = soup.select('#p1')[0]
# print(tag_obj.name)
# print(tag_obj.attrs)

print(tag_obj.get('class'))
print(tag_obj.attrs.get('class'))
print(tag_obj['class'])
