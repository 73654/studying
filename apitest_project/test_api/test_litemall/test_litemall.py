import requests


class TestLiteMall:
    def setup_class(self):
        self.base_url = 'https://litemall.hogwarts.ceshiren.com'
        url = f'{self.base_url}/admin/auth/login'
        json = {
            'username': 'hogwarts',
            'password': 'test12345'
        }
        self.token = requests.post(url, json=json).json()["data"]["token"]
        print(self.token)

    def test_litemall_add(self):
        url = 'https://litemall.hogwarts.ceshiren.com/admin/goods/create'
        json = {
            "goods": {
                "picUrl": "",
                "gallery": [

                ],
                "isHot": 'true',
                "isNew": 'true',
                "isOnSale": 'true',
                "goodsSn": "3423567",
                "name": "郗辰政",
                "counterPrice": "8888"
            },
            "specifications": [
                {
                    "specification": "规格",
                    "value": "标准",
                    "picUrl": ""
                }
            ],
            "products": [
                {
                    "id": 0,
                    "specifications": [
                        "标准"
                    ],
                    "price": 0,
                    "number": 0,
                    "url": ""
                }
            ],
            "attributes": [
                {
                    "attribute": "材质",
                    "value": "纯棉"
                }
            ]
        }
        headers = {
            "x-litemall-admin-token": self.token
        }
        r = requests.post(url, json=json, headers=headers)
        print(r.json())
        assert r.status_code == 200

    def test_litemall_select(self):
        url = 'https://litemall.hogwarts.ceshiren.com/admin/goods/list'
        params = {
            'page': 1,
            'limit': 20,
            'sort': 'add_time',
            'order': 'desc',
            'goodsId': 1433777
        }
        headers = {
            "x-litemall-admin-token": self.token
        }
        r = requests.get(url, params=params, headers=headers)
        print(r.json())
        assert r.status_code == 200

    def test_litemall_delete(self):
        url = 'https://litemall.hogwarts.ceshiren.com/admin/goods/delete'
        json = {"id": 1433811}
        headers = {
            "x-litemall-admin-token": self.token
        }
        r = requests.post(url, json=json, headers=headers)
        print(r.json())
        assert r.status_code == 200
