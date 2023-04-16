from faker import Faker
from utils.log_until import logger
from webtest_project.web_po.wechat.package.Main_package import MainPackage


class Testsearch:
    def setup(self):
        self.main = MainPackage()
        # 实例化 fake
        self.fake = Faker("zh_CN")

    def teardown(self):
        self.main.close_browser()

    def test_success(self):
        name = self.fake.name()
        uuid = self.fake.uuid4()
        phone_number = self.fake.phone_number()
        # result = self.main.contact_click().test_main().test_add(name, uuid, phone_number).get_success()
        result = self.main.contact_click().test_add(name, uuid, phone_number).get_success()
        print(result)
        assert "保存成功" == result

    def test_element_success(self):
        name = self.fake.name()
        uuid = self.fake.uuid4()
        phone_number = self.fake.phone_number()
        result = self.main.contact_click().test_add(name, uuid, phone_number).get_element().select_member(name)
        assert name in result
        logger.info(f"{name}添加成功")

    def test_fail(self):
        # name = self.fake.name()
        name = "郗辰政"
        uuid = self.fake.uuid4()
        # phone_number = self.fake.phone_number()
        phone_number = 17734595423
        result = self.main.contact_click().test_add(name, uuid, phone_number).get_fail()
        assert len(result) != 0
        error = [e.text for e in result]
        logger.info(f"错误提示信息:{error}")
