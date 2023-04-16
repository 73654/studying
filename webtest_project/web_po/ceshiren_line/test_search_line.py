import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
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

    @pytest.mark.parametrize(
        "a, b", [
            ['selenium', 'selenium-Selenium 1 (Selenium RC)'],
            ['python', '[12期 python] python pytest 实战2'],
            ['', '']
        ]
    )
    def test_ceshiren_search(self, a, b):
        # 打开测试人首页
        self.driver.get("https://www.ceshiren.com")
        # 点击搜索按钮元素
        self.driver.find_element(By.ID, 'search-button').click()
        # 点击详细搜索
        self.driver.find_element(By.CLASS_NAME, "fa.d-icon.d-icon-sliders-h.svg-icon.svg-node").click()
        # 找搜索框元素,并输入内容
        self.driver.find_element(By.CLASS_NAME,
                                 'full-page-search.search.no-blur.search-query.ember-text-field.ember-view').send_keys(
            a)
        # 点击搜索按钮
        self.driver.find_element(By.CLASS_NAME, "d-button-label").click()
        try:
            # 获取搜索成功后元素内容
            # ele = self.driver.find_element(By.CLASS_NAME,'search-highlight').text
            # # 断言结果是否正确
            # assert b in ele
            # print(f"搜索成功,搜索结果为{ele}")
            eles = self.driver.find_elements(By.CLASS_NAME, 'topic-title')
            names = [e.text for e in eles]
            assert b in names
            print(f"搜索成功,搜索结果为{names}")
        except AssertionError:
            # 获取搜索失败后元素内容
            ele2 = self.driver.find_element(By.CLASS_NAME, "fps-invalid").text
            assert ele2 == "您的搜索词过短。"
            print(f"搜索失败,提示信息为{ele2}")

    @pytest.mark.parametrize(
        "a, b", [
            ['看到奥德赛', '']
        ]
    )
    def test_ceshiren_search_fail(self, a, b):
        # 打开测试人首页
        self.driver.get("https://www.ceshiren.com")
        # 点击搜索按钮元素
        self.driver.find_element(By.ID, 'search-button').click()
        # 点击详细搜索
        self.driver.find_element(By.CLASS_NAME, "fa.d-icon.d-icon-sliders-h.svg-icon.svg-node").click()
        # 找搜索框元素,并输入内容
        self.driver.find_element(By.CLASS_NAME,
                                 'full-page-search.search.no-blur.search-query.ember-text-field.ember-view').send_keys(
            a)
        # 点击搜索按钮
        self.driver.find_element(By.CLASS_NAME, "d-button-label").click()
        ele3 = self.driver.find_element(By.XPATH,
                                        '/html/body/section/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/h3').text
        assert ele3 == "找不到结果。"
        print(f"搜索失败,提示信息为{ele3}")
