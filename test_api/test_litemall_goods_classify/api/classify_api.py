import random

import jsonpath
import requests

from test_api.test_litemall_pro.api.base_api import BaseApi
from test_api.test_litemall_pro.utils.log_util import logger


class ClassifyApi(BaseApi):

    def add(self, classify_name: str):
        info = {
            'method': 'POST',
            'url': f'{self.base_url}/admin/category/create',
            'headers': {'X-Litemall-Admin-Token': self.token},
            'json': {
                "name": classify_name,
                "keywords": "",
                "level": "L2",
                "pid": 0
            }
        }
        r = self.send(**info)
        logger.info(r.json())

        return r

    def get(self):
        """查询商品"""

        info = {
            'method': 'GET',
            'url': f'{self.base_url}/admin/category/list',
            'headers': {'X-Litemall-Admin-Token': self.token}
        }
        r = self.send(**info)
        logger.info(r.json())
        return r

    def delete(self, classify_name, id: int):
        info = {
            'method': 'POST',
            'url': f'{self.base_url}/admin/category/delete',
            'headers': {'X-Litemall-Admin-Token': self.token},
            'json': {
                "id": id,
                "name":classify_name,
                "keywords": "",
                "level": "L2",
                "pid": 0
            }
        }
        r = self.send(**info)
        logger.info(r.json())
        return r

    def update(self, new_name, id: int):
        info = {
            'method': 'POST',
            'url': f'{self.base_url}/admin/category/update',
            'headers': {'X-Litemall-Admin-Token': self.token},
            'json': {
                "id": id,
                "name": new_name,
                "keywords": "",
                "level": "L2",
                "pid": 0
            }
        }
        r = self.send(**info)
        logger.info(r.json())
        return r
