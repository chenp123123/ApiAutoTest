'''
登录接口的测试脚本
'''

import pytest
from ZongHe.baw import DbOp, Member
from ZongHe.caw import DataRead


# 测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"), scope='module')
def setup_data(request):
    return request.param


# 测试数据
@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(scope='module')
def register(setup_data, url, baserequests, db):
    # 注册用户
    mobile = setup_data['casedata']['mobilephone']
    DbOp.delete_user(db, mobile)
    r = Member.register(url, baserequests, setup_data['casedata'])
    assert r.json()["msg"] == setup_data["expect"]["msg"]
    assert r.json()["code"] == setup_data["expect"]["code"]
    yield
    # 删除用户
    DbOp.delete_user(db, mobile)


def test_login(register, login_data, url, baserequests):
    # 下发登录请求
    # 检查结果
    r = Member.register(url, baserequests, login_data['casedata'])
    print(r.text)
    assert r.json()["msg"] == login_data["expect"]["msg"]
    assert r.json()["code"] == login_data["expect"]["code"]



