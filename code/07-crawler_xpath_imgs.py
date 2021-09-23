# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 21:54
# @Author  : endless
# @FileName: 07-crawler_xpath_imgs.py
# @GitHub  ：https://github.com/epover

'''
    下载站长素材前10页图片
'''

# 第一页：https://sc.chinaz.com/tupian/jinmaoquantupian.html
# 第二页：https://sc.chinaz.com/tupian/jinmaoquantupian_2.html
import urllib.request
from lxml import etree

def create_request(page):
    url = None
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/jinmaoquantupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/jinmaoquantupian_'+str(page)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip%E6%9F%A5%E8%AF%A2&oq=ip%25E6%259F%25A5%25E8%25AF%25A2&rsv_pq=93fa920200008ca9&rsv_t=e38bd2devLnU2pnYyuiCFdtzwh3I3gTa0RM85dJNYYIowWwE%2BMJwdn%2FecFA&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=5&rsv_sug3=9&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_sug4=721'
    }
    return urllib.request.Request(url=url,headers=headers)

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def download(content):
    tree = etree.HTML(content)
    img_url = tree.xpath('//div[@id="container"]//a/img/@src2')
    name = tree.xpath('//div[@id="container"]//a/img/@alt')
    for i in range(len(img_url)):
        url = 'https:'+img_url[i]
        filename = './download_pricture/'+name[i]+'.jpg'
        urllib.request.urlretrieve(filename=filename,url=url)

if __name__ == '__main__':
    for page in range(1,4):
        request = create_request(page)
        content = get_content(request)
        download(content)
        print('over')