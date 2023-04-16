import allure
from appium.webdriver.common.appiumby import AppiumBy
from apptest_project.app_po.wework.Base.wework_app import BaseDriver


class MainPage(BaseDriver):
    # 页面元素定义为私有类属性
    # 通讯录按钮
    _CONTACT_BTN = AppiumBy.XPATH, "//*[@text='通讯录']"
    # 工作台按钮
    _STAGING_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/kjd']//*[@text='工作台']"

    # 点击通讯录按钮,跳转到通讯录页面
    def goto_address_list_page(self):
        with allure.step("跳转至通讯录页面"):
            from apptest_project.app_po.wework.page.address_list_page import AddressListPage
            # click 通讯录 按钮
            # self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='通讯录']").click()
            # 用解包的方式,把元组中的定位方式和定位表达式用位置传参的形式传递到方法中
            self.find_and_click(*self._CONTACT_BTN)
            # 跳转到通讯录页面
            return AddressListPage(self.driver)

    def goto_staging_page(self):
        with allure.step("跳转至工作台页面"):
            from apptest_project.app_po.wework.page.staging_page import StagingPage
            # 点击工作台按钮
            self.find_and_click(*self._STAGING_BTN)
            # 跳转到工作台页面
            return StagingPage(self.driver)
