import requests


def test_pet():
    # 添加宠物主人url
    url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    # 要添加的宠物主人的相关信息
    data = {'id': None,
            'firstName': "mingzi",
            'lastName': "xing",
            'address': "beijing",
            'city': "beijing",
            'telephone': "1234578",
            }
    # 发送添加请求
    r = requests.request(method='post', url=url, json=data)
    # 获取宠物主人id
    query_url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    data = {'lastName': 'xing'}
    r = requests.get(query_url, params=data)
    id = r.json()[0]['id']
    print(id)
    # 添加宠物url
    pet_url = f'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners/{id}/pets'
    data = {
        'id': None,
        "name": "wangwang",
        "birthDate": "2023-04-04",
        "type": {"name": "dog", "id": 3},
        "ownerId": id,
    }
    r = requests.post(url=pet_url, json=data)
    assert requests.codes.created == r.status_code
    # 获取宠物id
    query_url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    data = {'lastName': 'xing'}
    r = requests.get(query_url, params=data)
    pet_id = r.json()[0]['pets'][0]['id']
    # 修改宠物url
    update_url = f'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/pets/{pet_id}'
    update_data = {"id": pet_id,
                   "name": "wang",
                   "birthDate": "2023-04-04",
                   "pettype": {"name": "dog", "id": 3},
                   "type": {"name": "dog", "id": 3}
                   }
    r = requests.put(url=update_url, json=update_data)
    assert requests.codes.no_content == r.status_code
    # 修改宠物宠物类型
    update_type_data = {
        "id": pet_id,
        "name": "wang",
        "birthDate": "2023-04-04",
        "pettype": {"name": "cat", "id": 1},
        "type": {"name": "cat", "id": 1}
    }
    r = requests.put(url=update_url, json=update_type_data)
    assert requests.codes.no_content == r.status_code
    # 删除宠物
    r = requests.delete(url=update_url)
    assert requests.codes.no_content == r.status_code
