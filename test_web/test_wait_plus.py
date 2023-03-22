import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWaitUtil:
    def setup(self):
        # 实例化
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭,回收资源
        self.driver.quit()

    def test_wait_util(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        self.driver.find_element(By.ID,'primary_btn').click()
        self.driver.find_element(By.ID,'primary_btn').click()
        # 显式等待
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[1]/div'))
        ).text
        print(ele)
        assert ele == "该弹框点击两次后才会弹出"

    def test_swich_window(self):
        # 打开网页
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        # 获取首页句柄
        main_handle = self.driver.current_window_handle
        print(f"main_handle is {main_handle}")
        # 定位打开新窗口按钮
        self.driver.find_element(By.ID,"openWindows").click()
        # 切换窗口
        for handle in self.driver.window_handles:
            print(f"handles is {handle}")
            if handle != main_handle:
                self.driver.switch_to.window(handle)
        # 已经切换到新窗口
        # 定位新打开的窗口中的练习按钮
        self.driver.find_element(By.ID, "window_btn").click()
        # 弹出 alert 弹窗
        content = self.driver.switch_to.alert.text
        print(content)
        assert "这只是一条单纯的alert消息" in content
        # 点击弹窗上确定按钮
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        # 切换回主页
        self.driver.switch_to.window(main_handle)
        time.sleep(3)