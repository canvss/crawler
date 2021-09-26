# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 21:27
# @Author  : endless
# @FileName: 08-crawler_jsonpath_taopiaopiao_city.py
# @GitHub  ：https://github.com/epover


import urllib.request,json,jsonpath

def create_request():
    url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1632662735620_134&jsoncallback=jsonp135&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

    headers = {
        'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=foyqGW1EDTICAWXMQt+mnIzQ; t=d8799591d39e8a91536ef1af53e94680; lgc=%5Cu738B%5Cu5FD7%5Cu5F3A18228660970; tracknick=%5Cu738B%5Cu5FD7%5Cu5F3A18228660970; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=xaQAAf1k3RE0T6wwZbGLyV2Gnja1k0Qb1sUIKvldK8cqhNB0yJdteQDn5wniaVkO%2BkLgHMdFymW9XvMw4QJgvQ%3D%3D; uc3=nk2=rpB9i5t4xCwUCLbHex6iP5Y%3D&id2=UUGrdCbqdCCNpQ%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCujC5mqqlWnWtiF8%3D; uc4=nk4=0%40rMpFul3%2BHjvKbCkx325MJ6j9eKMThOpH7W4geA%3D%3D&id4=0%40U2OcRLKI%2FEgm9OyPQArEW1A%2BZQRT; _cc_=WqG3DMC9EA%3D%3D; xlly_s=1; cookie2=1bf16ed34adc72f369feffb4b59fd887; v=0; _tb_token_=56d8f63eb53e9; mt=ci=-1_0; tb_city=513200; tb_cityName="sKKw0w=="; uc1=cookie14=Uoe3dYeFqc%2FGog%3D%3D; tfstk=c11dBvG4Slq31D8Ou9egPdCe0dfRZGhH4z-SwPINyFcKVMlRiS5cM1ltUUmp6PC..; l=eBrCbbwugrzv13B8BO5CFurza779mQAb4sPzaNbMiInca69h1F11FNCLH0F2RdtjgtCAaetrd8LeqRLHR3AgCc0c07kqm0RxexvO.; isg=BFVVhJkpmMQ3ebzFQpH_cJvAZFEPUglks08wbNf4EkwbLnUgn6LDNDLg-DKYLiEc',
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

if __name__ == '__main__':
    # request = create_request()
    # content = get_content(request)
    # new_content = content.split('(')[1].split(')')[0]
    # with open('08-crawler_taopiaopiao_city.json','w',encoding='utf-8') as f:
    #     f.write(new_content)

    obj = json.load(open('08-crawler_taopiaopiao_city.json','r',encoding='utf-8'))
    city_list = jsonpath.jsonpath(obj,'$..regionName')
    print(city_list)