'''
发送post请求
'''

import requests
# 登录的接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13201889945",
    "pwd": "123456",
}
# 用data传表单参数,content-type:application
r = requests.post(url, data=user)
print(r.text)
print("*" * 50)  # 分割线


# 用data传表单参数
url = "http://www.httpbin.org/post"
user = {
    "mobilephone": "13201889945",
    "pwd": "123456",
}
r = requests.post(url, data=user)
print(r.text)
print("*" * 50)  # 分割线

# 用json传参数，content-type：application/json
r = requests.post(url, json=user)
print(r.text)
print("*" * 50)  # 分割线



# 练习：充值接口，给注册用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "13201889945",
    "amount": "10000"
}
r = requests.post(url, data=user)    # 使用data/json传参，看接口实现的是哪个
print(r.text)
assert r.json()['status'] == 1
assert r.json()['data']['regname'] == "Hello"
assert r.json()['data']['mobilephone'] == "13201889945"
assert (r.json()['data']['leaveamount'])


