import allure
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.wework.Base.wework_app import BaseDriver



class StagingPage(BaseDriver):
    # 打卡按钮
    _GOTO_PUNCH_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hek' and @text='打卡']"
    def goto_punch_page(self):
        from apptest_project.app_po.wework.page.punch_page import PunchPage
        with allure.step("点击打卡按钮,跳转至打卡页面"):
            # 点击打卡按钮
            self.swipe_find(*self._GOTO_PUNCH_BTN)
            # 跳转到打卡页面
            return PunchPage(self.driver)