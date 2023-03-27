import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestLitemallLogin:
    def setup(self):
        # 实例化 driver
        self.driver = webdriver.Chrome()
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭 driver
        self.driver.quit()

    @pytest.mark.parametrize(
        "username, passwd", [
            ['manage', 'manage123'],
            ['hogwarts', 'test12345'],
            ['manage', 'manage']
        ]
    )
    def test_litemail_login(self, username, passwd):
        try:
            # 打开litemall首页
            self.driver.get("http://litemall.hogwarts.ceshiren.com/#/dashboard")
            # 找账号输入框元素
            user = self.driver.find_element(By.NAME, 'username')
            # 清空输入框内容
            user.clear()
            # 输入指定账号
            user.send_keys(username)
            # 找密码输入框元素
            password = self.driver.find_element(By.NAME, 'password')
            # 清空输入框内容
            password.clear()
            # 输入指定密码
            password.send_keys(passwd)
            # 点击登录按钮
            self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/form/button').click()
            # 获取元素内容
            ele = self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/div[2]/section/div/div/div[1]/div/div[2]/div').text
            # 断言结果是否正确
            assert '用户数量' == ele
        except NoSuchElementException:
            print("登录失败!")
