from appium.webdriver.common.appiumby import AppiumBy

from app_po.xueqiu.base.xueqiu_app import BaseDriver



class SearchPage(BaseDriver):
    # 搜索框
    _SEARCH_FRAME = AppiumBy.ID, "com.xueqiu.android:id/search_input_text"
    # 搜索结果
    _SEARCH_RUSULT = by=AppiumBy.XPATH, f"// *[@resource-id='com.xueqiu.android:id/name']"
    def input_content(self,content):
        from app_po.xueqiu.pages.result_page import ResultPage
        # 输入搜索内容
        # el2 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/search_input_text")
        # el2.send_keys(content)
        self.find_and_sendkeys(*self._SEARCH_FRAME,content)
        # 点击第一个搜索到的元素
        # el3 = self.driver.find_element(by=AppiumBy.XPATH, value=f"// *[@resource-id='com.xueqiu.android:id/name']")
        # el3.click()
        self.find_and_click(*self._SEARCH_RUSULT)
        # 跳转到搜索结果页
        return ResultPage(self.driver)