# 数据解析

**解析数据，其用途就是在爬虫过程中将服务器返回的HTML源代码转换为我们能读懂的格式。**

- xpath
- jsonpath
- bs4

## xpath

- xpath插件安装（ctrl+shift+x）
- 安装lxml库（pip install lxml）
- 懒加载

### xpath使用

 ```python
from lxml import etree

# etree.parse()读取本地HTMl
tree = etree.parse('07-xpath_test.html')

# 获取body/ul/li标签的内容
list_li = tree.xpath('body/ul/li/text()')

# 获取body/ul/li标签id为l1的内容
list_li = tree.xpath('//ul/li[@id="l1"]/text()')

# 获取body/ul/li标签有id属性的内容
list_li = tree.xpath('//ul/li[@id]/text()')

# 获取body/ul/li标签有class属性的内容
list_li = tree.xpath('//ul/li[@class]/text()')

# 获取body/ul/li标签有id和有class属性的内容
list_li = tree.xpath('//ul/li[@id and @class]/text()')

# 获取body/ul/li标签的id以l开头的内容
list_li = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 获取body/ul/li标签的id包含l的内容
list_li = tree.xpath('//ul/li[contains(@class,"c")]/text()')

# 获取body/ul/li标签id为l1的class属性值
attribute = tree.xpath('//ul/li[@id="l1"]/@class')
 ```

### 抓取站长素材前10页图片

```python
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
```

## JsonPath

- pip install jsonpath

### JsonPath使用

 ```python
import json,jsonpath

object = json.load(open('08-crawler_jsonpath.json','r',encoding='utf-8'))

# 获取所有书的作者
author_list = jsonpath.jsonpath(object,'$.store.book[*].author')
print(author_list)

# 所有的作者
author_list = jsonpath.jsonpath(object,'$..author')
print(author_list)

# store下面的所有元素
tag_list = jsonpath.jsonpath(object,'$.store.*')
print(tag_list)

# store里面所有东西的price
price = jsonpath.jsonpath(object,'$.store..price')
print(price)

# 第三本书
book = jsonpath.jsonpath(object,'$..book[2]')
print(book)

# 最后一本书
book = jsonpath.jsonpath(object,'$..book[(@.length-1)]')
print(book)

# 前面两本书
book_list = jsonpath.jsonpath(object,'$..book[:2]')
book_list = jsonpath.jsonpath(object,'$..book[0,1]')
print(book_list)

# 过滤出所有包含isbn的书
book_list = jsonpath.jsonpath(object,'$..book[?(@.isbn)]')
print(book_list)

# 哪本书价格超过了10快
book_list = jsonpath.jsonpath(object,'$..book[?(@.price>10)]')
print(book_list)
 ```

### 淘票票城市数据

```python
import urllib.request,json,jsonpath

def create_request():
    url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1632662735620_134&jsoncallback=jsonp135&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
    headers = {
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=foyqGW1EDTICAWXMQt+mnIzQ; t=d8799591d39e8a91536ef1af53e94680; lgc=%5Cu738B%5Cu5FD7%5Cu5F3A18228660970; tracknic738B%5Cu5FD7%5Cu5F3A18228660970; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=xaQAAf1k3RE0T6wwZbGLyV2Gnja1k0Qb1sUIKvldK8cqhNB0yJdteQDn5wniaVkO%2BkLgHMdFymW9XvMw4QJgvQ%3D%3D; uc3=nk2=rpB9i5t4xCwUCLbHex6iP5Y%UGrdCbqdCCNpQ%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCujC5mqqlWnWtiF8%3D; uc4=nk4=0%40rMpFul3%2BHjvKbCkx325MJ6j9eKMThOpH7W4geA%3D%3D&id4=0%40U2OcRLKI%2FEgm9OyPQArEW1A%2BZQRT; _cc_=WqG3DMC9EA%3D%3D; xlly_s=1; cookie2=1bf16dc72f369feffb4b59fd887; v=0; _tb_token_=56d8f63eb53e9; mt=ci=-1_0; tb_city=513200; tb_cityName="sKKw0w=="; uc1=cookie14=Uoe3dYeFqc%2FGog%3D%3D; tfstk=c11dBvG4Slq31D8Ou9egPdCe0dfRZGhH4z-SwPINyFcKVMlRiS5cM1ltUUmp6PC..; l=eBrCbbwugrzv13B8BO5CFurza779mQAb4sPzaNbMiInca69h1F11FNCLH0F2RdtjgtCAaetrd8LeqRLHR3AgCc0c07kqm0RxexvO.; isg=BFVVhJkpmMQ3ebzFQpH_cJvAZFEPUglks08wbNf4EkwbLnUgn6LDNDLg-DKYLiEc',
        'referer': 'https://dianying.taobao.com/',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    return urllib.request.Request(url=url,headers=headers)

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')
```

## BeautifulSoup（bs4）

- pip install bs4

### bs4使用

 ```python
from bs4 import BeautifulSoup

# 通过bs4解析本地文件,默认读取文件方式为gbk,所以需要指定utf-8编码
soup = BeautifulSoup(open('09-crawler_bs4.html','r',encoding='utf-8'),'lxml')

# 根据标签名查找到第一个符合条件的数据
print(soup.a)

# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# (1) find
# 返回的是第一个符合条件的数据
print(soup.find('li'))

# 根据title的值来找到对应的标签
print(soup.find('a',title='a2'))

# 根据class属性值来找到对应的标签,class语法已经纯在所以需要添加_
print(soup.find('p',class_='p1'))

# (2)find_all 返回所有匹配的标签list
print(soup.findAll('li'))

# 查找多个标签
print(soup.findAll(['a','span']))

# limit的作用是查找的前几个数据
print(soup.findAll('li',limit=2))

# (3) select
# select查询返回一个list
print(soup.select('li'))

# 通过类选择器
# 查找class属性为a1的标签
print(soup.select('.a1'))
print(soup.select('#l2'))

# 属性选择器
# 查找li标签中id=l2的标签
print(soup.select('li[id="l2"]'))

# 查找li标签中有id的标签
print(soup.select('li[id]'))

# 层级选择器
# 后代选择器
# 找到div下面的li
print(soup.select('div li'))

# 子代选择器:某标签的第一级标签
print(soup.select('div > ul > span'))

# 找到a标签和li标签的所有对象
print(soup.select('a,li'))

# 节点信息
tag_l1 = soup.select('#l1')[0]
print(tag_l1)

# 获取标签内容
print(tag_l1.get_text())

# 获取标签对象中，存在标签那么string就获取不到数据，使用get_text()就能获取数据
print(tag_l1.string)

# 节点属性
tag_obj = soup.select('#p1')[0]
print(tag_obj.name)
print(tag_obj.attrs)soup = BeautifulSoup(response.read().decode(),'lxml')
 ```

### 爬去星巴克菜单图片数据

```python
import urllib.request,json
from bs4 import BeautifulSoup

def down_load(menu_name_list,picture_url_list):
    for i in range(len(menu_name_list)):
        file_name = './starbucks_menu_picture/'+menu_name_list[i].get_text()+'.jpg'
        picture_url = 'https://www.starbucks.com.cn'+menu_picture_list[i].get('style').split('"')[1].split('"')[0]
        try:
            urllib.request.urlretrieve(picture_url,file_name)
        except FileNotFoundError:
            name = menu_name_list[i].get_text().replace('/',' ')
            file_name = './starbucks_menu_picture/'+name+'.jpg'
            urllib.request.urlretrieve(picture_url, file_name)

if __name__ == '__main__':
    url = 'https://www.starbucks.com.cn/menu/'
    response = urllib.request.urlopen(url=url)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    menu_name_list = soup.select('ul[class="grid padded-3 product"] strong')
    menu_picture_list = soup.select('div[class="preview circle"]')
    down_load(menu_name_list,menu_picture_list)
```

