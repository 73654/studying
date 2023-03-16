import pytest

from script.caculator import Calculator


class TestCaculator:
    def teardown_class(self):
        print("结束测试")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize(
        "a, b, result",
        [
            [10, 20, 30],
            [5, 10, 15],
            [15, 20, 35],
            [15, 30, 45]
        ]
    )
    def test_add(self, a, b, result):
        self.count = Calculator()
        assert result == self.count.add(a, b)

    @pytest.mark.parametrize(
        "a, b, result",
        [
            [10, 20, 0.5],
            [5, 10, 0.5],
            [15, 20, 0.75],
            [15, 30, 0.5]
        ]
    )
    def test_div(self, a, b, result):
        self.count = Calculator()
        assert result == self.count.div(a, b)
