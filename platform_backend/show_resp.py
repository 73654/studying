from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def parse_resp_tuple():
    return 'hello', 301


@app.route('/json', methods=['GET'])
def parse_resp_json():
    return jsonify({'name': 'hogwarts'})


@app.route('/get/html', methods=['GET'])
def parse_resp_html():
    name = request.args.get('name')
    return render_template('index.html', owner=name)


@app.route('/get/diy', methods=['GET'])
def parse_resp_diy():
    # headers = {'token':12313221313}
    name = request.args.get('name')
    resp = make_response(render_template('index.html', owner=name))
    resp.set_cookie('name', 'chenzheng')
    resp.headers["hogwarts"] = "wzl"
    resp.headers["token"] = 12313221313
    # resp.headers = headers
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
