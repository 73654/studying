# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Test:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appium:deviceName"] = "kmob"
        caps["appium:appPackage"] = "cn.kmob.screenfingermovelock"
        caps["appium:appActivity"] = "com.samsung.ui.FlashActivity"
        caps["appium:noReset"] = "true"
        caps["appium:dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    def get_seat(self):
        x = 120
        y = 193
        distance = 240
        one_set = (x, y)
        two_set = (x + distance, y)
        three_set = (x + distance * 2, y)
        four_set = (x, y + distance)
        five_set = (x + distance, y + distance)
        six_set = (x + distance * 2, y + distance)
        seven_set = (x, y + distance * 2)
        eight_set = (x + distance, y + distance * 2)
        nine_set = (x + distance * 2, y + distance * 2)

    def test_action(self):
        x = 120
        y = 193
        distance = 240
        one_set = (x, y)
        two_set = (x + distance, y)
        three_set = (x + distance * 2, y)
        four_set = (x, y + distance)
        five_set = (x + distance, y + distance)
        six_set = (x + distance * 2, y + distance)
        seven_set = (x, y + distance * 2)
        eight_set = (x + distance, y + distance * 2)
        nine_set = (x + distance * 2, y + distance * 2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"),
                                            duration=100)
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//android.widget.ImageView[@content-desc='手势密码锁']").click()
        # 起始位置
        # actions.w3c_actions.pointer_action.move_to_location(120, 193)
        actions.w3c_actions.pointer_action.move_to_location(seven_set[0],seven_set[1])
        # 按下
        actions.w3c_actions.pointer_action.pointer_down()
        # 滑动
        actions.w3c_actions.pointer_action.move_to_location(two_set[0], two_set[1])
        actions.w3c_actions.pointer_action.move_to_location(nine_set[0], nine_set[1])
        actions.w3c_actions.pointer_action.move_to_location(four_set[0], four_set[1])
        actions.w3c_actions.pointer_action.move_to_location(three_set[0], three_set[1])
        actions.w3c_actions.pointer_action.move_to_location(eight_set[0], eight_set[1])
        actions.w3c_actions.pointer_action.move_to_location(one_set[0], one_set[1])
        actions.w3c_actions.pointer_action.move_to_location(six_set[0], six_set[1])
        actions.w3c_actions.pointer_action.move_to_location(five_set[0], five_set[1])
        # actions.w3c_actions.pointer_action.move_to_location(355, 19)
        # actions.w3c_actions.pointer_action.move_to_location(604, 198)
        # actions.w3c_actions.pointer_action.move_to_location(711, 439)
        # actions.w3c_actions.pointer_action.move_to_location(606, 679)
        # actions.w3c_actions.pointer_action.move_to_location(352, 842)
        # actions.w3c_actions.pointer_action.move_to_location(125, 675)
        # 抬起
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        # self.driver.back()
