# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/16 19:31
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''使用ajax发起post请求爬取kfc前10页门店数据'''

import urllib.request,urllib.parse,ssl

def creat_request(pageIndex):
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
    return urllib.request.Request(url=url,data=new_data)

def get_content(request):
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    return response.read().decode('utf-8')

if __name__ == '__main__':
    for page in range(1,11):
        request = creat_request(page)
        content = get_content(request)
        with open('kfc'+str(page)+'.json','w') as f:
            f.write(content)
    print('over!!!')