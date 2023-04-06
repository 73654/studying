import requests


class TestReq:

    def test_timeout1(self):
        url = 'https://httpbin.ceshiren.com/get'
        r = requests.get(url, timeout=2)
        assert r.status_code
    def test_timeout2(self):
        url = 'https://httpbin.ceshiren.com/delay/10'
        r = requests.get(url, timeout=3)
        assert r.status_code
    def test_timeout3(self):
        url = 'https://github.com'
        r = requests.get(url, timeout=2)
        assert r.status_code