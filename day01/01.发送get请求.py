# 使用requests发送get请求
# pip install
import requests

# 发送一个get请求，返回一个响应，将相应存到变量r中
r = requests.get("http://www.baidu.com")
print(r.text)

# list 获取用户列表。 register http://192.168.150.54:8089/
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
r = requests.get(url)  # 发送请求
print(r.json())
r = r.json()
assert r['status'] == 1  # 对结果进行检查
assert r['code'] == '10001'
assert r['msg'] == '获取用户列表成功'

# get请求带参数，并拼接到URL后面，？参数名1=参数名1&参数名2=参数名2
# 注册接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register?mobilephone=132019gg678&pwd=123324&reqname=小于"
r = requests.get(url)  # 发送请求
r = r.json()
print(r)
assert r['status'] == 0  # 对结果进行检查
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

# get请求带参数，方法2，使用params参数
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13201889945",
    "pwd": "123456",
    "regname": "Hello"
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r['status'] == 0    # 对结果进行检查
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

# 接口功能：查询手机号码归属地
# 接口地址：https://tcc.taobao.com/cc/json/mobile_tel_segment.htm
# 方法：get
# 参数名：tel
# 参数值：手机号

url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13201987793"
r = requests.get(url, params=user)
print(r.text)
print(type(r))
print(r.status_code)    # 状态码
print(r.reason)          # 状态信息
print(r.cookies)          # cookies
print(r.encoding)          # 编码方式
print(r.headers)             # 响应头


# 发送请求时，带请求头
# 有些网站，对自动化发出去的请求不处理或处理结果不一致
# 通过设置请求头，伪装成浏览器发送请求
# httpbin是一个成熟网站，发送的请求，这个网站请求转为json格式返回

url = "http://www.httpbin.org/get?user=root&pwd=123321"
r = requests.get(url)
print(r.text)
# 使用requests发送的请求，"User-Agent"为"python-requests/2.25.0"
head = {
    "User-Agent":""
}
r = requests.get(url,headers=head)
print(r.text)
