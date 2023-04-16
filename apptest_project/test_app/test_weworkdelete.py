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
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(
        "name",
        ["王","常雪","李琴","林建"]
    )
    def test_delete(self,name):
        # 点击通讯录
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='通讯录']")
        el1.click()
        # 滑动并找到人数
        el8 = swipe_element(self.driver,AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/itf']//*[@class='android.widget.TextView' and contains(@text,'未加入')]")
        num1 = float(el8[1:3])
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
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gp1']")
        # 确认删除
        el7 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/cst']")
        el7.click()
        # 获取删除后文本
        ele = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/dgl']").text
        # 断言搜索成功
        assert ele == "无搜索结果"
        # 返回
        self.driver.back()
        # 再次获取人数
        el9 = swipe_element(self.driver, AppiumBy.XPATH,
                      "//*[@resource-id='com.tencent.wework:id/itf']//*[@class='android.widget.TextView' and contains(@text,'未加入')]")
        num2 = float(el9[1:3])
        # 断言删除成功
        assert num1 - num2 == 1






