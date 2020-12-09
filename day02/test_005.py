'''
fixture的作用域
1.默认是函数级别
2.函数级别 < 模块 < 类级别 < session级别
'''

# 模块级别
import pytest


# scope 设置作用域
@pytest.fixture(scope='module')
def login():
    print("登录系统")
    yield
    print("退出系统")


@pytest.fixture(scope='module')
def db():
    print("连接数据库")
    yield
    print("断开数据库连接")


def test_query(db):  # 登录数据库
    print("执行查询功能，不需登录")


def test_add(login, db):  # 第一次使用fixture的地方执行前置
    print("执行添加功能")


def test_delete():
    print("执行删除功能")


def test_modify():  # 模块执行结束，执行后置
    print("执行修改功能")
