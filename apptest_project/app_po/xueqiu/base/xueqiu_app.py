from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.xueqiu.base.base_page import BasePage


class BaseDriver(BasePage):
    def start(self):
        '''
        启动 app
        :return:
        '''
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

        return self

    def restart(self):
        '''
        重启 app
        :return:
        '''
        # 关闭 app
        self.driver.close()
        # 激活后台运行的 app
        self.driver.activate_app("com.xueqiu.android")

    def stop(self):
        '''
        停止 app
        :return:
        '''
        self.driver.quit()

    def back(self):
        '''
        返回
        :return:
        '''
        self.find_and_click(AppiumBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='雪球']")
        # self.driver.back()

    def goto_main_page(self):
        from apptest_project.app_po.xueqiu.pages.main_page import MainPage
        '''
        进入 app 首页
        :return:
        '''
        ...
        return MainPage(self.driver)
