from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestWinxin:
    def setup(self):
        # 实例化 driver
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭 driver
        print("用例执行完成")

    def test_weixin(self):
        # 打开企业微信页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 定位页面元素
        ele = self.driver.find_element(By.CLASS_NAME,"frame_nav_item_title").text
        assert ele == "首页"

