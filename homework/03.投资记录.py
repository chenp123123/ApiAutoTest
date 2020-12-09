# import requests
#
# # 验证id为空，获取用户所有投资记录失败
# # url = "http://192.168.150.54:8089/futureloan/mvc/api//invest/getInvestsByLoanId"
# # user = {"memberId": ""}
# # r = requests.post(url, data= user)
# # r = r.json()
# # print(r)
# # assert r['status'] == 0
# # assert r['code'] == '30002'
# # assert r['msg'] == '参数错误：标id不能为空'
# # print(r)
#
#
# # 验证id为不为数字，获取用户所有投资记录失败
# # url = "http://192.168.150.54:8089/futureloan/mvc/api//invest/getInvestsByLoanId"
# # user = {"memberId": "abc"}
# # r = requests.post(url, data= user)
# # r = r.json()
# # print(r)
# # assert r['status'] == 0
# # assert r['code'] == '30104'
# # assert r['msg'] == '参数错误：参数必须是数字'
# # print(r)
#
#
# # 验证id为不为数字，获取用户所有投资记录失败
# # url = "http://192.168.150.54:8089/futureloan/mvc/api//invest/getInvestsByLoanId"
# # user = {"memberId": "ab3%c"}
# # r = requests.post(url, data= user)
# # r = r.json()
# # print(r)
# # assert r['status'] == 0
# # assert r['code'] == '30104'
# # assert r['msg'] == '参数错误：参数必须是数字'
# # print(r)
#
# # 验证正确id，获取用户所有投资记录成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api//invest/getInvestsByLoanId"
# user = {"memberId": "1314"}
# r = requests.post(url, data= user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == '10001'
# assert r['msg'] == '成功'
# print(r)