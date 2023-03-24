from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseDriver:
    def __init__(self, driver=None):
        # 实例化 driver
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            # 设置全局隐式等待
            self.driver.implicitly_wait(3)
            self.driver.get("https://www.ceshiren.com")
        else:
            self.driver = driver

    # 找元素
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 找多个元素
    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    # 找元素并输入内容
    def find_and_input(self, by, value, text: str):
        self.find(by, value).send_keys(text)

    # 找元素并点击
    def find_and_click(self, by, value):
        self.find(by, value).click()

    # 找元素并输入内容
    def get_text(self, by, value):
        return self.find(by, value).text
