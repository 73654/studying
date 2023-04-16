def pytest_collection_modifyitems(
    session, config, items
) -> None:
    """
    搜集全部用例
    :param session:
    :param config:
    :param items:所有用例的列表
    :return:
    """
    cases = []
    # 测试用例参数的编码格式改写
    for item in items:
        # items 就是一条用例对象
        # 修改每一条用例对象的 name 和 _nodeid 两个属性的编码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')