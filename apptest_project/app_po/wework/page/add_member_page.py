import allure
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.wework.Base.wework_app import BaseDriver
from utils.log_until import logger


class AddMemberPage(BaseDriver):
    # 手动输入添加按钮
    _MANUAL_INPUT_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dwd']"
    # toast弹窗
    _TOAST_POP = AppiumBy.XPATH, "//*[@class='android.widget.Toast']"

    # 点击手动添加按钮,进入手动添加页面
    def goto_input_member_page(self):
        from apptest_project.app_po.wework.page.input_member_page import InputMemberPage
        with allure.step("点击手动添加按钮"):
            # 点击手动添加按钮
            self.find_and_click(*self._MANUAL_INPUT_BTN)
        with allure.step("跳转手动添加页面"):
            # 进入手动添加页面
            return InputMemberPage(self.driver)

    # 获取toast内容
    def get_toast_tips(self):
        # 获取toast元素
        with allure.step("获取toast元素"):
            tips = self.get_tips(*self._TOAST_POP)
            logger.info(f"弹窗信息为{tips}")
            return tips
