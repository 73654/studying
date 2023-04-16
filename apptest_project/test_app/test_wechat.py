# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Test:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appium:deviceName"] = "wework"
        caps["appium:appPackage"] = "com.tencent.wework"
        caps["appium:appActivity"] = ".launch.WwMainActivity"
        caps["appium:noReset"] = "true"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_search(self):
        # 点击工作台
        el1 = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.tencent.wework:id/kjd']//*[@text='工作台']")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.tencent.wework:id/l6q']")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/jf8")
        el3.send_keys("打卡")
        el4 = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.tencent.wework:id/itf']//*[@text='打卡']")
        el4.click()
        name_ele = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.tencent.wework:id/a91']").text
        assert "打卡" in name_ele


