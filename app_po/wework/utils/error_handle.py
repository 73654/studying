import os

import allure
from appium.webdriver.common.appiumby import AppiumBy

from utils.log_until import logger

# 弹窗黑名单
black_list = [
    (AppiumBy.XPATH, "//*[@text='取消']"),
    (AppiumBy.XPATH, "//*[@text='确定']"),
    (AppiumBy.XPATH, "//*[@text='马上升级']")
]

# func 就相当与把 find() 方法传进来
def black_wrapper(func):
    def run(*args, **kwargs):
        # 传入第一个参数 self
        basepage = args[0]
        try:
            logger.info(f"开始查找元素: {args[1], args[2]}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.info("没有找到元素，开始异常处理")
            # 获取 root path
            root_path = os.path.dirname(os.path.abspath(__file__))
            # 截图
            image_path = basepage.screenshot(root_path)
            # 添加到报告中
            allure.attach.file(image_path, name="查找元素异常截图", attachment_type=allure.attachment_type.PNG)
            # 保存 page source
            page_source_path = basepage.save_page_source(root_path)
            allure.attach.file(page_source_path, name="元素查找异常page_source", attachment_type=allure.attachment_type.TEXT)
            # 遍历黑名单列表，查找里面的元素进行操作
            for b in black_list:
                eles = basepage.driver.find_elements(*b)
                # 如果定位到的元素返回的列表长度大于0，代表确实找到了
                if len(eles) > 0:
                    # 点击弹窗中的按钮
                    eles[0].click()
                    # 继续查找元素
                    func(*args, **kwargs)
            logger.info(f"遍历黑名单，仍然未找到元素，异常信息为 {e}")
            raise e
    return run
