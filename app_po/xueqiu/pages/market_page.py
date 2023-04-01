from appium.webdriver.common.appiumby import AppiumBy

from app_po.xueqiu.base.xueqiu_app import BaseDriver


class MarketPage(BaseDriver):
    # 行情结果元素
    _MARKET_RESULT = AppiumBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/portfolio_stockName']"
    def get_market_result(self):
        # 返回行情结果
        # 获取全部股票的名字并输出到列表中
        # ele = self.driver.find_elements(by=AppiumBy.XPATH,value="//*[@resource-id='com.xueqiu.android:id/portfolio_stockName']")
        ele = self.finds(*self._MARKET_RESULT)
        eles = [e.text for e in ele]
        return eles

