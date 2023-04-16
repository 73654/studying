import requests


def test_req_form():
    url = 'https://httpbin.ceshiren.com/post'
    data = {
        'name': 'hogwarts',
        'password': 'hogwartsisbest'
    }
    headers = {'Content-Type': 'application/json'}
    # 发起请求
    r = requests.post(url, data=data)
    r1 = requests.post(url, data=json.dumps(data, ensure_ascii=False), headers=headers)
    print(r.json())
    print(r1.json())
    target = r.json()['form']['password']
    # 断言
    assert r.status_code == 200
    assert 'hogwartsisbest' in target
