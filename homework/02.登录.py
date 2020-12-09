import requests



# 验证用户使用正确手机号5位数密码登录，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {"mobilephone": "13201889945", "pwd": "12345"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20108'
# assert r['msg'] == '密码长度必须为6~18'
# print(r)

# 验证用户使用已注册正确手机号19位数密码登录，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {"mobilephone": "13201889945", "pwd": "1234562222121212121"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20108'
# assert r['msg'] == '密码长度必须为6~18'
# print(r)

# 验证用户未注册手机号密码登录，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {"mobilephone": "13201987711", "pwd": "123456"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20111'
# assert r['msg'] == '用户名或密码错误'
# print(r)

# 验证用户不输入密码登录，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {"mobilephone": "13201889945", "pwd": ""}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20103'
# assert r['msg'] == '密码不能为空'
# print(r)

# 验证用户不输入手机号，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {"mobilephone": "", "pwd": "123456"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20103'
# assert r['msg'] == '手机号不能为空'
# print(r)

# 验证用户输入已注册手机号正确密码，登录成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {"mobilephone": "13201889945", "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'
print(r)

