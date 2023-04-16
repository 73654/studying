import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWinxin:
    # def setup(self):
    #     # 实例化 driver
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     # 设置全局隐式等待
    #     self.driver.implicitly_wait(3)
    #     self.fake = Faker("zh_CN")
    def setup(self):
        self.driver = webdriver.Chrome()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax',
             'secure': False,
             'value': 'PdppJBtjraXW1XgzIaavpwraDlIPyEx9246lTp5LpYWVyVBw9nZJtMNonwTmbzH44kDW0kuVem7jNrQhq3-m8dxboLKO5erH2yJcpnhHxJtdPlMmK53daB2sbvdEqWG3WngSJORH42dgw-s96AF6fluym5hQw8ZOFRUrUBNG8RhkGDKD8MJMSWYfeeYwhgMELw00aXxBWRHfjFohg6m0loJ4klmZ_4yZg44NMHyP5BBssZLFlJcBTcx0YR0KA4bU1fFaWpairrw8LQcQB8g5pA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1688856670530939'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1970325051548868'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1688856670530939'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': '1787113533415496'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'B2PhKiS9LASRvw-Dc6ZYYC-2CzqQ08UIoxlZ8s693oF11c18LoitFhPdfPqjTwov'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1711073206, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'sameSite': 'Lax',
             'secure': False, 'value': 'a3287985'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1682219962, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zh'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)
        self.fake = Faker("zh_CN")

    def teardown(self):
        # 关闭 driver
        self.driver.quit()
        print("用例执行完成")

    def test_weixin(self):
        # 打开企业微信添加成员页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 点击添加成员按钮
        while True:
            eles = self.driver.find_elements(By.ID, "memberAdd_acctid")
            if len(eles) == 0:
                self.driver.find_element(By.CSS_SELECTOR,'.ww_operationBar .js_add_member').click()
            else:
                break
        # 生成随机姓名
        name = self.fake.name()
        # 找姓名输入框元素,输入姓名 name
        self.driver.find_element(By.ID, "username").send_keys(name)
        # 找账号输入框元素,输入随机账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.fake.uuid4())
        # 找手机号输入框元素,输入随机手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.fake.phone_number())
        # 保存
        self.driver.find_element(By.CLASS_NAME, 'qui_btn.ww_btn.js_btn_save').click()
        # 找 保存成功 元素 输出文本
        success_text = self.driver.find_element(By.ID, "js_tips").text
        # 断言 输出结果是否正确
        assert "保存成功" == success_text
        # 显式等待所有姓名元素加载成功后结束延迟
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(2)"))
        )
        # 断言添加结果是否正确
        result = self.driver.find_elements(By.CSS_SELECTOR, "td:nth-child(2)")
        names = [e.text for e in result]
        assert name in names
        print(f"{name}添加成功")
    # def test_aaa(self):
    #     while True:
    #         self.test_weixin()
    #         time.sleep(3)