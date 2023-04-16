import time

import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookie:
    def setup(self):
        # 实例化 driver
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)
        self.fake = Faker("zh_CN")
        # 打开企业微信添加成员页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    def test_get_cookie(self):
        cookies = self.driver.get_cookies()
        with open("cookie.yaml", "w", encoding="utf-8")as f:
            yaml.dump(cookies, f)


# def test_set_cookie():
#     driver = webdriver.Chrome()
#     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'PdppJBtjraXW1XgzIaavpwraDlIPyEx9246lTp5LpYWVyVBw9nZJtMNonwTmbzH44kDW0kuVem7jNrQhq3-m8dxboLKO5erH2yJcpnhHxJtdPlMmK53daB2sbvdEqWG3WngSJORH42dgw-s96AF6fluym5hQw8ZOFRUrUBNG8RhkGDKD8MJMSWYfeeYwhgMELw00aXxBWRHfjFohg6m0loJ4klmZ_4yZg44NMHyP5BBssZLFlJcBTcx0YR0KA4bU1fFaWpairrw8LQcQB8g5pA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1688856670530939'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1970325051548868'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1688856670530939'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1787113533415496'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'B2PhKiS9LASRvw-Dc6ZYYC-2CzqQ08UIoxlZ8s693oF11c18LoitFhPdfPqjTwov'}, {'domain': '.work.weixin.qq.com', 'expiry': 1711073206, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'a3287985'}, {'domain': '.work.weixin.qq.com', 'expiry': 1682219962, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zh'}]
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
#     time.sleep(10)