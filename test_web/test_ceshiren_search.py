import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web.until.log_until import logger


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
        logger.info(f"打开测试人首页")
        self.driver.get("https://www.ceshiren.com")
        logger.info(f"输入首页源码到 home_record.html 文件中")
        page_sourse_path = "./home_record.html"
        with open(page_sourse_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(page_sourse_path, name="page_sourse", attachment_type=allure.attachment_type.TEXT)
        logger.info(f"获取到元素前截图")
        old_img_path = "./screenshot/未获取到该元素.png"
        self.driver.save_screenshot(old_img_path)
        allure.attach.file(old_img_path, name="old_img", attachment_type=allure.attachment_type.PNG)
        # 点击搜索按钮元素
        logger.info(f"点击搜索按钮元素")
        self.driver.find_element(By.ID, 'search-button').click()
        # 找搜索框元素
        logger.info(f"找搜索框元素")
        self.driver.find_element(By.ID, 'search-term').send_keys(a)
        # 点击在所有话题和帖子中
        logger.info(f"点击在所有话题和帖子中")
        self.driver.find_element(By.CLASS_NAME,'keyword').click()
        # 获取元素内容
        logger.info(f"获取元素内容")
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME,'first-line'))
        ).text
        logger.info(f"获取到元素后截图")
        img_path = "./screenshot/获取到该元素.png"
        self.driver.save_screenshot(img_path)
        allure.attach.file(img_path, name="new_img", attachment_type=allure.attachment_type.PNG)
        logger.info(f"断言结果是否正确")
        # 断言结果是否正确
        assert b in ele
