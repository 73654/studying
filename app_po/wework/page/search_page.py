import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from app_po.wework.Base.wework_app import BaseDriver


class SearchPage(BaseDriver):
    # 搜索框
    _SEARCH_FRAME = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/jf8']"
    # 搜索结果元素
    _SEARCH_RESULT = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gdx']/child::*"
    # 搜索结果按钮
    _SEARCH_RESULT_BTN = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gdx']"
    # 搜索不到结果元素
    _NOT_SEARCH_RESULT = AppiumBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dgl']"
    def search_member(self, name):
        with allure.step("搜索框输入姓名"):
            # 获取搜索框,并输入成员姓名
            self.find_and_sendkeys(*self._SEARCH_FRAME, name)
            exists = self.wait_for_text2("联系人")
            if not exists:
                pytest.xfail(reason=f"无搜索结果:{name}")
            # 判断搜索结果是否为1
            eles = self.finds(*self._SEARCH_RESULT)
            if len(eles) > 1:
                pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        with allure.step("返回搜索结果"):
            return eles[0].text


    def goto_message_page(self,name):
        from app_po.wework.page.message_page import MessagePage
        with allure.step("搜索框内输入姓名"):
            # 获取搜索框,并输入成员姓名
            self.find_and_sendkeys(*self._SEARCH_FRAME, name)
            exists = self.wait_for_text2("联系人")
            if not exists:
                pytest.xfail(reason=f"无搜索结果:{name}")
            # 判断搜索结果是否为1
            eles = self.finds(*self._SEARCH_RESULT)
            if len(eles) > 1:
                pytest.xfail(reason=f"搜索结果数量为:{len(eles)}")
        with allure.step("点击搜索结果"):
            # 点击搜索结果
            self.find_and_click(*self._SEARCH_RESULT_BTN)
        with allure.step("跳转至个人信息页面"):
            # 跳转到个人信息页面
            return MessagePage(self.driver)

    def get_delete_result(self):
        with allure.step("返回删除后文本"):
            # 返回删除后文本
            return self.find_and_text(*self._NOT_SEARCH_RESULT)

