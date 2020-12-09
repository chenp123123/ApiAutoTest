'''
注册的脚本
'''

import pytest

from ZongHe.baw import Member
from ZongHe.caw import DataRead
from ZongHe.baw import DbOp


# 测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/register_fail.yaml"))
def fail_data(request):
    return request.param

# 测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


# @pytest.fixture(params=DataRead.read_yaml("data_case/register_repeat.yaml"))
# def pass_data(request):
#     return request.param


# 测试逻辑/测试步骤:注册失败的逻辑
def test_register_fail(url, baserequests, fail_data):
    print(f"测试数据：{fail_data}")
    # 下发注册的请求
    # fixture session级别 conftest.py
    r = Member.register(url, baserequests, fail_data['data'])
    print(r.text)
    # 校验结果
    assert r.json()["msg"] == fail_data["expect"]["msg"]
    assert r.json()["code"] == fail_data["expect"]["code"]
    assert r.json()["status"] == fail_data["expect"]["status"]


# 测试逻辑/测试步骤：注册成功的逻辑
def test_register_pass(url, baserequests, pass_data, db):
    print(f"测试数据: {pass_data}")
    # 获取手机号
    mobile = pass_data['data']['mobilephone']
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    print(r.text)

    # 检查结果：1：检查响应与预期结果一致
    assert r.json()["msg"] == pass_data["expect"]["msg"]
    assert r.json()["code"] == pass_data["expect"]["code"]
    # 检查结果： 2：检查系统中用户注册成功
    # 方式1：查询用户，检查手机号在返回的结果中。
    r = Member.select_user(url, baserequests)
    assert mobile in r.text
    # 方式2：从数据库中查询注册用户。
    r = DbOp.select_user(db, mobile)
    assert len(r) == 1
    # 清理环境：删除注册用户
    DbOp.delete_user(db)
    # 重复注册






