from appium.webdriver.common.appiumby import AppiumBy
from app_po.xueqiu.base.xueqiu_app import BaseDriver




class MainPage(BaseDriver):
    # 搜索框按钮
    _SEARCH_BTN = AppiumBy.ID,"com.xueqiu.android:id/tv_search"
    # 行情按钮
    _MARKET_BTN= AppiumBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情'] "
    def goto_search_page(self):
        from app_po.xueqiu.pages.search_page import SearchPage
        # click搜索框按钮
        # el1 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_search")
        # el1.click()
        self.find_and_click(*self._SEARCH_BTN)
        # 跳转到搜索页
        return SearchPage(self.driver)
    def goto_market_page(self):
        from app_po.xueqiu.pages.market_page import MarketPage
        # 点击行情
        # self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情'] ").click()
        self.find_and_click(*self._MARKET_BTN)
        # 跳转到行情页面
        return MarketPage(self.driver)