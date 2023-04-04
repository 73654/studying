import requests


def test_req_json():
    url = 'https://httpbin.ceshiren.com/post'
    resume = {
        'name': '辰政',
        'gender': 'man',
        'age': '29',
        'email': '3423567@qq.com'
    }
    data = {
        'name': 'xiaoming',
        'gender': 'man',
        'age': '20',
        'mail': '24786812512@qq.com',
        'address': {
            'province': '北京市',
            'shi': '北京市',
            'qu': '昌平区'
        },
        'skills': {
            'python': '熟练',
            'pytest': '熟练',
            'allure': '熟练',
            'selenium': '熟练',
            'appium': '熟练'
        }
    }

    r = requests.post(url, json=data)
    assert "北京市" == r.json()["json"].get("address").get("shi")
    assert "昌平区" == r.json()["json"].get("address").get("qu")
    assert "熟练" == r.json()["json"].get("skills").get("pytest")
    assert "熟练" == r.json()["json"].get("skills").get("selenium")
    assert "熟练" == r.json()["json"].get("skills").get("appium")
