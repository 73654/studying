import pytest


class TestParams:

    @pytest.mark.parametrize(
        "name",
        ["python", "selenium"]
    )
    def test_search(self, name):
        search_list = ["python", "java", "selenium"]
        assert name in search_list

    def test_search1(self):
        name2 = "javaee"
        self.search_list = ["python", "java", "selenium"]
        self.search_list.append(name2)
        assert name2 in self.search_list

    @pytest.mark.parametrize(
        "name, age, sex",
        [
            ["wangzelin", 20, "男"],
            ["gengshijie", 18, "女"],
            ["wangshirui", 28, "男"]
        ], ids=["xiaolin", "xiaogeng", "xiaowang"]
    )
    def test_mark_more(self, name, age, sex):
        print(f"name is {name}, age is {age}, sex is {sex}")
        assert True

    @pytest.mark.parametrize(
        "name",
        ["xiaowang", "xiaoli"]
    )
    @pytest.mark.parametrize(
        "hobby",
        ["run", "play", "sing"]
    )
    def test_mark_more(self, name, hobby):
        print(f"name is {name}, hobby is {hobby}")
        assert True
