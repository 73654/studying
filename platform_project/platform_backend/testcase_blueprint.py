from flask import Blueprint, jsonify

# 实例化蓝图对象
testcase_bp = Blueprint('testcase', __name__, url_prefix='/testcase')


@testcase_bp.route('/add', methods=['POST'])
def add():
    return jsonify({'msg': 'add'})


@testcase_bp.route('/delete', methods=['DELETE', 'POST'])
def delete():
    return jsonify({'msg': 'delete'})


@testcase_bp.route('/update', methods=['POST'])
def update():
    return jsonify({'msg': 'update'})


@testcase_bp.route('/select', methods=['GET', 'POST'])
def select():
    return jsonify({'msg': 'select'})
