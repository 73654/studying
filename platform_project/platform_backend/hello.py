from flask import Flask

app = Flask(__name__)


@app.route(rule='/')
def chatbot():
    print()
    return f"Hello world!"


if __name__ == '__main__':
    app.run()
