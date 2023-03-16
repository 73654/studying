def setup_module():
    print("测试开始")


def teardown_module():
    print("测试结束")


def setup_function():
    print("函数级别测试开始")


def teardown_function():
    print("函数级别测试结束")


def test_demo():
    print("测试方法 test_demo1")
    assert True


class TestSetup:
    def setup_class(self):
        print("类级别测试开始")

    def teardown_class(self):
        print("类级别测试结束")

    def setup(self):
        print("方法级别的 set up")

    def teardown(self):
        print("方法级别的 teardown")

    def test_demo1(self):
        print("测试方法 test_demo1")
        assert True

    def test_demo2(self):
        print("测试方法 test_demo2")
