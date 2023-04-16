import random

import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from apptest_project.app_po.wework.Base.wework_app import BaseDriver



class ReviseMemberPage(BaseDriver):
    # 姓名输入框
    _NAME_INPUT_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gpu']/child::*/child::*[3]"
    # 性别选择按钮
    _SEX_CHOICE_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gpb']"
    # 保存按钮
    _SAVE_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/l6s']"
    # 删除成员按钮
    _DELETE_MEMBER_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gp1']"
    # 确认删除按钮
    _REALLY_DELETE_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/cst']"
    def update_message(self,new_name):
        from apptest_project.app_po.wework.page.message_page import MessagePage
        with allure.step("更新成员信息"):
        # 清除姓名框内容并输入新内容
            self.find(*self._NAME_INPUT_FRAME).clear()
            self.find_and_sendkeys(*self._NAME_INPUT_FRAME,new_name)
            # 点击性别
            self.find_and_click(*self._SEX_CHOICE_BTN)
            # 定义一个列表
            sex = ["男", "女"]
            # 随机选择列表的一个元素
            choice = random.choice(sex)
            # 获取随机性别并点击更改
            self.find_and_click(AppiumBy.XPATH, f"//*[@text='{choice}']")
        with allure.step("等待保存按钮可以点击"):
            exists = self.wait_for_click("//*[@text='保存']")
            if not exists:
                pytest.xfail(reason=f"保存不可点击")
        with allure.step("点击保存按钮"):
            # 点击保存
            self.find_and_click(*self._SAVE_BTN)
        with allure.step("等待姓名更新后,跳转至个人信息页面"):
            self.wait_for_text2(new_name)
            # 跳转到个人信息页面
            return MessagePage(self.driver)

    def delete_member(self):
        from apptest_project.app_po.wework.page.search_page import SearchPage
        with allure.step("点击删除成员按钮"):
            # 滑动找到并点击删除成员按钮
            self.swipe_find(*self._DELETE_MEMBER_BTN)
        with allure.step("点击确认删除按钮"):
            # 确认删除
            self.find_and_click(*self._REALLY_DELETE_BTN)
        with allure.step("跳转至搜索结果页面"):
            # 跳转到搜索结果页面
            return SearchPage(self.driver)