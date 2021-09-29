# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 19:33
# @Author  : endless
# @FileName: 10-crawler_selenium_method.py
# @Email   : endliss@sina.cn

'''
    1.导入selenium包
    2.创建浏览器操作对象
    3.访问网站
'''
from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get("https://www.baidu.com/")

# 通过id定位元素
button = browser.find_element_by_id("su")
print(button)

# 通过name定位元素
name = browser.find_elements_by_name("wd")
print(name)

# 通过xpath语发定位元素
img_xpath =  browser.find_elements_by_xpath("//div[@id='wrapper']//input")
print(img_xpath)

# 通过标签名定位元素
tag_name = browser.find_elements_by_tag_name('input')
print(tag_name)

# 通过css属性定位元素
css_selector = browser.find_elements_by_css_selector('#kw')
print(css_selector)

# 通过超链接文本定位
link_text = browser.find_element_by_link_text('贴吧')
print(link_text)

# 获取元素文本
print(link_text.text)

# 获取元素属性
print(link_text.get_attribute('class'))

# 获取标签名
print(link_text.tag_name)

# 关闭浏览器
browser.quit()