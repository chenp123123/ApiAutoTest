'''
mock:
1.接口测试的测试场景较难模拟，要大量的工作才能做好
2.该接口的测试，依赖其他接口的模块，依赖的接口尚未开发完成
测试条件不充分时，怎么开展接口测试？
使用Mock模拟接口的返回值
'''
from unittest import mock

import requests

'''
支付接口:http://www.zhifu.com/
方法：post
参数：{"订单号"："12345","支付金额":20.56,"支付方式":"支付宝/微信/余额宝/银行卡"}
返回值：{"code":200, "msg":"支付成功"},{"code":201, "msg":"支付失败"}
接口尚未开发完成
'''


class Pay:
    def zhifu(self, data):
        r = requests.post("http://www.zhifu.com/", data=data)
        return r.json()




def test_001():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
    canshu = {"订单号": "12345", "支付金额": 20.56, "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "支付成功"


def test_002():
    pay = Pay()
    # 通过mock模拟接口的返回值
    pay.zhifu = mock.Mock(return_value={"code": 201, "msg": "支付失败"})
    canshu = {"订单号": "12345", "支付金额": -20.56, "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "支付失败"


# 模块名.类名.方法名
@mock.patch("test_001.Pay.zhifu", return_value={"code": 200, "msg": "支付成功"})
def test_003(n):
    pay = Pay()
    n.return_value = {"code": 200, "msg": "支付超时"}
    canshu = {"订单号": "12345", "支付金额": 2000.56, "支付方式": "微信"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "支付超时"


# 取现接口未实现，写一个取现成功的测试用例
def quxian(data):
    r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data)
    print("实际返回值", r.text)
    return r.json()


def test_quxian():
    canshu = {"mobilephone": "18312332166", "amount": 1001}
    quxian = mock.Mock(return_value={'status': 1, 'code': '20001', 'data': None, 'msg': '取现成功'})
    r = quxian(canshu)
    print("mock后的返回值", r)

