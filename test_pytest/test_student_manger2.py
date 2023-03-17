import allure
import pytest
import yaml

from script.student import Student
from script.student_manger import StudentManager
from utils.log_until import logger


def teardown_module():
    print("测试结束")


def studentyaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return (data)

@allure.epic("学生信息管理系统")
@allure.feature("单元测试")
class TestStudentManger:
    """
    学生信息管理系统单元测试
    """

    def setup(self):
        # 1.实例化学生信息管理类
        self.sm = StudentManager()
        # 2.实例化学生
        # self.stu = Student("xcz", 80)

    @pytest.mark.parametrize(
        "name, score", studentyaml("D:/project/data/student.yaml")["student"]
        #     [
        #         ["xcz", 80],
        #         ["wzl", 90],
        #         ["gsj", 100],
        #         ["wsr", 99]
        #     ]
    )
    @pytest.mark.P0
    @allure.title("添加学生的方法,学生姓名为{name},学生的成绩为{score}")
    @allure.story("添加学生")
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @allure.description("添加学生的冒烟用例")
    def test_add(self, name, score):
        """
        测试添加学生方法
        """
        # 测试步骤
        stu = Student(name, score)
        # 3.调用学生信息管理类中的添加学生方法
        with allure.step("调用学生信息管理类中的添加学生方法"):
            self.sm.add(stu)
            logger.info(f"添加的学生姓名为{stu.name}")
            logger.info(f"添加的学生成绩为{stu.score}")
        # 断言
        # 获取当前学生信息管理系统中所有的学生姓名,放到列表中
        with allure.step("获取当前学生信息管理系统中所有的学生姓名,放到列表中"):
            stu_name_list = []
        # 遍历学生信息管理系统中 students 列表
        with allure.step("遍历学生信息管理系统中 students 列表"):
            for s in self.sm.students:
            # 把每一次遍历到的学生实例中的 name 属性拿到,放到学生姓名列表中
                stu_name_list.append(s.name)
        with allure.step("断言添加结果是否正确"):
            print(stu_name_list)
            assert name in stu_name_list

    @pytest.mark.parametrize(
        "name, score", studentyaml("D:/project/data/student.yaml")["student"]
        # [
        #     ["xcz", 80],
        #     ["wzl", 90],
        #     ["gsj", 100],
        #     ["wsr", 99]
        # ]
    )
    @pytest.mark.P0
    @allure.title("删除学生的方法,学生姓名为{name},学生的成绩为{score}")
    @allure.story("删除学生")
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @allure.description("删除学生的冒烟用例")
    def test_del(self, name, score):
        """
        测试删除学生方法
        """
        stu = Student(name, score)
        # 3.调用学生信息管理类中的添加学生方法
        with allure.step("调用学生信息管理类中的添加学生方法"):
            self.sm.add(stu)
        # 4.调用学生信息管理类中的删除学生方法
        with allure.step("调用学生信息管理类中的删除学生方法"):
            self.sm.remove(stu.name)
        # 获取当前学生信息管理系统中所有的学生姓名,放到列表中
        with allure.step("获取当前学生信息管理系统中所有的学生姓名,放到列表中"):
            stu_name_list = []
        # 遍历学生信息管理系统中 students 列表
        with allure.step("遍历学生信息管理系统中 students 列表"):
            for s in self.sm.students:
            # 把每一次遍历到的学生实例中的 name 属性拿到,放到学生姓名列表中
                stu_name_list.append(s.name)
        with allure.step("断言添加结果是否正确"):
            print(stu_name_list)
            assert name not in stu_name_list

    @pytest.mark.parametrize(
        "name, score", studentyaml("D:/project/data/student.yaml")["student"]
        # [
        #     ["xcz", 80],
        #     ["wzl", 90],
        #     ["gsj", 100],
        #     ["wsr", 99]
        # ]
    )
    @allure.title("查询学生的方法,学生姓名为{name},学生的成绩为{score}")
    @pytest.mark.P0
    @allure.story("查询学生")
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @allure.description("查询学生的冒烟用例")
    def test_sel(self, name, score):
        """
        测试获取学生信息方法
        """
        stu = Student(name, score)
        # 3.调用学生信息管理类中的添加学生方法
        with allure.step("调用学生信息管理类中的添加学生方法"):
            self.sm.add(stu)
        # 4.调用查询学生信息方法
        with allure.step("调用学生信息管理类中的查询学生方法"):
            result_stu = self.sm.get_student_info(stu.name)
        # 断言
        with allure.step("断言 姓名,分数 正确"):
            assert name == result_stu.name
            assert score == result_stu.score

    @pytest.mark.parametrize(
        "name, score,name1, score1,name2, score2,name3, score3,avg", studentyaml("D:/project/data/student.yaml")["avg"]
        # [
        #     ["xcz", 80, "wzl", 90, "gsj", 100, "wsr", 99, 92.25],
        #     ["zxb", 120, "cyw", 150, "nqf", 130, "wzl2", 0, 100]
        # ]
    )
    @allure.title("求平均分的方法")
    @pytest.mark.P0
    @allure.story("求平均分")
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @allure.description("求平均分的冒烟用例")
    def test_avg(self, name, score, name1, score1, name2, score2, name3, score3, avg):
        """
        测试计算平均分方法
        """
        stu = Student(name, score)
        stu1 = Student(name1, score1)
        stu2 = Student(name2, score2)
        stu3 = Student(name3, score3)
        # 3.调用学生信息管理类中的添加学生方法
        with allure.step("调用学生信息管理类中的添加学生方法"):
            self.sm.add(stu)
            self.sm.add(stu1)
            self.sm.add(stu2)
            self.sm.add(stu3)
        # 4.调用计算平均分方法
        with allure.step("调用计算平均分方法"):
            avg_score = self.sm.average_score()
        with allure.step("断言计算结果是否正确"):
            assert avg == avg_score
