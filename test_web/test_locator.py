from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocator:
    def setup(self):
        # 实例化driver
        self.driver = webdriver.Chrome()
        # 设置全局隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 关闭driver
        self.driver.quit()

    def test_locator_by_id(self):
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过id来定位元素
        ele = self.driver.find_element(By.ID, "located_id")
        print(ele)

    def test_locator_by_name(self):
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过 name 属性来定位元素
        ele = self.driver.find_element(By.NAME, "located_name")
        print(ele)

    def test_locator_by_css_selector(self):
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过 css_selector 属性来定位元素
        ele = self.driver.find_element(By.CSS_SELECTOR, "#located_id")
        print(ele)

    def test_locator_by_link(self):
        '''
        定位a标签
        '''
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过 link 属性来定位元素
        ele = self.driver.find_element(By.LINK_TEXT, "link")
        print(ele)
        # 通过 partial link 定位
        ele2 = self.driver.find_element(By.PARTIAL_LINK_TEXT, "lin")
        print(ele2)
    def test_lacator_by_tag_name(self):
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过标签名定位元素, 一般会返回多个元素
        eles = self.driver.find_elements(By.TAG_NAME,"a")
        print(eles[0])
    def test_lacator_by_class(self):
        # 打开web页面
        self.driver.get("https://vip.ceshiren.com/#/ui_study/locate")
        # 通过 class 属性也可以找到多个元素
        eles = self.driver.find_elements(By.CLASS_NAME,"el-button")
        print(eles[0])