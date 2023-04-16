from _pydecimal import Decimal
from utils.log_until import logger
from other_project.script import Calculator
import pytest
import yaml
import allure


def get_caculatoryaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return (data)


@allure.epic("计算器加减乘除系统")
@allure.feature("单元测试")
class TestCaculator:
    def teardown_class(self):
        print("结束测试")

    def setup(self):
        print("开始计算")
        self.count = Calculator()

    def teardown(self):
        print("结束计算")

    # 标题
    # 分类
    # 步骤
    # 描述
    # 优先级
    # 链接
    @allure.title("计算器相加的方法")
    @allure.story("相加类")
    @allure.description("计算器相加的冒烟用例")
    @pytest.mark.P0
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @pytest.mark.parametrize(
        "a, b, result", get_caculatoryaml("D:/project/data/caculator.yaml")["add"]
    )
    def test_add(self, a, b, result):
        with allure.step("调用计算器系统中的相加方法"):
            expect = self.count.add(Decimal(str(a)), Decimal(str(b)))
        with allure.step("断言相加结果是否正确"):
            assert result == float(expect)
            logger.info(f"两数相加结果为{expect}")
        # assert result == pytest.approx(self.count.add.pyyaml(a, b))

    @allure.title("计算器相减的方法")
    @allure.story("相减类")
    @allure.description("计算器相减的冒烟用例")
    @pytest.mark.P0
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @pytest.mark.parametrize(
        "a, b, result", get_caculatoryaml("D:/project/data/caculator.yaml")["sub"]
    )
    def test_sub(self, a, b, result):
        with allure.step("调用计算器系统中的相减方法"):
            expect = self.count.sub(Decimal(str(a)), Decimal(str(b)))
        with allure.step("断言相减结果是否正确"):
            assert result == float(expect)
            logger.info(f"两数相减结果为{expect}")

    @allure.title("计算器相乘的方法")
    @allure.story("相乘类")
    @allure.description("计算器相乘的冒烟用例")
    @pytest.mark.P0
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @pytest.mark.parametrize(
        "a, b, result", get_caculatoryaml("D:/project/data/caculator.yaml")["mul"]
    )
    def test_mul(self, a, b, result):
        with allure.step("调用计算器系统中的相乘方法"):
            expect = self.count.mul(Decimal(str(a)), Decimal(str(b)))
        with allure.step("断言相乘结果是否正确"):
            assert result == float(expect)
            logger.info(f"两数相乘结果为{expect}")

    @allure.title("计算器相除的方法")
    @allure.story("相除类")
    @allure.description("计算器相除的冒烟用例")
    @pytest.mark.P0
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @pytest.mark.parametrize(
        "a, b, result", get_caculatoryaml("D:/project/data/caculator.yaml")["div"]
    )
    def test_div(self, a, b, result):
        with allure.step("调用计算器系统中的相除方法"):
            expect = self.count.div(Decimal(str(a)), Decimal(str(b)))
        with allure.step("断言相除结果是否正确"):
            assert result == float(expect)
            logger.info(f"两数相除结果为{expect}")

    @allure.title("抛出类型错误的方法")
    @allure.story("抛出错误类")
    @allure.description("计算器错误的冒烟用例")
    @pytest.mark.P1
    @allure.link("https://www.baidu.com/")
    @allure.testcase("https://www.baidu.com/")
    @allure.issue("https://www.baidu.com/")
    @pytest.mark.parametrize(
        "a, b, result",
        get_caculatoryaml("D:/project/data/caculator.yaml")["error"]
        , ids=["first_chinese", "second_chinese"]
    )
    def test_add2(self, a, b, result):
        # try:
        #     assert result == self.count.add.pyyaml(a, b)
        #     # raise Exception()
        # except TypeError as e:
        #     print(e)
        # else:
        #     assert result == self.count.add.pyyaml(a, b)
        with allure.step("抛出错误结果给e"):
            with pytest.raises(eval(result)) as e:
                with allure.step("输出e"):
                    print(e)
                    logger.info(f"实际结果:{self.count.add(a, b)}")
