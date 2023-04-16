import allure
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.wework.Base.wework_app import BaseDriver



class MoreOptionsPage(BaseDriver):
    # 编辑成员按钮
    _REBISE_MEMBER_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/c5x']"
    def goto_revise_member_page(self):
        from apptest_project.app_po.wework.page.revise_member_page import ReviseMemberPage
        with allure.step("跳转到编辑成员页面"):
            # 编辑成员
            self.find_and_click(*self._REBISE_MEMBER_BTN)
            # 跳转编辑成员页面
            return ReviseMemberPage(self.driver)