# 创建用户模块 user.py
from flask import Blueprint, request

user = Blueprint('user', __name__, url_prefix='/user')


@user.route("/auth", methods=["post"])
def auth():
    print(request.json)
    return {"code": 200, "msg": "login succes@s"}


@user.route("/regist", methods=["post"])
def regist():
    return {"code": 200, "msg": "regist success"}
