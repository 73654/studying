from flask import Flask

app = Flask(__name__)


@app.route(rule='/<string:name>/')
def chatbot(name):
    return f"{name},我爱你!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)