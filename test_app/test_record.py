# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Test:
    def setup(self):
        self.caps = {}
        self.caps["platformName"] = "android"
        self.caps["appium:deviceName"] = " xueqiu"
        self.caps["appium:appPackage"] = "com.xueqiu.android"
        self.caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        self.caps["appium:noReset"] = "true"
        self.caps["appium:ensureWebviewsHavePages"] = True
        self.caps["appium:nativeWebScreenshot"] = True
        self.caps["appium:newCommandTimeout"] = 3600
        self.caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        # el3 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/name")
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="// *[@text='BABA']")
        el3.click()
        name_ele = self.driver.find_element(by=AppiumBy.ID, value='com.xueqiu.android:id/topic_text').text
        assert "阿里巴巴" in name_ele
