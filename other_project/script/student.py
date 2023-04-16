class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"学生的姓名：{self.name}, 分数：{self.score}"