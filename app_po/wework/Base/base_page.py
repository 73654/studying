import os

import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common import actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_po.wework.utils.error_handle import black_wrapper
from app_po.wework.utils.utils import Utils
from utils.log_until import logger
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
    def find(self, by, value):
        '''
        查找元素,返回元素
        :param by:
        :param value:
        :return:
        '''
        logger.info(f"{value}通过{by}方式寻找")
        return self.driver.find_element(by, value)

    @black_wrapper
    def finds(self, by, value):
        '''
        查找多个元素,返回元素对象的列表
        :param by:
        :param value:
        :return:
        '''
        logger.info(f"{value}通过{by}方式寻找")
        return self.driver.find_elements(by, value)

    def find_and_click(self, by, value):
        '''
        查找元素并点击
        :param by:
        :param value:
        :return:
        '''
        logger.info(f"{value}通过{by}方式寻找并点击")
        self.driver.find_element(by, value).click()

    def find_and_sendkeys(self, by, value, text):
        '''
        查找元素并输入内容
        :param by:
        :param value:
        :return:
        '''
        logger.info(f"{value}通过{by}方式寻找并输入{text}")
        self.driver.find_element(by, value).send_keys(text)

    def find_and_text(self, by, value):
        logger.info(f"{value}通过{by}方式寻找并输出为text")
        return self.driver.find_element(by, value).text

    def set_implicitly_wait(self, time=1):
        '''
        设置隐式等待
        :param time:
        :return:
        '''
        logger.info(f"设置隐式等待时间为{time}秒")
        self.driver.implicitly_wait(time)

    # 滑动找元素并点击
    @black_wrapper
    def swipe_find(self, by, value):
        logger.info(f"{value}通过{by}方式滑动找到并点击")
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        startx = width / 2
        starty = height * 0.8
        endx = startx
        endy = height * 0.2
        duration = 0
        i = 1
        self.set_implicitly_wait(2)
        while True:
            eles = self.driver.find_elements(by=by, value=value)
            if i > 10:
                print("超过10次啦")
                break
            if len(eles) == 0:
                # print(f"第{i}次滑动")
                self.driver.swipe(startx, starty, endx, endy, duration)
                i += 1
            else:
                eles[0].click()
                self.set_implicitly_wait(2)
                break

    @black_wrapper
    def get_tips(self, by, value):
        '''
        获取toast 的文本
        :return:
        '''
        logger.info(f"{value}通过{by}方式并输出为text")
        return self.driver.find_element(by, value).text

    def swipe_element(self, by, value):
        logger.info(f"{value}通过{by}方式滑动找到并输出为text")
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        startx = width / 2
        starty = height * 0.8
        endx = startx
        endy = height * 0.2
        duration = 0
        i = 1
        while True:
            eles = self.driver.find_elements(by=by, value=value)
            if i > 10:
                print("超过10次啦")
                break
            if len(eles) == 0:
                # print(f"第{i}次滑动")
                self.driver.swipe(startx, starty, endx, endy, duration)
                i += 1
            else:
                return eles[0].text

    def delete_circulate(self, by, value):
        i = 1
        while True:
            eles = self.driver.find_elements(by=by, value=value)
            if i > 5:
                print("重名的有5个人?滚")
                break
            if len(eles) == 0:
                print(f"第{i}次删除")
                # 点击搜索结果
                el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
                el4.click()
                # 点击更多选项
                el5 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6l']")
                el5.click()
                # 编辑成员
                el6 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/c5x']")
                el6.click()
                self.swipe_find(AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gp1']")
                # 确认删除
                el7 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/cst']")
                el7.click()
                i += 1
            else:
                return eles[0]

    def wait_elements(self, locator, time=10):
        '''
        显式等待找元素后停止
        :param locator:
        :param time:
        :return:
        '''
        logger.info(f"显式等待找到{locator}后停止")
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_text(self, by, value):
        '''
        显式等待文本可见
        :param by:
        :param value:
        :return:
        '''
        try:
            logger.info(f"显式等待找到{by, value}文本可见停止")
            self.driver.find_element(by, value=value)
            return True
        except:
            return False

    def wait_for_text2(self, text, time=10):
        '''
        显式等待文本可见
        :param text:
        :param time:
        :return:
        '''
        try:
            logger.info(f"显式等待找到{text}文本可见停止")
            WebDriverWait(self.driver, time).until(
                expected_conditions.visibility_of_element_located((AppiumBy.XPATH, f"//*[@text='{text}']")),
                message=f"{text}没找到"
            )
            return True
        except TimeoutException as e:
            print(e)
            return False

    def wait_for_click(self, value, time=10):
        '''
        显式等待元素可点击
        :param value:
        :param time:
        :return:
        '''
        try:
            logger.info(f"显式等待找到{value}按钮可点击停止")
            WebDriverWait(self.driver, time).until(
                expected_conditions.element_to_be_clickable((AppiumBy.XPATH, value)),
            )
            return True
        except TimeoutException as e:
            print(e)
            return False

    def screenshot(self, root_path):
        '''
        截图
        :param root_path: 当前文件的路径
        :return: 截图保存的路径
        '''
        logger.info("完成截图操作")
        # 使用当前时间作为截图的文件名
        image_name = Utils.get_current_time() + ".png"
        # 拼接当前图片保存的路径
        image_dir_path = os.sep.join([root_path, "..", "image/"])
        # 如果图片保存路径不存在
        if not os.path.isdir(image_dir_path):
            # 创建这个路径
            os.mkdir(image_dir_path)
        # 拼接图片保存路径
        image_path = image_dir_path + image_name
        logger.info(f"截图路径为 {image_path}")
        # 截图
        self.driver.save_screenshot(image_path)
        return image_path

    def save_page_source(self, root_path):
        '''
        保存页面源码
        :param root_path: 当前文件的路径
        :return: 页面源码文件的路径
        '''
        logger.info("保存页面源码")
        # 使用当前时间作为页面源码的文件名
        page_source_name = Utils.get_current_time() + "_page_source.xml"
        # 拼接当前文件保存的路径
        page_source_dir_path = os.sep.join([root_path, "..", "page_source/"])
        # 如果文件保存路径不存在
        if not os.path.isdir(page_source_dir_path):
            # 创建这个路径
            os.mkdir(page_source_dir_path)
        # 拼接文件保存路径
        page_source_path = page_source_dir_path + page_source_name
        logger.info(f"page source 的保存路径为 {page_source_path}")
        # 写 page source 文件
        with open(page_source_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        return page_source_path
