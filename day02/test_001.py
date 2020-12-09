'''
pytest是一种测试框架，用来方便的组织测试脚本生成报告
1.测试文件以test_开头或_test结尾
2.测试类似test开头
3.测试函数/方法以test_开头
执行：
1.运行某个文件pytest脚本.py
2.运行某个文件测试用例 py.test_register_001
3.运行生成测试报告： pytest 脚本.py --html=report.html
4.多线程运行：pytest 脚本.py -n 3
5.失败重执行：pytest 脚本.py -reruns 3
'''

import requests
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
def test_register_001():
    data = {"mobilephone": "1320144945", "pwd": "123456"}
    r = requests.post(url, data=data)
    assert r.json()['msg'] == "手机号码格式不正确"

def test_register_002():
    data = {"mobilephone": "13201449945", "pwd": "12345"}
    r = requests.post(url, data=data)
    assert r.json()['msg'] == "密码长度必须为6~18位"

def test_register_003():
    data = {"mobilephone": "13201449945", "pwd": "1234622222222222222"}
    r = requests.post(url, data=data)
    assert r.json()['msg'] == "密码长度必须为6~18位"
