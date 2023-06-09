import random


class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        print(f"我是{self.name},现在有{self.balance}块钱")


class Manager(Person):
    """群主类"""
    red_pockets = []

    def sendbag(self, money, num):
        if money > self.balance:
            print("我借贷给你们发?")
            return
        self.balance = self.balance - money
        avg = money // num
        mod = money % num
        for i in range(num):
            self.red_pockets.append(avg)
        self.red_pockets[-1] += mod
        # self.red_pockets.append(money)


class Member(Person):
    """成员类"""

    def grabbag(self, red_list):
        if len(red_list) == 0:
            print("手慢了,红包抢完了")
            return
        idx = random.randint(0, len(red_list) - 1)
        self.balance += red_list.pop(idx)
        print(f"{self.name}抢了一个红包!")



if __name__ == '__main__':
    manager = Manager("郗辰政", 1000)
    manager.show()
    manager.sendbag(999, 4)
    manager.show()
    zelin = Member(name="王泽林", balance=100)
    shijie = Member(name="耿世杰", balance=100)
    shirui = Member(name="王实瑞", balance=100)
    zelin.show()
    shijie.show()
    shirui.show()
    zelin.grabbag(manager.red_pockets)
    zelin.show()
    shijie.grabbag(manager.red_pockets)
    shijie.show()
    shirui.grabbag(manager.red_pockets)
    shirui.show()
