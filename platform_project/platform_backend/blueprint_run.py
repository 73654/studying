from flask import Flask
from  flask import CORS

from platform_project.platform_backend.bp_user import user
from platform_project.platform_backend.testcase_blueprint import testcase_bp

app = Flask(__name__)
CORS(app)

@app.route(rule='/')
def chatbot():
    print()
    return f"Hello world!"


# 注册蓝图
app.register_blueprint(testcase_bp)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
