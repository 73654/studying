# 雪球自选排序功能-最新价
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
        caps = {}
        caps["platformName"] = "android"
        caps["appium:deviceName"] = "xueqiu"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        caps["appium:noReset"] = "true"
        caps["appium:uid"] = "127.0.0.1:7555"
        caps["appium:newCommandTimeout"] = "60"
        caps["appium:dontStopAppOnReset"] = "true"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        # el1 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
        # el1.click()
        # el2 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
        # el2.send_keys("阿里巴巴")
        # el3 = self.driver.find_element(by=AppiumBy.XPATH, value="// *[@text='BABA']")
        # el3.click()
        # el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/current_price']")
        # result= float(el4.text)
        # assert 80*1.1>result and 80*0.9<result
        # print(f"股票当前价格为{result}")
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情'] ")
        el1.click()
        el2 = self.driver.find_elements(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/content_recycler']//*[@resource-id='com.xueqiu.android:id/row_recycler']/child::*[1]/child::*")
        prices = [float(e.text) for e in el2]
        result = sorted(prices, reverse=True)
        el3 = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@text='最新价']")
        el3.click()
        prices2 = [float(e.text) for e in el2]
        assert prices2 == result
