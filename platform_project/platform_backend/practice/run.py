from flask import Flask
from flask_cors import CORS

from platform_project.platform_backend.practice.app import testcase_bp

app = Flask(__name__)
CORS(app)


# 注册蓝图
app.register_blueprint(testcase_bp)


if __name__ == '__main__':
    app.run(debug=True)
