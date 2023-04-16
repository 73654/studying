import pytest

from apptest_project.app_po.xueqiu.base.xueqiu_app import BaseDriver


class TestXueqiuSearch:
    def setup_class(self):
        self.content = "阿里巴巴"

    def setup(self):
        # 初始化 app
        self.app = BaseDriver()
        # 进入首页
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        # 停止 app
        self.app.back()

    @pytest.mark.run(order=2)
    def test_xueqiu_search(self):
        result = self.main.goto_search_page().input_content(
            self.content).click_add_optional().click_cancel().goto_market_page().get_market_result()
        # 断言
        assert self.content in result

    @pytest.mark.run(order=1)
    def test_xueqiu_toast(self):
        result = self.main.goto_search_page().input_content(self.content).click_add_optional().get_toast_tips()
        assert "添加成功" == result
