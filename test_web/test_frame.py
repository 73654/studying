import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web.until.log_until import logger


class TestFrame:
    def setup(self):
        # 实例化
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭,回收资源
        self.driver.quit()

    allure.story("登录测试")

    def test_switch_frame(self):
        # 打开网页
        logger.info(f"打开网页")
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        # 输入切换前源码到 record.html 文件中
        logger.info(f"输入切换前源码到 record.html 文件中")
        page_sourse_path = "./record.html"
        with open(page_sourse_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(page_sourse_path, name="page_sourse", attachment_type=allure.attachment_type.TEXT)
        # 定位 iframe 元素
        logger.info(f"定位 iframe 元素")
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe.iframe")
        # 切换到 iframe 当中
        logger.info(f"切换到 iframe 当中")
        self.driver.switch_to.frame(iframe)
        # 切换后,可以对 iframe 中的元素进行操作,定位练习按钮
        logger.info(f"切换后,可以对 iframe 中的元素进行操作,定位练习按钮")
        print(self.driver.find_element(By.ID, "frame_btn").text)
        # 截图
        img_path = "./screenshot/切换后截图.png"
        self.driver.save_screenshot(img_path)
        allure.attach.file(img_path, name="img", attachment_type=allure.attachment_type.PNG)
        # 输入切换后源码到 new_record.html 文件中
        page_sourse_path2 = "./new_record.html"
        logger.info(f"输入切换后源码到 new_record.html 文件中")
        with open(page_sourse_path2, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(page_sourse_path2, name="new_page_sourse", attachment_type=allure.attachment_type.TEXT)
        # 切换回原来的 frame
        logger.info(f"切换回原来的 frame")
        self.driver.switch_to.parent_frame()
        # 定位原来 frame 中的元素
        logger.info(f"定位原来 frame 中的元素")
        self.driver.find_element(By.ID, "primary_btn").click()
        time.sleep(3)
