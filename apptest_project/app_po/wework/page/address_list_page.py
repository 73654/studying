import allure
from appium.webdriver.common.appiumby import AppiumBy
from apptest_project.app_po.wework.Base.wework_app import BaseDriver



class AddressListPage(BaseDriver):
    # 添加成员按钮
    _ADD_MEMBER_BTN = AppiumBy.XPATH, "//*[@text='添加成员']"
    _SEARCH_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/l6v']"

    # 点击添加成员按钮,进入添加成员页面
    def goto_add_member_page(self):
        with allure.step("点击添加成员按钮"):
            from apptest_project.app_po.wework.page.add_member_page import AddMemberPage
            # 点击添加成员按钮
            self.swipe_find(*self._ADD_MEMBER_BTN)
        with allure.step("跳转至添加成员页面"):
            # 跳转到添加成员页面
            return AddMemberPage(self.driver)
    def goto_search_page(self):
        from apptest_project.app_po.wework.page.search_page import SearchPage
        with allure.step("点击搜索按钮"):
            # 点击搜索按钮
            self.find_and_click(*self._SEARCH_BTN)
        with allure.step("跳转至通搜索页面"):
            #跳转到搜索界面
            return SearchPage(self.driver)

