import jsonpath
import requests

from test_api.test_litemall_pro.utils.log_util import logger


class BaseApi:

    def __init__(self):
        self.base_url = 'http://litemall.hogwarts.ceshiren.com'
        self.token = self.get_token()

    def get_token(self):
        # 组装请求数据
        url = f'{self.base_url}/admin/auth/login'
        data = {
            'username': 'hogwarts',
            'password': 'test12345'
        }

        # 解析响应数据
        r = requests.post(url, json=data)
        r_data = r.json()
        logger.info(r_data)

        # 提取token
        token = jsonpath.jsonpath(r_data, expr='$..token')[0]
        return token

    def send(self, method, url, **kwargs):
        r = requests.request(method=method, url=url, **kwargs)

        return r