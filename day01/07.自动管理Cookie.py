'''
自动管理Cookie
'''

import requests

s = requests.session()

# 登录百格
print("===============登录前的Cookies", s.cookies)
url = "https://www.bagevent.com/user/login"
user = {
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url, data=user)
# print(r.text)
print("===============登录后的Cookies", s.cookies)


# 获取账户信息
url = "https://www.bagevent.com/account/dashboard"
r = s.get(url)
# print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

# 退出登录
url = "https://www.bagevent.com/user/login_out"
r = s.get(url)
# print(r.text)
print("===============退出登录后的Cookies", s.cookies)
