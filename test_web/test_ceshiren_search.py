import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshirenSearch:
    def setup(self):
        # 实例化 driver
        self.driver = webdriver.Chrome()
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭 driver
        self.driver.quit()

    @pytest.mark.parametrize(
        "a, b", [
            ['selenium','selenium'],
            ['python','python']
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
        self.driver.find_element(By.XPATH,
                                 '//*[@id="ember6"]/header/div/div/div[2]/div/div/div/div/div[2]/ul/li/a/span[2]/span[2]').click()
        # 获取元素内容
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@id="ember6"]/header/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a/span[1]/span[1]/span[2]/span/span[1]').text
        print(ele)
        # 断言结果是否正确
        assert b in ele
