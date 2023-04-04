import requests


def test_resp():
    url = 'https://httpbin.ceshiren.com/get'
    r = requests.get(url)
    print(f'r.status_code:{r.status_code}')
    print(f'r.raw:{r.raw}')
    content = r.content.decode("utf-8")
    print(f'r.content:{type(content)}{content}')
    print(f'r.text:{r.text}')
    print(f'r.headers:{r.headers}')
    print(f'r.url:{r.url}')
    print(f'r.json:{r.json()}')
    assert r.url == 'https://httpbin.ceshiren.com/get'
    assert r.status_code == 200
    assert "application/json" == r.headers["Content-Type"]