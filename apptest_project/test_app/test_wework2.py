# 企业微信 App 端添加成员功能自动化测试
# 添加联系人的结果进行断言
import random

# For W3C actions

from apptest_project.test_app.utils import *
from faker import Faker

class Test:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appium:deviceName"] = "wework"
        caps["appium:appPackage"] = "com.tencent.wework"
        caps["appium:appActivity"] = ".launch.WwMainActivity"
        caps["appium:noReset"] = "true"
        caps["appium:uid"] = "127.0.0.1:7555"
        caps["appium:newCommandTimeout"] = "60"
        caps["appium:dontStopAppOnReset"] = "true"
        caps["appium:platformVision"] = "6.0"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)
        fake = Faker("zh_CN")

    def teardown(self):
        self.driver.back()

    def test_swip(self):
        # 滑动找到并点击添加成员元素
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@text='添加成员']")
        # 点击手动输入添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dwd']").click()
        # 获取随机姓名
        name = member_name()
        # 获取随机手机号
        phone = member_phone()
        # 姓名输入框输入姓名
        # self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/byk']").send_keys(name)
        # 手机输入框输入手机号
        # self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/i4t']").send_keys(phone)
        # 点击保存按钮
        # self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/az1']").click()
        # 姓名输入框输入姓名
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/gpu']/child::*/child::*[3]").send_keys(name)
        # 账号输入框输入手机号
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/goa']/child::*/child::*[3]").send_keys(phone)
        # 定义一个列表
        sex=["男","女"]
        # 随机选择列表的一个元素
        choice = random.choice(sex)
        print(choice)
        # 如果选择为 女 点击性别选择
        if choice =="女":
            # 点击 男 按钮
            self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/gpb']").click()
            # 显式等待性别选择框出现
            wait_elements(self.driver,(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/cjp']/child::*[2]"))
            # 点击 女 按钮
            self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/cjp']/child::*[2]").click()
        # 企业邮箱输入框输入手机号
        self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/il8']/child::*/child::*[2]").send_keys(phone)
        # 手机号输入框输入手机号
        self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.tencent.wework:id/i4t']").send_keys(phone)
        # 滑动找到并点击保存元素
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/az1']")
        # 获取toast元素
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text"))
        # 打印xml格式源码
        print(self.driver.page_source)
        print(f"添加成功,添加成员姓名:{name},手机号:{phone}")
        # 断言结果是否正确
        assert "添加成功" == result
