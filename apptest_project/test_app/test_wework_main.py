import random
import pytest
from apptest_project.test_app.utils import *


class TestMain:
    def setup_class(self):
        # 定义一个json串
        caps = {}
        # 设置app的平台 android 或者 ios
        caps["platformName"] = "android"
        # 设置设备名称
        caps["appium:deviceName"] = "wework"
        # 设置设备包名
        caps["appium:appPackage"] = "com.tencent.wework"
        # 设置app的启动页
        caps["appium:appActivity"] = ".launch.LaunchSplashActivity"
        # 不清除缓存启动app
        caps["appium:noReset"] = "true"
        # 等待时间不超过60秒
        caps["appium:newCommandTimeout"] = "60"
        # 不重启app
        caps["appium:dontStopAppOnReset"] = "true"
        # 设置手机版本
        caps["appium:platformVision"] = "9.0"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:connectHardwareKeyboard"] = True
        # client 与 server端建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 设置全局隐式等待时间
        self.driver.implicitly_wait(2)
        self.name = "王东"
        self.phone = "15555573654"
        self.new_name = "王西"
        # 点击底部通讯录按钮
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='通讯录']").click()

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        while True:
            eles = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@text='通讯录']")
            if len(eles) == 0:
                self.driver.back()
            else:
                break

    @pytest.mark.run(order=1)
    def test_add(self):
        # 滑动找到并点击添加成员元素
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@text='添加成员']")
        # 点击手动输入添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dwd']").click()
        # 获取右上角text
        ele = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/l6i']").text
        if ele == "快速输入":
            # 姓名输入框输入姓名
            self.driver.find_element(AppiumBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/gpu']/child::*/child::*[3]").send_keys(
                self.name)
            # 账号输入框输入手机号
            self.driver.find_element(AppiumBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/goa']/child::*/child::*[3]").send_keys(
                self.phone)
            # 定义一个列表
            sex = ["男", "女"]
            # 随机选择列表的一个元素
            choice = random.choice(sex)
            print(choice)
            # 如果选择为 女 点击性别选择
            if choice == "女":
                # 点击 男 按钮
                self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gpb']").click()
                # 显式等待性别选择框出现
                wait_elements(self.driver,
                              (AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/cjp']/child::*[2]"))
                # 点击 女 按钮
                self.driver.find_element(AppiumBy.XPATH,
                                         "//*[@resource-id='com.tencent.wework:id/cjp']/child::*[2]").click()
            # 企业邮箱输入框输入手机号
            self.driver.find_element(AppiumBy.XPATH,
                                     "//*[@resource-id='com.tencent.wework:id/il8']/child::*/child::*[2]").send_keys(
                self.phone)
            # 手机号输入框输入手机号
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/i4t']").send_keys(
                self.phone)
        else:
            # 姓名输入框输入姓名
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/byk']").send_keys(
                self.name)
            # 手机输入框输入手机号
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/i4t']").send_keys(
                self.phone)
        # 滑动找到并点击保存元素
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/az1']")
        # 获取toast元素
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(f"添加成功,添加成员姓名:{self.name},手机号:{self.phone}")
        # 断言结果是否正确
        assert "添加成功" == result

    @pytest.mark.run(order=3)
    def test_revise(self):
        # 点击搜索
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6v']").click()
        # 获取搜索框,并输入成员姓名
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/jf8']").send_keys(
            self.name)
        exists = wait_for_text2(self.driver, "联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果:{self.name}")
        # 判断搜索结果是否为1
        eles = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
        if len(eles) > 1:
            pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        # 点击搜索结果
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']").click()
        # 点击更多选项
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6l']").click()
        # 编辑成员
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/c5x']").click()
        # 清除姓名框内容并输入新内容
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[@text='{self.name}']")
        el1.clear()
        el1.send_keys(self.new_name)
        # 点击性别
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gpb']").click()
        # 定义一个列表
        sex = ["男", "女"]
        # 随机选择列表的一个元素
        choice = random.choice(sex)
        # 获取随机性别并点击更改
        self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[@text='{choice}']").click()
        exists = wait_for_click(self.driver, "//*[@text='保存']")
        if not exists:
            pytest.xfail(reason=f"保存不可点击")
        # 点击保存
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6s']").click()
        wait_for_text2(self.driver, self.new_name)
        # 获取新姓名
        el11 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/khc']")
        assert self.new_name == el11.text
        print(f"成功将{self.name}修改为{self.new_name},其性别修改为{choice}")

    @pytest.mark.run(order=2)
    def test_select(self):
        # 点击搜索
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6v']").click()
        # 获取搜索框,并输入成员姓名
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/jf8']").send_keys(
            self.name)
        exists = wait_for_text2(self.driver, "联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果:{self.name}")
        # 判断搜索结果是否为1
        eles = self.driver.find_elements(by=AppiumBy.XPATH,
                                         value="//*[@resource-id='com.tencent.wework:id/gdx']/child::*")
        if len(eles) > 1:
            pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        assert eles[0].text == self.name

    @pytest.mark.run(order=4)
    def test_delete(self):
        # 滑动并找到人数
        el1 = swipe_element(self.driver, AppiumBy.XPATH,
                            "//*[@resource-id='com.tencent.wework:id/itf']//*[@class='android.widget.TextView' and contains(@text,'未加入')]")
        num1 = float(el1[1:3])
        # 点击搜索
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6v']").click()
        # 获取搜索框,并输入成员姓名
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/jf8']").send_keys(
            self.new_name)
        exists = wait_for_text2(self.driver, "联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果:{self.name}")
        # 判断搜索结果是否为1
        eles = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
        if len(eles) > 1:
            pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        # 点击搜索结果
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']").click()
        # 点击更多选项
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6l']").click()
        # 编辑成员
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/c5x']").click()
        swipe_find(self.driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gp1']")
        # 确认删除
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/cst']").click()
        # 获取删除后文本
        ele = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/dgl']").text
        # 断言搜索成功
        assert ele == "无搜索结果"
        # 返回
        self.driver.back()
        # 再次获取人数
        el2 = swipe_element(self.driver, AppiumBy.XPATH,
                            "//*[@resource-id='com.tencent.wework:id/itf']//*[@class='android.widget.TextView' and contains(@text,'未加入')]")
        num2 = float(el2[1:3])
        # 断言删除成功
        assert num1 - num2 == 1
