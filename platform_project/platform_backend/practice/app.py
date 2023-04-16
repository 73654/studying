from flask import request, Blueprint, jsonify

from platform_project.platform_backend.practice.data import testcases

# 实例化蓝图对象
testcase_bp = Blueprint('testcase', __name__, url_prefix='/testcase')


@testcase_bp.route("/", methods=["get"])
def get_testcase():
    # 可查询所有的用例，以及单个用例
    # 获取请求信息
    req_data = request.args
    # 获取请求信息中id
    id = req_data.get("id")
    # 实例化数据库信息
    my_cases = testcases
    datas = []
    flag = False
    # 如果获取到id
    if id:
        # 遍历y_cases中数据到datas
        for case in my_cases:
            # 获取到的id与my_cases中一致
            if (int(id)) == case.get("id"):
                # 添加数据到cases
                datas.append(case)
                flag = True
        # 如果flag=False
        if not flag:
            # 返回查询失败信息
            return jsonify({"code": 40002, "msg": "case id is not exists"})
    # 如果请求不存在id,添加数据库信息到datas
    else:
        datas = my_cases
    # 返回查询成功信息
    return jsonify({"code": 200, "msg": "success", "data": datas})


@testcase_bp.route("/", methods=["post"])
def post_testcase():
    # 存在id，不添加并返回 {"code":40001, "msg":" case id is exists"}
    # 不存在id，添加并返回 {"code": 200, "msg": "success", "data": new_datas}
    # 获取body体中json信息
    case_data = request.json
    print(f"接收到的参数:{case_data}")
    print(f"case_data 类型:{type(case_data)}")
    # 接收到的测试用例信息
    id = int(case_data.get("id"))
    name = case_data.get("name")
    desc = case_data.get("desc")
    # 将接收到的数据对象，转成字典格式
    new_case = {"id": id, "name": name, "desc": desc}
    # 实例化数据库信息
    my_cases = testcases
    # 遍历my_cases中数据到new_case
    for case in my_cases:
        # 如果my_cases中存在参数中id,返回错误信息,id已存在
        if case.get("id") == id:
            return jsonify({"code": 40001, "msg": " case id is exists"})
    my_cases.append(new_case)
    # 如果my_cases中不存在参数中id,返回成功信息
    print(f"当前所有的用例: {my_cases}")
    # with open("./data.py", "w", encoding="utf-8") as f:
    #     json.dump(my_cases, f)
    return jsonify({"code": 200, "msg": "success", "data": my_cases})
