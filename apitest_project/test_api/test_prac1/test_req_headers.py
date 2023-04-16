import requests


def test_get_with_headers():
    url = 'https://httpbin.ceshiren.com/post'
    info = {'Content-Type': 'application/json', 'Name': 'chatgpt'}
    data = {'name': '辰政'}
    r = requests.post(url, data=data, headers=info)
    print(r.status_code, r.content.decode('utf-8'))
