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
        sm = StudentManager()
        stu1 = Student("xcz", 80)
        stu2 = Student("wzl", 10)
        sm.add(stu1)
        sm.add(stu2)
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
        sm = StudentManager()
        stu = Student("xcz", 80)
        sm.add(stu)
        print(sm.get_student_info(stu.name))
        assert "学生的姓名：xcz, 分数：80" == str(sm.get_student_info(stu.name))

    def test_avg(self):
        sm = StudentManager()
        stu1 = Student("xcz", 80)
        stu2 = Student("wzl", 100)
        sm.add(stu1)
        sm.add(stu2)
        assert 90 == sm.average_score()
