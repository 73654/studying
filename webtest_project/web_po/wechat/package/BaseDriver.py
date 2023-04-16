import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_until import logger


class BaseDriver:

    def __init__(self, driver=None):
        # 实例化 driver
        if driver is None:
            self.driver = webdriver.Chrome()
            with open("cookie.yaml", "r", encoding="utf-8") as f:
                cookies = yaml.safe_load(f)
            # 打开网页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 把cookies添加到网页cookie中
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 设置全局隐式等待
            self.driver.implicitly_wait(3)
            # 实例化 fake
            self.fake = Faker("zh_CN")
            # 打开网页
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = driver

    # 找元素
    def find(self, by, value=None):
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, value)

    # 找多个元素
    def finds(self, by, value=None):
        if isinstance(by, tuple):
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, value)

    # 找元素并输入内容
    def find_and_input(self, by, value, text: str):
        self.find(by, value).send_keys(text)

    # 找元素并点击
    def find_and_click(self, by, value=None):
        if isinstance(by, tuple):
            self.find(*by).click()
        else:
            self.find(by, value).click()

    # 找元素并输入内容
    def get_text(self, by, value):
        return self.find(by, value).text

    # 显式等待
    def wait_elements(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    # 释放 driver
    def close_browser(self):
        self.driver.quit()

    # While循环找元素
    def wait_element_show(self, click_element, waite_element, click_num=10):
        i = 1
        while True:
            logger.info(f"第{i}次点击添加成员按钮")
            eles = self.finds(waite_element)
            if i >= click_num:
                break
            if len(eles) == 0:
                self.find_and_click(click_element)
                i += 1
            else:
                break
