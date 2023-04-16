import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common import actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        '''
        查找元素,返回元素
        :param by:
        :param value:
        :return:
        '''
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        '''
        查找多个元素,返回元素对象的列表
        :param by:
        :param value:
        :return:
        '''
        return self.driver.find_elements(by, value)

    def find_and_click(self, by, value):
        '''
        查找元素并点击
        :param by:
        :param value:
        :return:
        '''
        self.driver.find_element(by, value).click()

    def find_and_sendkeys(self, by, value, text):
        '''
        查找元素并输入内容
        :param by:
        :param value:
        :return:
        '''
        self.driver.find_element(by, value).send_keys(text)

    def find_and_text(self, by, value):
        return self.driver.find_element(by, value).text

    def set_implicitly_wait(self, time=1):
        '''
        设置隐式等待
        :param time:
        :return:
        '''
        self.driver.implicitly_wait(time)

    # 滑动找元素并点击
    def swipe_find(self, by, value):
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
                eles[0].click()
                break

    def get_tips(self, by, value):
        '''
        获取toast 的文本
        :return:
        '''
        return self.driver.find_element(by, value).text

    def swipe_element(self, by, value):
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

    # 生成随机姓名
    def member_name(self):
        fake = Faker("zh_CN")
        name = fake.name()
        return name

    # 生成随机手机号
    def member_phone(self):
        fake = Faker("zh_CN")
        phone = fake.phone_number()
        return phone

    def wait_elements(self, locator, time=10):
        '''
        显式等待找元素后停止
        :param locator:
        :param time:
        :return:
        '''
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_text(self, by, value):
        '''
        显式等待文本可见
        :param by:
        :param value:
        :return:
        '''
        try:
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
            WebDriverWait(self.driver, time).until(
                expected_conditions.element_to_be_clickable((AppiumBy.XPATH, value)),
            )
            return True
        except TimeoutException as e:
            print(e)
            return False
