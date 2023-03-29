from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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


# 滑动找元素并点击
def swipe_find(driver, by, value):
    window_size = driver.get_window_size()
    width = window_size["width"]
    height = window_size["height"]
    startx = width / 2
    starty = height * 0.8
    endx = startx
    endy = height * 0.2
    duration = 0
    i = 1
    while True:
        eles = driver.find_elements(by=by, value=value)
        if i > 10:
            print("超过10次啦")
            break
        if len(eles) == 0:
            print(f"第{i}次滑动")
            driver.swipe(startx, starty, endx, endy, duration)
            i += 1
        else:
            eles[0].click()
            break

def swipe_element(driver, by, value):
    window_size = driver.get_window_size()
    width = window_size["width"]
    height = window_size["height"]
    startx = width / 2
    starty = height * 0.8
    endx = startx
    endy = height * 0.2
    duration = 0
    i = 1
    while True:
        eles = driver.find_elements(by=by, value=value)
        if i > 10:
            print("超过10次啦")
            break
        if len(eles) == 0:
            print(f"第{i}次滑动")
            driver.swipe(startx, starty, endx, endy, duration)
            i += 1
        else:
           return eles[0].text

def delete_circulate(driver, by, value):
    i = 1
    while True:
        eles = driver.find_elements(by=by, value=value)
        if i > 5:
            print("重名的有5个人?滚")
            break
        if len(eles) == 0:
            print(f"第{i}次删除")
            # 点击搜索结果
            el4 = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/gdx']")
            el4.click()
            # 点击更多选项
            el5 = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/l6l']")
            el5.click()
            # 编辑成员
            el6 = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/c5x']")
            el6.click()
            swipe_find(driver, AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gp1']")
            # 确认删除
            el7 = driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.tencent.wework:id/cst']")
            el7.click()
            i += 1
        else:
            return eles[0]


# 生成随机姓名
def member_name():
    fake = Faker("zh_CN")
    name = fake.name()
    return name


# 生成随机手机号
def member_phone():
    fake = Faker("zh_CN")
    phone = fake.phone_number()
    return phone


# 显式等待找元素后停止
def wait_elements(driver, locator, time=10):
    WebDriverWait(driver, time).until(expected_conditions.visibility_of_element_located(locator))


def wait_for_text(driver, by, value):
    try:
        driver.find_element(by, value=value)
        return True
    except:
        return False


def wait_for_text2(driver, text, time=10):
    try:
        WebDriverWait(driver, time).until(
            expected_conditions.visibility_of_element_located((AppiumBy.XPATH, f"//*[@text='{text}']")),
            message=f"{text}没找到"
        )
        return True
    except TimeoutException as e:
        print(e)
        return False

def wait_for_click(driver,value,time=10):
    try:
        WebDriverWait(driver, time).until(
            expected_conditions.element_to_be_clickable((AppiumBy.XPATH, value)),
        )
        return True
    except TimeoutException as e:
        print(e)
        return False

