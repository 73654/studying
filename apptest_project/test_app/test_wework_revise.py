# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import random

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
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.back()

    @pytest.mark.parametrize(
        "name,new_name",
        [
            ["王亮","王晨"],
            ["陈颖", "陈晨"],
            ["邓桂花", "邓桂花"]
        ]
    )
    def test_delete(self,name,new_name):
        # 点击通讯录
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='通讯录']")
        el1.click()
        # 点击搜索
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6v']")
        el2.click()
        # 获取搜索框,并输入成员姓名
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/jf8']")
        el3.send_keys(name)
        # exists = wait_for_text(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gdx']")
        exists = wait_for_text2(self.driver,"联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果:{name}")
        # 判断搜索结果是否为1
        eles = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
        if len(eles) > 1:
            pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        # 点击搜索结果
        el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
        el4.click()
        # 点击更多选项
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6l']")
        el5.click()
        # 编辑成员
        el6 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/c5x']")
        el6.click()
        # 清除姓名框内容并输入新内容
        el7 = self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[@text='{name}']")
        el7.clear()
        el7.send_keys(new_name)
        # 点击性别
        el8 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gpb']")
        el8.click()
        # 定义一个列表
        sex = ["男", "女"]
        # 随机选择列表的一个元素
        choice = random.choice(sex)
        # 获取随机性别并点击更改
        el9 = self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[@text='{choice}']")
        el9.click()
        exists = wait_for_click(self.driver, "//*[@text='保存']")
        if not exists:
            pytest.xfail(reason=f"保存不可点击")
        # 点击保存
        el10 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6s']")
        el10.click()
        wait_for_text2(self.driver,new_name)
        # 获取新姓名
        el11 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/khc']")
        assert  new_name == el11.text
        print(f"成功将{name}修改为{new_name},其性别修改为{choice}")
        # 返回
        self.driver.back()




