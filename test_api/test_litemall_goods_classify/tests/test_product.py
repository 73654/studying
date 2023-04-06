import random

import jsonpath
import requests

from test_api.test_litemall_goods_classify.api.classify_api import ClassifyApi
from test_api.test_litemall_pro.utils.log_util import logger


class TestLitemall:

    def setup_class(self):
        self.classify_api = ClassifyApi()

    def test_add(self):
        """测试上架商品"""
        r = self.classify_api.add("郗辰政")
        logger.info(r.json())

        assert r.status_code == 200

    def test_get(self):
        r = self.classify_api.get()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0

    def test_delete(self):
        r = self.classify_api.delete("郗辰政",1044885)
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0

    def test_update(self):
        r = self.classify_api.update(new_name="郗辰政啊", id=1044883)
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0