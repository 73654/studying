from selenium.webdriver.common.by import By
from web_po.ceshiren_line.package.BaseDriver import BaseDriver
from web_po.ceshiren_line.package.Search_package import SearchPackage


class MainPackage(BaseDriver):
    def test_main_search(self):
        # 点击搜索按钮元素
        self.find_and_click(By.ID, 'search-button')
        # self.driver.find_element(By.ID, 'search-button').click()
        # 点击详细搜索
        self.find_and_click(By.CLASS_NAME, "searching")
        # self.driver.find_element(By.CLASS_NAME, "fa.d-icon.d-icon-sliders-h.svg-icon.svg-node").click()
        return SearchPackage(self.driver)