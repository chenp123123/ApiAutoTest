'''
fixture带参数
'''

import pytest


# 测试数据
# 参数使用params关键字，一个列表，列表有5组数据，前3组是数据字典
@pytest.fixture(params=[{"username": "root", "pwd": "123456"},
                        {"username": "admin", "pwd": "888888"},
                        {"username": "administrator", "pwd": "HelloPaw"},
                        "four",
                        5])
def login_data(request):  # 参数request是固定的
    return request.param  # 使用request.param返回每组数据


# 测试逻辑（测试步骤）
# 登录功能的测试脚本
def test_login(login_data):
    print(f"测试登录功能，测试数据为：{login_data}")


# 注册接口的测试代码，用这种方法来实现

