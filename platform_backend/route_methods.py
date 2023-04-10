from flask import Flask

app = Flask(__name__)


@app.route(rule='/')
def chatbot():
    return f"Hello world!"


@app.route(rule='/topic/<string:name>/', methods=['GET', 'POST'])
def select_case1(name):
    print(name)
    return f"Hello {name}!"


@app.route(rule='/topic/<string:name>/', methods=['POST'])
def post(name):
    print(name)
    return {"code": 0, "msg": "post success"}


@app.route(rule='/topic/put', methods=['PUT'])
def put():
    return ('put')


@app.route(rule='/topic/delete', methods=['DELETE'])
def delete():
    return {"code": 0, "msg": "delete success"}


if __name__ == '__main__':
    app.run()
