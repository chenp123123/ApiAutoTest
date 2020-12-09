'''
设置代理
1.如果想抓包分析自动化发出去的报文，可设置代理抓包
2.用一台电脑频繁访问一个网站，被网站认为是攻击，将ip地址禁用.设置代理，换一个ip访问
'''

import requests
proxy = {
    "http": "http://127.0.0.1:8888",   # http协议，使用xxx代理
    "https": "http://127.0.0.1:8888",   # https协议，使用xxx代理
}

# proxy = {
#     "http": None,
#     "https": None
# }

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r = requests.get(url, proxies=proxy)
print(r.json())


url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login?mobilephone=13201889945&pwd=123456"
r = requests.get(url)
print(r.json())
