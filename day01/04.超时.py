'''
超时：
1,上传文件比较大，如2g的文件，默认的时间上传不完，可设置大一点的超时时间
2.接口性能要求，如接口必须在0.5秒内返回，可设置为0.5秒
'''

import requests

# 获取用户列表的接口
for i in range(10):
    try:
        url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
        r = requests.get(url, timeout=0.5)
        print(r.text)
    except Exception as e:
        print(e)