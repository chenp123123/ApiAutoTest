'''
fixture 测试前置与后置
1.命名灵活，不限于setup,teardown等命名方式
2.使用灵活
3.不需要import即可实现共享
'''

import pytest

# 测试前置
@pytest.fixture()
def login():
    print("登录系统")  # yield之前是前置
    yield
    print("退出系统")  # yield之后是后置

# 测试脚本
def test_query():
    print("查询功能，不需登录")

# 使用方式1：将fixture作为参数传到脚本中    (这个常用一些)
def test_add(login):
    print("添加功能，需登录")

# 使用方式2,：使用注解usefixtures
@pytest.mark.usefixtures("login")
def test_delete(login):
    print("删除功能，需登录")
