import random

import pytest

from test_api.test_litemall_goods_classify.api.classify_api import ClassifyApi
from test_api.test_litemall_pro.utils.log_util import logger


class TestLitemall:

    def setup_class(self):
        self.classify_api = ClassifyApi()
        self.id = int(f"{random.randint(1000000, 10000000)}")

    @pytest.mark.run(order=1)
    def test_add(self):
        '''
        测试增加类目
        :return:
        '''
        r = self.classify_api.add("郗辰政")
        logger.info(r.json())
        assert r.status_code == 200

    @pytest.mark.run(order=2)
    def test_get(self):
        '''
        测试获取所有类目
        :return:
        '''
        r = self.classify_api.get()
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0

    @pytest.mark.run(order=4)
    def test_delete(self):
        '''
        测试删除类目
        :return:
        '''
        r = self.classify_api.delete("郗辰政", self.id)
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0

    @pytest.mark.run(order=3)
    def test_update(self):
        '''
        测试修改类目
        :return:
        '''
        r = self.classify_api.update("郗辰政啊", self.id)
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0
