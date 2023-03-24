import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestCeshirenSearch:
    def setup(self):
        # 实例化 driver
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭 driver
        self.driver.quit()

    @pytest.mark.parametrize(
        "a, b", [
            ['selenium','selenium-Selenium 1 (Selenium RC)'],
            ['python','[12期 python] python pytest 实战2']
        ]
    )
    def test_ceshiren_search(self, a, b):
        # 打开测试人首页
        self.driver.get("https://www.ceshiren.com")
        # 点击搜索按钮元素
        self.driver.find_element(By.ID, 'search-button').click()
        # 找搜索框元素
        self.driver.find_element(By.ID, 'search-term').send_keys(a)
        # 点击在所有话题和帖子中
        self.driver.find_element(By.CLASS_NAME,'keyword').click()
        # 获取元素内容
        eles = self.driver.find_elements(By.CLASS_NAME,'first-line')
        # 获取所有的标题内容,放到列表中
        # names = []
        # for e in eles:
        #     print(e.text)
        #     names.append(e.text)
        names = [e.text for e in eles]
        # 断言结果是否正确
        assert b in names