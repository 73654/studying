import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAction:
    def setup(self):
        # 实例化 driver
        self.driver = webdriver.Chrome()
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭 driver
        self.driver.quit()
    def test_baidu(self):
        # 打开百度首页
        self.driver.get("https://www.baidu.com/")
        # 定位输入框,输入内容
        # 链式调用
        # self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹")
        # 先找元素,然后再通过元素进行操作
        ele = self.driver.find_element(By.ID,"kw")
        ele.send_keys("hogwarts")
        time.sleep(2)
        # 清空输入框
        ele.clear()
        time.sleep(2)
        # 再次输入内容
        ele.send_keys("霍格沃兹")
        # 点击百度一下按钮
        self.driver.find_element(By.ID,"su").click()
        time.sleep(2)
        # 获取元素的值,传入元素属性的key
        name = ele.get_attribute("name")
        class_name = ele.get_attribute("class")
        print(f"name属性值为{name},class属性值为{class_name}")
        # 获取元素的文本内容
        res = self.driver.find_element(By.XPATH,'//*[@id="2"]/div/h3/a').text
        print(res)
        assert "霍格沃兹" in res