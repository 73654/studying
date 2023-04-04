import requests


def test_update_owner():
    '''
    修改宠物主人信息
    :return:
    '''
    # 获取宠物主人id
    query_url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    data = {'lastName':'hogwarts'}
    r = requests.get(query_url, params=data)
    my_owner = r.json()[0]['id']
    print(my_owner)
    # 修改主人信息
    modify_address = 'shanghai'
    url = f'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners/{my_owner}'
    payload = {"id":my_owner,"firstName":"wuhogwarts","lastName":"hogwarts","address":modify_address,"city":"shenzhen","telephone":"123456780"}
    r = requests.put(url, json=payload)
    assert r.status_code == 204
    assert requests.codes.no_content == r.status_code
    # 获取主人信息
    r = requests.get(query_url, params=data)
    owner_info = r.json()[0]
    address_after = owner_info['address']
    assert modify_address == address_after