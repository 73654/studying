import random

import jsonpath
import requests

from test_api.test_litemall_pro.api.base_api import BaseApi
from test_api.test_litemall_pro.utils.log_util import logger


class ProductApi(BaseApi):

    def add(self, product_name: str):

        info = {
            'method': 'POST',
            'url': f'{self.base_url}/admin/goods/create',
            'headers': {'X-Litemall-Admin-Token': self.token},
            'data': {
                "goods": {
                    "goodsSn": f"{random.randint(1000000000, 10000000000)}",
                    "name": product_name
                },
                "specifications": [
                    {
                        "specification": "规格",
                        "value": "标准"
                    }
                ],
                "products": [
                    {
                        "specifications": [
                            "标准"
                        ],
                        "price": 0,
                        "number": 0,
                    }
                ],
                "attributes": [
                    {
                        "attribute": "材质",
                        "value": "纯棉"
                    }
                ]
            }
        }

        # r = requests.post(url, json=data, headers=headers)
        r = self.send(**info)
        logger.info(r.json())

        return r

    def get(self, product_name: str):
        """查询商品"""

        info = {
            'method': 'GET',
            'url': f'{self.base_url}/admin/goods/list',
            'params': {
                'name': product_name
            },
            'headers': {'X-Litemall-Admin-Token': self.token}
        }

        # r = requests.get(url, params=params, headers=headers)
        r = self.send(**info)
        logger.info(r.json())

        return r

    def delete(self, product_id: int):
        info = {
            'method': 'POST',
            'url': f'{self.base_url}/admin/goods/delete',
            'headers': {'X-Litemall-Admin-Token': self.token},
            'json': {
                "id": product_id
            }
        }

        # r = requests.post(url, json=data, headers=headers)
        r = self.send(**info)
        logger.info(r.json())

        return r