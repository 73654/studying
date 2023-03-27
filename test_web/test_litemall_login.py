import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from test_web.until.log_until import logger


@allure.feature("litemall单元测试")
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
        ],ids=["使用manage账号登录","使用默认账号登录","使用错误账号密码登录"]
    )
    @allure.story("登录方法")
    @allure.step
    @allure.title("litemall登录测试")
    def test_litemail_login(self, username, passwd):
        try:
            # 打开litemall首页
            with allure.step("打开网页"):
                self.driver.get("http://litemall.hogwarts.ceshiren.com/#/dashboard")
                logger.info(f"截图登录页面")
                old_img_path = "./screenshot/登录页面.png"
                self.driver.save_screenshot(old_img_path)
                allure.attach.file(old_img_path, name="old_img", attachment_type=allure.attachment_type.PNG)
            # 找账号输入框元素
            with allure.step("找账号输入框元素"):
                user = self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/form/div[2]/div/div/input')
            # 清空输入框内容
            with allure.step("清空账号输入框内容"):
                user.clear()
            # 输入指定账号
            with allure.step("输入指定账号"):
                user.send_keys(username)
            # 找密码输入框元素
            with allure.step("找密码输入框元素"):
                password = self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/form/div[3]/div/div/input')
            # 清空输入框内容
            with allure.step("清空密码输入框内容"):
                password.clear()
            # 输入指定密码
            with allure.step("输入指定密码"):
                password.send_keys(passwd)
            # 点击登录按钮
            with allure.step("点击登录按钮"):
                self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/form/button').click()
            # 获取元素内容
            with allure.step("获取元素内容,并输出给ele"):
                ele = self.driver.find_element(By.XPATH, '//*[@id="test_app"]/div/div[2]/section/div/div/div[1]/div/div[2]/div').text
            # 断言结果是否正确
            with allure.step("断言登录结果是否正确"):
                assert '用户数量' == ele
                logger.info("登录成功!输出首页源码到home_record文件中")
                page_sourse_path = "./home_record.html"
                with open(page_sourse_path, "w", encoding="utf-8") as f:
                    f.write(self.driver.page_source)
                allure.attach.file(page_sourse_path, name="page_sourse", attachment_type=allure.attachment_type.TEXT)
                logger.info(f"截图首页")
                img_path = "./screenshot/首页.png"
                self.driver.save_screenshot(img_path)
                allure.attach.file(img_path, name="new_img", attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            logger.info("登录失败!")
