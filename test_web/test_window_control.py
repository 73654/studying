import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindowControl:

    def setup(self):
        # 实例化
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(3)
    def teardown(self):
        # 关闭,回收资源
        self.driver.quit()
    def test_open_window(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        time.sleep(3)
    def test_refresh_window(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        time.sleep(3)
        # 刷新页面
        self.driver.refresh()
        time.sleep(3)
    def test_back_window(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        time.sleep(2)
        # 点击ActionChains
        self.driver.find_element(By.XPATH,'//*[@id="action_chains"]/span').click()
        time.sleep(2)
        # 返回上一页面
        self.driver.back()
    def test_window(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        time.sleep(2)
        # 最大化窗口
        self.driver.maximize_window()
        time.sleep(2)
        # 最小化窗口
        self.driver.minimize_window()