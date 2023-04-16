from faker import Faker

from webtest_project.web_po.ceshiren_line.package.Main_package import MainPackage



class Testsearch:
    def setup(self):
        self.main = MainPackage()



    def test_search(self):
        keyword_text = 'selenium'
        result = self.main.test_main_search().test_search_search(keyword_text).get_search_result()
        assert keyword_text in result[0]
        print(f"搜索成功,搜索结果为{result}")

    def test_search_fail(self):
        keyword_text= ''
        result = self.main.test_main_search().test_search_search(keyword_text).get_search_result_fail()
        assert  "您的搜索词过短。" in result
        print(f"搜索失败,提示信息为{result}")

    def test_search_fail2(self):
        keyword_text='看到奥德赛'
        result = self.main.test_main_search().test_search_search(keyword_text).get_search_reasult_fail2()
        assert "找不到结果。" in result
        print(f"搜索失败,提示信息为{result}")
    def test_abc(self):
        self.fake = Faker("zh_CN")
        print(self.fake.name())
        print(self.fake.phone_number())