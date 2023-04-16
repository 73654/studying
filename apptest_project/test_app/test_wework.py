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
        caps["appium:uid"] = "127.0.0.1:7555"
        caps["appium:dontStopAppOnReset"] = "true"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()

    @pytest.mark.parametrize(
        "text,element,result",
        [
            ["高启强","//*[@resource-id='com.tencent.wework:id/f4l']//*[@text='高启强']","高启强"],
            ["..+","//*[@resource-id='com.tencent.wework:id/dgl']","无搜索结果"],
            ["123456","//*[@resource-id='com.tencent.wework:id/gdx']//*[@class='android.widget.TextView']","123456"],
            ["","//*[@resource-id='com.tencent.wework:id/jf8']",""],
            ["12345", "//*[@resource-id='com.tencent.wework:id/jf8']", ""]
        ]
    )
    def test_search(self,text,element,result):
        el1 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/jud")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/l6v")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.tencent.wework:id/jf8")
        el3.send_keys(text)
        # el4 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/cxq")
        # el4.click()
        # name_ele=self.driver.find_element(by=AppiumBy.ID,value='com.tencent.wework:id/khc').text
        name_ele = self.driver.find_element(by=AppiumBy.XPATH,value=element).text
        assert result in name_ele
        # 给二傻子打电话
        # e15 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/b33")
        # e15.click()
        # e16 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/cjr")
        # e16.click()
        # e17 = self.driver.find_element(by=AppiumBy.ID,value="com.tencent.wework:id/mf6").text
        # assert '高启强' in e17

