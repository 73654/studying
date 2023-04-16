from typing import List
from other_project.script.student import Student


class StudentManager:
    def __init__(self):
        self.students:List[Student] = []

    def add(self,student:Student):
        '''添加学员'''
        self.students.append(student)

    def remove(self,name:str):
        ''' 移除学员 '''

        for student in self.students:
            if student.name == name:
                self.students.remove(student)

    def get_student_info(self,name:str):
        for stu in self.students:
            if stu.name == name:
                return stu

        raise Exception(f"Student <{name}> not found. ")

    def average_score(self)->float:
        sum = 0
        for s in self.students:
            sum += s.score
        stu_num = len(self.students)
        print(f"学生的总分数：{sum}, 学生总人数：{stu_num}")
        return sum/stu_num

    def show_students(self):
        for stu in self.students:
            print(f"显示学员相关信息：{stu}")

