# requests

Requests 唯一的一个**非转基因**的 Python HTTP 库，人类可以安全享用。

**警告**：非专业使用其他 HTTP 库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。

- [官方文档](https://docs.python-requests.org/en/latest/)

- [快速上手](https://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

- 安装requests：`pip install requests`

## response属性

- text：获取网站源码
- encoding：指定编码
- url：获取请求url
- content：响应字节类型
- status_code：获取状态码
- headers：获取响应头信息

```python
import requests

url = 'https://www.baidu.com/'

response = requests.get(url=url)
response.encoding = 'utf-8'
print(response.text)
print(response.status_code)
print(response.headers)
```

## get请求

```python
import requests

url = 'https://www.baidu.com/s?'
headers = {
    'Cookie': "IDUPSID=F92B9E4D1E56FFC74D986488556291F4; PSTM=1649496000; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; APPGUIDE_10_0_2=1; BAIDUID=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1; BDUSS_BFESS=VBFRlB2ME1PSGtETFc5ZjhKTDdiUmFFbmE3SGlpTU5Xd2tnNE4wYnlJYXZaSk5pSUFBQUFBJCQAAAAAAAAAAAEAAABvAdDLt6Gw28O709DO5WkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK~Xa2Kv12tic; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651053384,1651143328,1651299236,1651747217; H_PS_PSSID=36309_31253_34812_36167_34584_35979_35801_26350_36303_22159_36061; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651751227; delPer=0; PSINO=2; BA_HECTOR=a00k8k810g018la03s1h77ftl0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YWZmYzAyYmIyNDkyNzJiMjFhN2Y4ZDllYWIwYmQwMjU4OWJlNzg5MjYyNTZmZDI1MDYzZTNlMDMzNjZhNDJhYzY2OTY5MmM0MjJiODFlMTc1MjBkMzlkMTcwZDk4ZGM1ZjlkZDkyMTRmM2RjODIyNjdjYTk5MGIxZjkzOWUyN2FmZjIxMDM4MGMzMDQ0Zjc4Yjg2ZjZjNDgxN2NjZWVhNQ==; BAIDUID_BFESS=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

data = {
    'wd':'张学友'
}

response = requests.get(url=url, params=data, headers=headers)
response.encoding = 'utf-8'
content = response.text
with open('zxy.html', 'w', encoding='utf-8')as f:
    f.write(content)
```

## post请求

```python
import requests,json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'Cookie': "IDUPSID=F92B9E4D1E56FFC74D986488556291F4; PSTM=1649496000; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; APPGUIDE_10_0_2=1; BAIDUID=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1; BDUSS_BFESS=VBFRlB2ME1PSGtETFc5ZjhKTDdiUmFFbmE3SGlpTU5Xd2tnNE4wYnlJYXZaSk5pSUFBQUFBJCQAAAAAAAAAAAEAAABvAdDLt6Gw28O709DO5WkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK~Xa2Kv12tic; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651053384,1651143328,1651299236,1651747217; H_PS_PSSID=36309_31253_34812_36167_34584_35979_35801_26350_36303_22159_36061; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651751227; delPer=0; PSINO=2; BA_HECTOR=a00k8k810g018la03s1h77ftl0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YWZmYzAyYmIyNDkyNzJiMjFhN2Y4ZDllYWIwYmQwMjU4OWJlNzg5MjYyNTZmZDI1MDYzZTNlMDMzNjZhNDJhYzY2OTY5MmM0MjJiODFlMTc1MjBkMzlkMTcwZDk4ZGM1ZjlkZDkyMTRmM2RjODIyNjdjYTk5MGIxZjkzOWUyN2FmZjIxMDM4MGMzMDQ0Zjc4Yjg2ZjZjNDgxN2NjZWVhNQ==; BAIDUID_BFESS=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

data = {
    'kw': 'book',
}

response = requests.post(url=url, data=data, headers=headers)
content = response.text
obj = json.loads(content)
print(obj)
```

## 代理

```python
import requests

url = 'https://www.baidu.com/s?'
headers = {
    'Cookie': "IDUPSID=F92B9E4D1E56FFC74D986488556291F4; PSTM=1649496000; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; APPGUIDE_10_0_2=1; BAIDUID=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1; BDUSS_BFESS=VBFRlB2ME1PSGtETFc5ZjhKTDdiUmFFbmE3SGlpTU5Xd2tnNE4wYnlJYXZaSk5pSUFBQUFBJCQAAAAAAAAAAAEAAABvAdDLt6Gw28O709DO5WkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK~Xa2Kv12tic; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1651053384,1651143328,1651299236,1651747217; H_PS_PSSID=36309_31253_34812_36167_34584_35979_35801_26350_36303_22159_36061; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1651751227; delPer=0; PSINO=2; BA_HECTOR=a00k8k810g018la03s1h77ftl0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YWZmYzAyYmIyNDkyNzJiMjFhN2Y4ZDllYWIwYmQwMjU4OWJlNzg5MjYyNTZmZDI1MDYzZTNlMDMzNjZhNDJhYzY2OTY5MmM0MjJiODFlMTc1MjBkMzlkMTcwZDk4ZGM1ZjlkZDkyMTRmM2RjODIyNjdjYTk5MGIxZjkzOWUyN2FmZjIxMDM4MGMzMDQ0Zjc4Yjg2ZjZjNDgxN2NjZWVhNQ==; BAIDUID_BFESS=F92B9E4D1E56FFC7EA9D48ED13BD1A6F:SL=0:NR=10:FG=1",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

proxy = {
    'http':'27.44.215.155:4513',
}

data = {
    "wd": "ip"
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)
content = response.text
with open("ip.html", 'w', encoding='utf-8')as f:
    f.write(content)
```

