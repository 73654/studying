import json

import requests


def test_req_files():
    url = 'https://httpbin.ceshiren.com/post'
    my_files = {
        'qiqiang': open('./demo.txt', 'rb')
    }
    r = requests.post(url, files=my_files)
    print(r.status_code)
    print(r.json())


def test_req_practice():
    url = 'https://httpbin.ceshiren.com/post'
    files = {
        'hogwarts': open('./demo.txt', 'rb')
    }
    # 发起请求
    r = requests.post(url, files=files)
    print(r.json())
    r_data = r.json()
    target = r_data['files']['hogwarts']
    print(json.dumps(r_data, ensure_ascii=False))
    # 断言
    assert r.status_code == 200
    assert '霍格沃兹测试开发' in target

