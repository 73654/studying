from selenium.webdriver.common.by import By
from utils.log_until import logger
from web_po.wechat.package.BaseDriver import BaseDriver


class ContactPackage(BaseDriver):
    def test_main(self):
        from web_po.wechat.package.Add_package import AddPackage
        # 显式等待跳转到添加成员页面
        click_element = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        waite_element = (By.ID, 'username')
        self.wait_element_show(click_element, waite_element)
        return AddPackage(self.driver)

    def select_member(self, name):
        # 显式等待所有姓名元素加载成功后结束延迟
        self.wait_elements((By.CSS_SELECTOR, "td:nth-child(2)"))
        # 判断是否存在多页
        i = 1
        logger.info(f"第{i}次点击添加成员按钮")
        while True:
            # 找下一页按钮元素并输出到列表中
            eles = self.finds(By.CLASS_NAME, "ww_pageNav_info_arrowWrap.js_next_page")
            if i >= 10:
                logger.info(f"i>10跳出循环")
                break
            if len(eles) == 0:
                logger.info(f"没有多页,跳出循环")
                break
            else:
                # 找成员姓名元素输出到列表中
                result = self.finds(By.CSS_SELECTOR, "td:nth-child(2)")
                names = [e.text for e in result]
                if name in names:
                    logger.info(f"当前页找到人员跳出循环")
                    break
                else:
                    logger.info(f"没找到人员点击下一页")
                    self.find_and_click(By.CLASS_NAME, "ww_pageNav_info_arrowWrap.js_next_page")
                    i += 1
        # 断言添加结果是否正确
        result = self.finds(By.CSS_SELECTOR, "td:nth-child(2)")
        names = [e.text for e in result]
        return names
