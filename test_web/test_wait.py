import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        # 实例化
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭,回收资源
        self.driver.quit()
    def test_wait_until(self):
        '''
        显式等待
        '''
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 显式等待  WebDriverWait(driver实例, 最长等待时间, 轮询时间).until(结束条件)
        WebDriverWait(self.driver, 10 ,0.5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#located_id"))
        )
        # 定位 消息提示按钮
        self.driver.find_element(By.ID,"success_btn").click()