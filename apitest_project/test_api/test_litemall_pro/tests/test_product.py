from apitest_project.test_api.test_litemall_pro.api.product_api import ProductApi
from apitest_project.test_api.test_litemall_pro.utils.log_util import logger


class TestLitemall:

    def setup_class(self):
        self.product_api = ProductApi()

    def test_add(self):
        """测试上架商品"""
        r = self.product_api.add()
        logger.info(r.json())

        assert r.status_code == 200

    def test_get(self):
        r = self.product_api.get(product_name='face2face0406-2')
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0

    def test_delete(self):
        r = self.product_api.delete(product_id=1433813)

        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['errno'] == 0