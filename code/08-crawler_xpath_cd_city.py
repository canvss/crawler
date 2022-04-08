# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/8 19:23
import time
import urllib.request, json, jsonpath,random,ssl


def create_request(url='http://www.sczwfw.gov.cn/jiq/interface/jitem/find-by-code?code=510000000000&deptType=1&jsonpCallback=jsonpcallback&_=1649418013832'):
    header = {
        'Host': 'www.sczwfw.gov.cn',
        'Referer': 'http://www.sczwfw.gov.cn/?areaCode=510000000000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }


    return urllib.request.Request(url=url, headers=header)


def get_content(request):
    proxies_pool = [
        {'http': '27.29.147.103:40035'},
        {'http': '223.214.31.57:63493'},
        {'http': '49.88.45.26:46981'},
        {'http': '27.157.192.172:28814'},
        {'http': '182.54.37.46:35074'},
        {'http': '183.151.228.251:64710'},
        {'http': '223.242.23.36:46782'},
        {'http': '223.215.174.42:25626'},
        {'http': '223.243.70.76:24203'},
        {'http': '114.239.29.185:38383'},
        {'http': '113.78.27.143:60434'},
        {'http': '117.81.227.197:64074'},
        {'http': '117.69.243.126:58173'},
        {'http': '27.204.95.89:29549'},
        {'http': '115.48.185.217:44342'},
        {'http': '27.29.140.253:40018'},
    ]

    handler = urllib.request.ProxyHandler(proxies=random.choice(proxies_pool))
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    return response.read().decode('utf-8')


def get_county_request(code):
    county_list = []
    for i in city_code:
        request = create_request(
            'http://www.sczwfw.gov.cn/jiq/interface/jitem/find-by-code?code=' + i + '&deptType=1&jsonpCallback=jsonpcallback&_=1649418013832')
        content = get_content(request).split('(')[1].split(')')[0]
        countys = json.loads(content)
        county = jsonpath.jsonpath(countys, '$..data.group.sonAreas..areaLevelCode')
        county_list.append(county)
    return county_list

if __name__ == '__main__':
    request = create_request()
    content = get_content(request)
    new_content = content.split('(')[1].split(')')[0]
    city_list = json.loads(new_content)
    city_code = jsonpath.jsonpath(city_list, '$..data.group.sonAreas..areaLevelCode')
    city_name = jsonpath.jsonpath(city_list, '$..data.group.sonAreas..name')
    county_list = get_county_request(city_code)
    data = get_county_request(county_list)
    for j in range(len(data)):
        for i in data[j]:
            request = create_request(
                'http://www.sczwfw.gov.cn/jiq/interface/jitem/find-by-code?code=' + i + '&deptType=1&jsonpCallback=jsonpcallback&_=1649418013832')
            content = get_content(request).split('(')[1].split(')')[0]
            county = json.loads(content)
            name = str(jsonpath.jsonpath(county, '$..data.group.sonAreas..name'))
            county_name = str(jsonpath.jsonpath(county, '$..data.group.name'))
            code = str(jsonpath.jsonpath(county, '$..data.group.sonAreas..areaLevelCode'))
            with open('city/'+ county_name + '.txt', 'w', encoding='utf-8') as f:
                f.write(code+'\n')
                f.write(name)
                f.close()
