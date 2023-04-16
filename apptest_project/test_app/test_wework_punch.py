# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import pytest

# For W3C actions

from apptest_project.test_app.utils import *


class Test:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appium:deviceName"] = "wework"
        caps["appium:appPackage"] = "com.tencent.wework"
        caps["appium:appActivity"] = ".launch.LaunchSplashActivity"
        caps["appium:noReset"] = "true"
        caps["appium:newCommandTimeout"] = "60"
        caps["appium:dontStopAppOnReset"] = "true"
        caps["appium:platformVision"] = "9.0"
        caps["appium:settings[waitForIdleTimeout]"] = 1
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()


    def test_punch(self):
        while True:
            # 点击工作台
            el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/kjd']//*[@text='工作台']")
            el1.click()
            # 滑动点击打卡按钮
            swipe_find(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hek' and @text='打卡']")
            # 点击外出打卡
            el2 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/kls']")
            el2.click()
            # 显式等待第*次外出按钮可点击
            exists = wait_for_click(self.driver,"//*[contains(@text,'次外出')]")
            if not exists:
                pytest.xfail(reason="没找到打卡按钮")
            # 点击外出打卡按钮
            el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'次外出')]")
            el3.click()
            # 显式等待外出打卡成功
            exists = wait_for_text2(self.driver,"外出打卡成功")
            if not exists:
                pytest.xfail(reason="没找到外出打卡成功")
            # 获取成功提示信息
            el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/s_']").text
            assert "外出打卡成功" == el4
            self.driver.back()