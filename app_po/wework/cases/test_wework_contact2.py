import allure
import pytest
from app_po.wework.Base.wework_app import BaseDriver
from app_po.wework.utils.utils import Utils
from utils.log_until import logger


@allure.epic("对企业微信增删改查成员功能进行测试")
@allure.feature("企业微信单元测试")
class TestWeworkContact:
    def setup_class(self):
        # 初始化 app
        self.app = BaseDriver()
        # 准备姓名和手机号
        self.name = self.app.start().faker.name()
        self.phone = self.app.start().faker.phone_number()
        self.new_name = "王西"

    def teardown_class(self):
        # 停止 app
        self.app.back()

    def setup(self):
        # 进入首页
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        # 停止 app
        # self.app.stop()
        # 返回主页面
        self.app.back_main()

    @pytest.mark.run(order=1)
    @pytest.mark.P0
    @allure.story("添加人员方法")
    @allure.title("添加人员功能测试")
    @pytest.mark.parametrize(
        "name,phone",
        Utils.get_yaml_data("../datas/member.yaml")["member"]
    )
    def test_add_contact(self, name, phone):
        '''
        测试步骤
        1.首页,点击通讯录按钮,进入通讯录页面
        2.通讯录页面,点击添加成员按钮,进入添加成员页面
        3.添加成员页面,点击手动输入按钮,进入手动输入成员信息页面
        4.手动输入成员信息页面,输入成员信息,点击保存,进入添加成员页面
        5.添加成员页面,获取 toast 信息,完成断言
        '''
        result = self.main.goto_address_list_page().goto_add_member_page().goto_input_member_page().input_member_info(
            name, phone).get_toast_tips()
        assert "添加成功" == result

    @pytest.mark.run(order=2)
    @pytest.mark.P0
    @allure.story("查找人员方法")
    @allure.title("查找人员功能测试")
    def test_select_member(self):
        '''
        测试步骤
        1.首页,点击通讯录按钮,进入通讯录页面
        2.通讯录页面,点击搜索按钮,进入搜索成员页面
        3.搜索成员页面输入搜索姓名,获取搜索结果
        '''
        result = self.main.goto_address_list_page().goto_search_page().search_member(self.new_name)
        # 断言搜索结果是否与搜索姓名一致
        assert result == self.new_name

    @pytest.mark.run(order=3)
    @pytest.mark.P0
    @allure.story("更新人员方法")
    @allure.title("更新人员功能测试")
    def test_update_member(self):
        '''
        测试步骤
        1.首页,点击通讯录按钮,进入通讯录页面
        2.通讯录页面,点击搜索按钮,进入搜索成员页面
        3.搜索成员页面输入搜索姓名,获取搜索结果后点击联系人,进入个人信息页面
        4.个人信息页面,点击更多选项,进入更多选项页面
        5.更多选项页面,点击编辑成员,进入编辑成员页面
        6.编辑成员页面,修改成员姓名及性别,点击保存,跳转个人信息页面
        7.搜索结果页面,获取更新后姓名,完成断言
        '''
        result = self.main.goto_address_list_page().goto_search_page().goto_message_page(
            "王东").goto_more_options_page().goto_revise_member_page().update_message(
            self.new_name).get_newname()
        # 断言修改后结果是否与新姓名一致
        assert result == self.new_name

    @pytest.mark.run(order=4)
    @pytest.mark.P0
    @allure.story("删除人员方法")
    @allure.title("删除人员功能测试")
    @pytest.mark.parametrize(
        "name",
        Utils.get_yaml_data("..\datas\member.yaml")["delete_name"]
    )
    def test_delete_member(self, name):
        '''
        测试步骤
        1.首页,点击通讯录按钮,进入通讯录页面
        2.通讯录页面,点击搜索按钮,进入搜索成员页面
        3.搜索成员页面输入搜索姓名,获取搜索结果后点击联系人,进入个人信息页面
        4.个人信息页面,点击更多选项,进入更多选项页面
        5.更多选项页面,点击编辑成员,进入编辑成员页面
        6.编辑成员页面,下滑点击删除成员按钮,点击确认删除,跳转到搜索结果页面
        7.搜索结果页面,获取无搜索结果文本,完成断言
        '''
        result = self.main.goto_address_list_page().goto_search_page().goto_message_page(
            name).goto_more_options_page().goto_revise_member_page().delete_member().get_delete_result()
        # 断言删除后 无搜索结果
        assert result == "无搜索结果"
        logger.info("删除成功")

    @pytest.mark.run(order=5)
    @pytest.mark.P1
    @allure.story("微信打卡方法")
    @allure.title("外出打卡功能测试")
    @allure.link("https://jingyan.baidu.com/article/eae07827b745905eed548505.html")
    @allure.testcase("https://jingyan.baidu.com/article/eae07827b745905eed548505.html")
    @allure.issue("https://jingyan.baidu.com/article/eae07827b745905eed548505.html")
    def test_punch_the_clock(self):
        '''
        测试步骤
        1.首页,点击工作台按钮,进入工作台页面
        2.工作台页面,点击打卡按钮,跳转打卡页面
        3.打卡页面点击外出打卡,点击第n次打卡,打卡成功返回成功信息,完成断言
        '''
        result = self.main.goto_staging_page().goto_punch_page().goout_punch_the_clock()
        assert "外出打卡成功" == result
