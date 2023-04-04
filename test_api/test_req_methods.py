import requests


def test_get():
    '''
    发送get请求
    :return:
    '''
    url = "https://httpbin.ceshiren.com/get"
    params = {'name': '郗辰政'}

    r = requests.get(url, params=params)
    print(r)


def test_post():
    '''
    发送post请求
    :return:
    '''
    url = "https://httpbin.ceshiren.com/post"
    my_data = {'name': '辰政'}

    r = requests.post(url, data=my_data)
    print(r)


def test_put():
    '''
    发送put请求
    :return:
    '''
    url = "https://httpbin.ceshiren.com/put"
    my_data = {'name': '泽林'}

    r = requests.put(url, data=my_data)
    print(r)


def test_delete():
    '''
    发送delete请求
    :return:
    '''
    url = "https://httpbin.ceshiren.com/delete"
    r = requests.delete(url)
    print(r)


def test_request_get():
    method = 'GET'
    url = 'https://httpbin.ceshiren.com/get'
    params = {'name': '永旺'}
    r = requests.request(method=method, url=url, data=params)
    print(r.status_code)


def test_request_post():
    url = 'https://httpbin.ceshiren.com/post'
    params = {'name': '辰政'}
    r = requests.request(method='post', url=url, data=params)
    print(r)


def test_request_put():
    url = 'https://httpbin.ceshiren.com/put'
    params = {'name': '辰政'}
    r = requests.request(method='put', url=url, data=params)
    print(r)


def test_request_delete():
    url = "https://httpbin.ceshiren.com/delete"
    r = requests.request(method='delete', url=url)
    print(r)
