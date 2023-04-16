from flask import Flask

app = Flask(__name__)


@app.route(rule='/xcz/topic/<string:name>/')
def select_case1(name):
    print(name)
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run()
