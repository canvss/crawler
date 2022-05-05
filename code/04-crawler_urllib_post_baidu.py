# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/15 22:54
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

'''
    利用cookie反爬机制爬取百度详细翻译
'''
import urllib.request,urllib.parse,ssl,json


def get_post_baidu_translate_details():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    headers = {
        'Cookie':'BIDUPSID=2CA898D6EE068F5219370D8141F12912; PSTM=1619934765; BAIDUID=2CA898D6EE068F5248C8EF5B177799A3:FG=1; __yjs_duid=1_515472adcb4d897fc9cc7261d7484d0a1619969288638; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=dJcHA4NzRaY05LQ35lOGU2NEp-b0pwa2JiSlJHMDZicFluUDUwN29GaUNMT3hnRVFBQUFBJCQAAAAAAAAAAAEAAABvAdDLt6Gw28O709DO5WkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIKfxGCCn8RgdT; BDUSS_BFESS=dJcHA4NzRaY05LQ35lOGU2NEp-b0pwa2JiSlJHMDZicFluUDUwN29GaUNMT3hnRVFBQUFBJCQAAAAAAAAAAAEAAABvAdDLt6Gw28O709DO5WkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIKfxGCCn8RgdT; MCITY=-73%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=7B974D7A5B5D1704DA5A85576BEA07F4:FG=1; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1631536089,1631596506,1631618823,1631683528; H_PS_PSSID=34650_34443_34378_31253_34549_34004_34524_34584_34092_34106_26350_34427_34471; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1631717618; __yjs_st=2_MzgxODM1ODcyNjM4YWZlZGFjNDZmYzcyM2VmOTAyZWE1ODY1NWRkMDMwZGEyNjRmNDA4ZmM0ODE0Njg4YTVmMzdhMTUyMzQ3YzM4YzkxMDM3MTlmNWYzNTJmZWE4YzI2MDQxMzRjMzdmMTU2ZDQwODIzM2MxMzcxMmJhMjcyMjBhYmZlNjkxMmNhNTIwZWRjZTA0MWMzMzNlZDBlMzkxOWEwOGEzNWQ3MmQ0YjQzNjU4N2ZiNzMzYWZkMWI5MjVjNmI3Mjk2NzRiODdmYjcxMDNiNzRlMGM4YWUyNzNlNmY1YzE3ZDFiOTlhYmYxMmMyZWYwNDhiZWM3YjYwNWY5NV83X2RjZTBjMjM1; ab_sr=1.0.1_ZWM1ZjAyNTU3YTBiZmU5OTNjNmVmMWZkOTkzN2U0NzE4M2U0YzBkY2JmZDcyOWU1NzhmYzJlYTc2NjQ4OTg5MWY0YzMzNjMxNGY5NWViNTkzYmIyZjFjZTY2MTkxNWQ1OWNlYTM0YTM4OThhNmMzYjEzZDRhZThmOGYyOTdjZTEwMjYyYmEwZTY0OTZhMWY1NGEwNDBkZmY5ZjRjZGQxNGJkMGRlY2QyYjE1ZTgwOGNkN2RmZGViNTA4ZGFlMjkw',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'crawler',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '115941.337876',
        'token': '5a4b9aed798f787a5ab9cd646f33cc50',
        'domain': 'common'
    }

    new_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,data=new_data,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    content = response.read().decode('utf-8')
    resp_obj =json.loads(content)
    print(resp_obj)


get_post_baidu_translate_details()