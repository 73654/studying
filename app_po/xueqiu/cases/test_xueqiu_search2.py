import pytest
import yaml

from app_po.xueqiu.base.xueqiu_app import BaseDriver
from app_po.xueqiu.utils.utils import get_yaml


class TestXueqiuSearch:

    def setup_class(self):
        # 初始化 app
        self.app = BaseDriver()

    def setup(self):
        # 进入首页
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        # 返回首页 app
        self.app.back()

    def teardown_class(self):
        # 停止 app
        self.app.stop()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(
        "content", get_yaml("..\datas\search_content.yaml")["content"]
        # ["阿里巴巴", "京东", "拼多多"]
    )
    def test_xueqiu_search(self, content):
        result = self.main.goto_search_page().input_content(
            content).click_add_optional().click_cancel().goto_market_page().get_market_result()
        # 断言
        assert content in result

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        "content",
        ["阿里巴巴", "京东", "拼多多"]
    )
    def test_xueqiu_toast(self, content):
        result = self.main.goto_search_page().input_content(content).click_add_optional().get_toast_tips()
        assert "添加成功" == result
