from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        if i > 5:
            print("超过5次啦")
            break
        if len(eles) == 0:
            print(f"第{i}次滑动")
            driver.swipe(startx, starty, endx, endy, duration)
            i += 1
        else:
            eles[0].click()
            break


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
    WebDriverWait(driver, time).until(
        expected_conditions.visibility_of_element_located(locator)
    )
