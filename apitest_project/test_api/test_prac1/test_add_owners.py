import requests


def test_add_owners():
    # 添加宠物主人url
    url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    # 要添加的宠物主人的相关信息
    data = {'id': None,
              'firstName': "jiejie",
              'lastName': "ci",
              'address': "北京",
              'city': "北京",
              'telephone': "1234578",
              }
    # 发送添加请求
    r = requests.request(method='post', url=url, json=data)
    # 断言响应码
    assert r.status_code == 201

    # 获取全部宠物主人url
    url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    # 发送获取请求
    all_owner = requests.get(url).json()
    # 获取全部宠物主人的信息
    all_owner_name = [owner['firstName'] for owner in all_owner]
    # 断言添加成功
    assert data['firstName'] in all_owner_name

    # 搜索宠物主人url
    url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    # 要获取的宠物主人名字
    perame = {'lastName': 'jiejie'}
    # 发送搜索请求
    r = requests.get(url=url, params=perame)
    # 获取宠物主人名字
    owner_lastName = r.json()[0]['lastName']
    # 断言搜索成功
    assert "jiejie" == owner_lastName
