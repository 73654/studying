# 雪球自选排序功能-最新价
# 雪球搜索股票，并添加自选，断言toast和行情列表
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
        caps["appium:deviceName"] = "xueqiu"
        caps["appium:appPackage"] = "com.xueqiu.android"
        caps["appium:appActivity"] = ".view.WelcomeActivityAlias"
        caps["appium:noReset"] = "true"
        caps["appium:newCommandTimeout"] = "60"
        caps["appium:dontStopAppOnReset"] = "true"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize(
        "concent",
        [["阿里巴巴"],["京东"],["拼多多"]]
    )
    def test_search(self,concent):
        # 点击搜索框
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
        el1.click()
        # 搜索框输入内容
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
        el2.send_keys(concent)
        # 点击第一个搜索到的元素
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value=f"// *[@resource-id='com.xueqiu.android:id/name']")
        el3.click()
        # 获取搜索到的股票价格
        # el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 将获取到的价格转为浮点数
        # result= float(el4.text)
        # 断言价格是否在80的上下10%浮动
        # assert 80*1.1>result and 80*0.9<result
        # print(f"股票当前价格为{result}")
        # 点击行情按钮
        # el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情'] ")
        # el1.click()
        # 获取股票最新价并输出到列表中
        # el2 = self.driver.find_elements(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/content_recycler']//*[@resource-id='com.xueqiu.android:id/row_recycler']/child::*[1]/child::*")
        # prices = [float(e.text) for e in el2]
        # 对列表中元素按从大到小排序
        # result = sorted(prices, reverse=True)
        # 点击最新价按钮
        # el3 = self.driver.find_element(by=AppiumBy.XPATH,value="//*[@text='最新价']")
        # el3.click()
        # 输出到列表中
        # prices2 = [float(e.text) for e in el2]
        # 断言排序结果相同
        # assert prices2 == result
        # 点击加自选按钮
        self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/follow_btn']").click()
        # 获取toast文本元素
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 断言获取结果是否一致
        assert result == "添加成功"
        # 点击取消按钮
        self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/action_close']").click()
        # 点击行情按钮
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情'] ").click()
        # 获取全部股票的名字并输出到列表中
        ele = self.driver.find_elements(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/portfolio_stockName']")
        eles = [e.text for e in ele]
        # 断言输入内容是否等于输出结果
        assert concent == eles
        # 点击股票管理按钮
        self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/edit_group']").click()
        # 点击全选按钮
        self.driver.find_element(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/check_all']").click()
        # 点击取消关注按钮
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/cancel_follow']").click()
        # 点击确定按钮
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tv_right']").click()
        # 点击完成按钮
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/action_close']").click()
        # 点击雪球首页按钮
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='雪球'] ").click()
