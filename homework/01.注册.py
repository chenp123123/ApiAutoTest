import requests

# 注册

# 验证用户使用不合法手机号注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {"mobilephone": "11111111111", "pwd": "123456"}
# r = requests.post(url, data=user)
# r = r.json()
# print(r)
# assert r['status'] == 0  # 对结果进行检查
# assert r['code'] == '20109'
# assert r['msg'] == '手机号码格式不正确'
# print(r)


# # 验证用户使用10位数手机号码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=1320198779&pwd=123324"
# r = requests.get(url)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == '20109'
# assert r['msg'] == '手机号码格式不正确'


# # 验证用户使用12位数手机号码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=132019877934&pwd=123324"
# r = requests.get(url)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == '20109'
# assert r['msg'] == '手机号码格式不正确'


# # 验证用户使用空手机号码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=&pwd=123324"
# r = requests.get(url)
# r = r.json()
# print(r)
# assert r['status'] == 0
# assert r['code'] == '20103'
# assert r['msg'] == '手机号不能为空'


# 验证用户使用5位数密码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {"mobilephone": "13201889922", "pwd": "12345"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20108'
# assert r['msg'] == '密码长度必须为6~18'
# print(r)


# 验证用户使用19位数密码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {"mobilephone": "13201889922", "pwd": "1234522345675432345"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20108'
# assert r['msg'] == '密码长度必须为6~18'
# print(r)


# 验证用户不输入密码注册，注册异常
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {"mobilephone": "13201889922", "pwd": ""}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20103'
# assert r['msg'] == '密码不能为空'
# print(r)


# 验证用户使用已注册手机号码注册，注册失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {"mobilephone": "13201889945", "pwd": "123456"}
# r = requests.post(url, data=user)
# r = r.json()
# assert r['status'] == 0
# assert r['code'] == '20110'
# assert r['msg'] == '手机号码已被注册'
# print(r)

# 验证用户使用未注册手机号码注册，注册成功
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {"mobilephone": "13201889945", "pwd": "123456"}
r = requests.post(url, data=user)
r = r.json()
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '注册成功'
print(r)