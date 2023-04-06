import requests


def test_req_proxies():
    url = 'https://httpbin.ceshiren.com/get'
    data = {
        'http': '127.0.0.1:8888',
        'https': '127.0.0.1:8888'
    }
    params = {'test': 'proxies'}
    r = requests.get(url, params=params, proxies=data, verify=False)
    print(r.text)

def test_req_practice():
    url = "https://httpbin.ceshiren.com/post"
    proxies = {
        'http': '127.0.0.1:8888',
        'https': '127.0.0.1:8888'
    }
    json = {
        'test':'proxies'
    }
    response = requests.post(url, json=json, proxies=proxies, verify=False)
    print(response.text)