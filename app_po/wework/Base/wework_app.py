# 完成企业微信 app 相关的设置
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker

from app_po.wework.Base.base_page import BasePage


class BaseDriver(BasePage):

    def start(self):
        '''
        启动 app
        :return:
        '''
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
        # 初始化 faker
        self.faker = Faker("zh_CN")

        return self

    def restart(self):
        '''
        重启 app
        :return:
        '''
        # 关闭 app
        self.driver.close()
        # 激活后台运行的 app
        self.driver.activate_app("com.tencent.wework")

    def stop(self):
        '''
        停止 app
        :return:
        '''
        self.driver.quit()

    def goto_main_page(self):
        from app_po.wework.page.main_page import MainPage
        '''
        进入 app 首页
        :return:
        '''
        ...
        return MainPage(self.driver)

    def back_main(self):
        '''
        返回首页界面
        :return:
        '''
        while True:
            eles = self.finds(AppiumBy.XPATH, "//*[@text='通讯录']")
            if len(eles) == 0:
                self.driver.back()
            else:
                break
        # 返回消息页面
        self.find_and_click(AppiumBy.XPATH, value="//*[@text='消息']")

    def back(self):
        '''
        返回
        :return:
        '''
        self.driver.back()
