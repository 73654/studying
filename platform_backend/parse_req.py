from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def parse_req_args():
    print(f'args:{request.args.get("name")}')
    return 'hello'


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def parse_req_method():
    print(f'请求方法:{request.method}')
    return 'hello'


@app.route('/protocol', methods=['GET', 'POST'])
def parse_req_protocol():
    print(f'协议版本:{request.environ.get("SERVER_PROTOCOL")}')
    return 'hello'


@app.route('/url', methods=['GET'])
def parse_req_url():
    print(f'url:{request.url}')
    return 'hello'


@app.route('/headers', methods=['GET', 'POST'])
def parse_req_headers():
    print(f'headers:{request.headers}')
    return 'hello'


@app.route('/body', methods=['POST'])
def parse_req_body():
    print(f'请求体:{request.data}')
    return 'hello'


@app.route('/body/json', methods=['POST'])
def parse_req_body_json():
    req_data = request.json
    print(f'请求体json:{req_data},类型:{type(req_data)}')
    name = req_data.get('name')
    print(name)
    return 'hello'


@app.route('/body/form', methods=['POST'])
def parse_req_body_form():
    req_data = request.form
    print(f'请求体form:{req_data},类型:{type(req_data)}')
    name = req_data.get('name')
    print(name)
    return 'hello'


@app.route('/body/file', methods=['POST'])
def parse_req_body_file():
    req_data = request.files
    # 获取文件对象
    upload_file = req_data.get('rrr')
    # 获取文件名称
    file_name = upload_file.filename
    # 保存文件
    upload_file.save(f'upload_{file_name}')
    print(f'请求体文件名称:{file_name}')
    print(f'请求体files:{req_data},类型:{type(req_data)}')

    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
