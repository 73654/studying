from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.xueqiu.base.xueqiu_app import BaseDriver



class ResultPage(BaseDriver):
    # 加自选按钮
    _ADD_OPTIONAL_BTN = AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/follow_btn']"
    # 取消按钮
    _CANCEL_BTN = AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_close']"
    # toast弹窗
    _TOAST_POP = AppiumBy.XPATH, "//*[@class='android.widget.Toast']"
    # 取消自选按钮
    _CANCEL_OPTIONAL_BTN = AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/followed_btn']"
    def click_add_optional(self):
        # 判断是否在自选列表
        ele = self.finds(*self._ADD_OPTIONAL_BTN)
        if len(ele) == 0:
            self.find_and_click(*self._CANCEL_OPTIONAL_BTN)
        # 点击加自选按钮
        # self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/follow_btn']").click()
        self.find_and_click(*self._ADD_OPTIONAL_BTN)
        return self
    def click_cancel(self):
        from apptest_project.app_po.xueqiu.pages.main_page import MainPage
        # 点击取消
        # self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/action_close']").click()
        self.find_and_click(*self._CANCEL_BTN)
        # 跳转到首页
        return MainPage(self.driver)
    def get_toast_tips(self):
        tips = self.get_tips(*self._TOAST_POP)
        return tips

