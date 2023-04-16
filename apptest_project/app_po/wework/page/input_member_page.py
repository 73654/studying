import random

import allure
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.wework.Base.wework_app import BaseDriver


class InputMemberPage(BaseDriver):
    # 右上角输入方式按钮
    _INPUT_WAY = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/l6i']"
    # 姓名输入框
    _NAME_INPUT_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gpu']/child::*/child::*[3]"
    # 账号输入框
    _USERNAME_INPUT_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/goa']/child::*/child::*[3]"
    # 性别选择按钮
    _SEX_CHOICE_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gpb']"
    # 性别选择女按钮
    _SEX_CHOICE_WOMAN_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/cjp']/child::*[2]"
    # 企业邮箱输入框
    _EMAIL_INPUT_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/il8']/child::*/child::*[2]"
    # 手机号输入框
    _PHONE_INPUT_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/i4t']"
    # 姓名输入框2
    _NAME_INPUT_FRAME2 = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/byk']"
    # 保存按钮
    _SAVE_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/az1']"

    # 输入成员信息,点击保存按钮
    def input_member_info(self, name, phone):
        from apptest_project.app_po.wework.page.add_member_page import AddMemberPage
        with allure.step("填写新增人员信息"):
            # 获取右上角text
            ele = self.find_and_text(*self._INPUT_WAY)
            if ele == "快速输入":
                # 姓名输入框输入姓名
                self.find_and_sendkeys(*self._NAME_INPUT_FRAME, name)
                # 账号输入框输入手机号
                self.find_and_sendkeys(*self._USERNAME_INPUT_FRAME, phone)
                # 定义一个列表
                sex = ["男", "女"]
                # 随机选择列表的一个元素
                choice = random.choice(sex)
                print(choice)
                # 如果选择为 女 点击性别选择
                if choice == "女":
                    # 点击 男 按钮
                    self.find_and_click(*self._SEX_CHOICE_BTN)
                    # 显式等待性别选择框出现
                    self.wait_elements(self._SEX_CHOICE_WOMAN_BTN)
                    # 点击 女 按钮
                    self.find_and_click(*self._SEX_CHOICE_WOMAN_BTN)
                # 企业邮箱输入框输入手机号
                self.find_and_sendkeys(*self._EMAIL_INPUT_FRAME, phone)
                # 手机号输入框输入手机号
                self.find_and_sendkeys(*self._PHONE_INPUT_FRAME, phone)
            else:
                # 姓名输入框输入姓名
                self.find_and_sendkeys(*self._NAME_INPUT_FRAME2, name)
                # 手机输入框输入手机号
                self.find_and_sendkeys(*self._PHONE_INPUT_FRAME, phone)
        with allure.step("点击保存按钮"):
            # 滑动找到并点击保存元素
            self.swipe_find(*self._SAVE_BTN)
        with allure.step("跳转至添加成员页面"):
            # 跳转到添加成员页面
            return AddMemberPage(self.driver)
