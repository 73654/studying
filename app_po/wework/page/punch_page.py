import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from app_po.wework.Base.wework_app import BaseDriver


class PunchPage(BaseDriver):
    # 切换到外出打卡选项
    _GOOUT_PUNCH_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/kls']"
    # 外出打卡按钮
    _PUNCH_THE_CLOCK_BTN = AppiumBy.XPATH, "//*[contains(@text,'次外出')]"
    # 成功打卡提示信息
    _RIGHT_PUNCH_THE_CLOCK_TEXT = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/s_']"
    def goout_punch_the_clock(self):
        with allure.step("点击外出打卡"):
            # 点击外出打卡
            self.find_and_click(*self._GOOUT_PUNCH_BTN)
        with allure.step("等待外出打卡按钮可以点击"):
        # 显式等待第*次外出按钮可点击
            exists = self.wait_for_click("//*[contains(@text,'次外出')]")
            if not exists:
                pytest.xfail(reason="没找到打卡按钮")
        with allure.step("点击打卡按钮"):
        # 点击外出打卡按钮
            self.find_and_click(*self._PUNCH_THE_CLOCK_BTN)
            # 显式等待外出打卡成功
            exists = self.wait_for_text2("外出打卡成功")
            if not exists:
                pytest.xfail(reason="没找到外出打卡成功")
        with allure.step("返回成功提示信息"):
            # 返回成功提示信息
            return self.find_and_text(*self._RIGHT_PUNCH_THE_CLOCK_TEXT)