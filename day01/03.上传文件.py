

import requests


url = "http://www.httpbin.org/post"
# 将本地文件上传到服务器
# 上传文本文件
file = "c:/test.txt"
with open(file, mode='r') as f:
    load = {
         "file1": (file, f, "text/plain")
    }
    r = requests.post(url, files=load)
    print(r.text)

# 上传图片
file2 = "c:/test.jpg"
with open(file2, mode='rb') as f:
    load = {
        "file2": (file2, f, "image/jpg")
    }
    r = requests.post(url, files=load)
    print(r.text)

# 可以一次上传多个文件，文本与图片一起上传
with open(file, mode='r') as f1:
    with open(file2, mode='rb') as f2:
        load = {
            "file1": (file, f1),
            "file2": (file2, f2, "image/jpg")
        }
        r = requests.post(url, files=load)
        print(r.text)