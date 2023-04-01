import allure
from appium.webdriver.common.appiumby import AppiumBy

from app_po.wework.Base.wework_app import BaseDriver



class MessagePage(BaseDriver):
    # 更多按钮
    _MORE_OPTIONS_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/l6l']"
    # 姓名元素
    _NAME_TEXT = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/khc']"
    def goto_more_options_page(self):
        from app_po.wework.page.more_options_page import MoreOptionsPage
        with allure.step("点击更多选项"):
            # 点击更多选项
            self.find_and_click(*self._MORE_OPTIONS_BTN)
        with allure.step("跳转至更多选项页面"):
            # 跳转到更多选项界面
            return MoreOptionsPage(self.driver)
    def get_newname(self):
        with allure.step("返回修改后的新姓名"):
            # 获取修改后的新姓名
            return self.find_and_text(*self._NAME_TEXT)