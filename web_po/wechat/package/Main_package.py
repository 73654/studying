from selenium.webdriver.common.by import By

from web_po.wechat.package.Add_package import AddPackage
from web_po.wechat.package.BaseDriver import BaseDriver


class MainPackage(BaseDriver):
    def contact_click(self):
        # 找到并点击添加成员元素
        self.find_and_click(By.CLASS_NAME, "ww_indexImg.ww_indexImg_AddMember")
        return AddPackage(self.driver)
