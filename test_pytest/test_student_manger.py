from script.student import Student
from script.student_manger import StudentManager


class TestStudentManger:
    """
    学生信息管理系统单元测试
    """

    def test_add(self):
        """
        测试添加学生方法
        """
        # 测试步骤
        # 1.实例化学生信息管理类
        sm = StudentManager()
        # 2.实例化学生
        stu = Student("xcz", 80)
        # 3.调用学生信息管理类中的添加学生方法
        sm.add(stu)
        # 断言
        # 获取当前学生信息管理系统中所有的学生姓名,放到列表中
        stu_name_list = []
        # 遍历学生信息管理系统中 students 列表
        for s in sm.students:
            # 把每一次遍历到的学生实例中的 name 属性拿到,放到学生姓名列表中
            stu_name_list.append(s.name)
        print(stu_name_list)
        assert "xcz" in stu_name_list

    def test_del(self):
        """
        测试删除学生方法
        """
        # 1.实例化学生信息管理类
        sm = StudentManager()
        # 2.实例化学生
        stu1 = Student("xcz", 80)
        stu2 = Student("wzl", 10)
        # 3.调用学生信息管理类中的添加学生方法
        sm.add(stu1)
        sm.add(stu2)
        # 4.调用学生信息管理类中的删除学生方法
        sm.remove(stu1.name)
        # 获取当前学生信息管理系统中所有的学生姓名,放到列表中
        stu_name_list = []
        # 遍历学生信息管理系统中 students 列表
        for s in sm.students:
            # 把每一次遍历到的学生实例中的 name 属性拿到,放到学生姓名列表中
            stu_name_list.append(s.name)
        print(stu_name_list)
        assert "xcz" not in stu_name_list

    def test_sel(self):
        """
        测试获取学生信息方法
        """
        # 1.实例化学生信息管理类
        sm = StudentManager()
        # 2.实例化学生
        stu = Student("xcz", 80)
        # 3.调用学生信息管理类中的添加学生方法
        sm.add(stu)
        # 4.调用查询学生信息方法
        result_stu = sm.get_student_info(stu.name)
        # 断言
        assert "xcz" == result_stu.name
        assert 80 == result_stu.score

    def test_avg(self):
        """
        测试计算平均分方法
        """
        # 1.实例化学生信息管理类
        sm = StudentManager()
        # 2.实例化学生
        stu1 = Student("xcz", 80)
        stu2 = Student("wzl", 100)
        # 3.调用学生信息管理类中的添加学生方法
        sm.add(stu1)
        sm.add(stu2)
        # 4.调用计算平均分方法
        avg_score = sm.average_score()
        assert 90 == avg_score
