import time
from selenium.webdriver.common.by import By
from web_po.wechat.package.BaseDriver import BaseDriver
from web_po.wechat.package.Contact_package import ContactPackage


class AddPackage(BaseDriver):
    def test_add(self, name, uuid, phone_number):
        # 找姓名输入框元素,输入姓名 name
        self.find_and_input(By.ID, "username", name)
        # 找账号输入框元素,输入随机账号
        self.find_and_input(By.ID, "memberAdd_acctid", uuid)
        # 找手机号输入框元素,输入随机手机号
        self.find_and_input(By.ID, "memberAdd_phone", phone_number)
        # 点击保存
        self.find_and_click(By.CLASS_NAME, 'qui_btn.ww_btn.js_btn_save')

        return self

    def get_success(self):
        # 找 保存成功 元素 输出文本
        success_text = self.get_text(By.ID, "js_tips")
        return success_text

    def get_element(self):
        return ContactPackage(self.driver)

    def get_fail(self):
        time.sleep(2)
        # 找错误提示信息元素 输出列表
        eles = self.finds(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips")
        return eles
