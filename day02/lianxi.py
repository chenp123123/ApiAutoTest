


# 注册接口的测试代码，用test_007的方法来实现
import pytest
import requests


@pytest.fixture(params=[
    {"data": {"mobilephone": "13201889945", "pwd": "123456"},
     "expect": {"msg": "手机号码已被注册", "code": '20110'}},
    {"data": {"mobilephone": "13201889945", "pwd": "12346"},
     "expect": {"msg": "密码长度必须为6~18", "code": '20108'}},
    {"data": {"mobilephone": "13201889945", "pwd": "1234561234567876543"},
     "expect": {"msg": "密码长度必须为6~18", "code": '20108'}},
])
def register_data(request):  # 参数request是固定的
    return request.param  # 使用request.param返回每组数据


# 测试逻辑（测试步骤）
# 登录功能的测试脚本
def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print("测试数据", register_data['data'])
    print("预期结果", register_data['expect'])
    r = requests.post(url, data=register_data['data'])
    print(r.json())
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']