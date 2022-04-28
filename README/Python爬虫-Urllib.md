# Urllib

**Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。**

## urllib库使用

```python
import urllib.request

# 1、定义url
url = 'http://www.baidu.com'
# 2、通过代码模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 3、读取数据，一个字节一个字节的读取  read()方法返回的是字节形式的二进制，需要转换成utf-8
content = response.read().decode('utf-8')
```

## 请求对象定制

```python
import urllib.request
import ssl
url = 'https://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request,context=ssl.SSLContext())
content = response.read().decode('utf-8')
```

## 编解码

- #### urllib.parse.quote()

```python
import urllib.request
import urllib.parse
import ssl

url = 'https://www.baidu.com/s?wd='
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
request_parameters ='张学友'
new_url = url+urllib.parse.quote(request_parameters)
request = urllib.request.Request(url=new_url,headers=headers)
response = urllib.request.urlopen(request,context=ssl.SSLContext())
content = response.read().decode('utf-8')
```

- #### urllib.parse.urlencode()

```python
import urllib.parse
import ssl

def get_webpage():
    url = 'https://www.baidu.com/s?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    data = {
        'wd':'张学友',
        'sex':'男',
        'location':'中国香港'
    }
    # 通过urlencode将参数进行unicode转码拼接
    new_url = url + urllib.parse.urlencode(data)
    # 请求对象的定制
    request = urllib.request.Request(url=new_url,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    if response.getcode() == 200:
        content = response.read().decode('utf-8')
        with open('baidu.html','w') as f:
            f.write(content)
    else:
        print('Crawl failed ！')
```

## Ajax

### get请求

```python
import urllib.request,urllib.parse,ssl

def get_ajax_doubantop20():
    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    content = response.read().decode('utf-8')
    with open('doubantop20.json','w',encoding='utf-8') as f:
        f.write(content)
```

### post请求

```python
import urllib.request,urllib.parse,ssl

def create_request(pageIndex):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid':'',
        'pageIndex': pageIndex,
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    new_data = urllib.parse.urlencode(data).encode('utf-8')
    return urllib.request.Request(url=url,data=new_data,headers=headers)

def get_content(request):
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    return response.read().decode('utf-8')

def download(page,content):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as f:
        f.write(content)
```


## URLError HTTPError

- HTTPError类是URLError类的子类
- 导入urllib.error.HTTPError urllib.error.URLError

```python
import urllib.request,ssl,urllib.error

def get_cnsd_article():
    url = 'https://blosdas.csdn.net/sugar_no1/article/details/883179501'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return urllib.request.urlopen(request,context=ssl.SSLContext())

if __name__ == '__main__':
    try:
        response = get_cnsd_article()
        content =response.read().decode('utf-8')
        print(content)
    except urllib.error.HTTPError:
        print('HTTPError!!!')
    except urllib.error.URLError:
        print('please check up url !')
```


## Cookie登录

```python
import urllib.request,ssl

def create_request():
    url = 'https://www.gulixueyuan.com/'
    headers = {
        'Cookie':'UM_distinctid=17937a016be2721-113a6054-13c680-17937a01675fdc; CNZZDATA1264603569=531034137-1620133818-null%7C1631791587; online-uuid=DCDFF27A-C9-82FB28A78807; PHPSESSID=ftss7rtoujh5fevl4ccg8kpf57; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOW5ZVzlyT1RFeE1HUkFaV1IxYzI5b2J5NXVaWFE9OjE2NjMzMzY4MzY6MDIyNjNTzRmZTQ1ZDdkY2MyYWJlZmI3OTE5OGZlZGU5MA%3D%3D',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Referer': 'https://www.gulixueyuan.com/login'
    }
    return urllib.request.Request(url=url,headers=headers)

def get_content(request):
    return urllib.request.urlopen(request,context=ssl.SSLContext()).read().decode('utf-8')

def download(content):
    with open('sgg.html','w') as f:
        f.write(content)
```


## Handler处理器

### 为什么要学习handler？

- urllib.request.urlopen(url) 不能定制请求头
- urllib.request.Request(url,headers,data)
- Handler 可以定制更高级的请求头

### 代理服务器（代理池）

#### 代理的日常功能

- 突破自身ip限制访问
- 访问一些单位或团体内部资源
- 提高访问速度
- 隐藏真实ip

#### 配置代理

- 创建Request对象
- 创建ProxyHandler对象
- handler对象创建opener对象
- opener.open发起请求

```python
import ssl,urllib.request,random

url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Referer':'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip%E6%9F%A5%E8%AF%A2&oq=ip%25E6%259F%25A5%25E8%25AF%25A2&rsv_pq=93fa920200008ca9&rsv_t=e38bd2devLnU2pnYyuiCFdtzwh3I3gTa0RM85dJNYYIowWwE%2BMJwdn%2FecFA&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=5&rsv_sug3=9&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_sug4=721'
}
proxies_pool = [
    {'http':'58.243.29.180:4570'},
    {'http':'27.44.215.155:4513'},
    {'http':'58.243.29.58:4554'},
    {'http':'58.243.29.148:4570'},
]
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=random.choice(proxies_pool))
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('ip_proxypool.html','w',encoding='utf-8') as f:
    f.write(content)
```
