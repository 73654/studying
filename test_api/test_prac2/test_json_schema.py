import requests
from jsonschema.validators import validate


def test_json_schema():
    # 被测对象
    url = 'https://spring-petclinic-rest.poc.ceshiren.com/petclinic/api/owners'
    params = {'lastName': 'hogwarts'}
    proxies = {
        'http': '127.0.0.1:8888',
        'https': '127.0.0.1:8888',
    }
    resp = requests.get(url, params=params, proxies=proxies, verify=False).json()

    # schema文档（尺子）
    schema_doc = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "type": "array",
        "items": {
            "$ref": "#/definitions/WelcomeElement"
        },
        "definitions": {
            "WelcomeElement": {
                "type": "object",
                "additionalProperties": True,
                "properties": {
                    "firstName": {
                        "type": "string"
                    },
                    "lastName": {
                        "type": "string"
                    },
                    "address": {
                        "type": "string"
                    },
                    "city": {
                        "type": "string"
                    },
                    "telephone": {
                        "type": "string",
                        "format": "integer"
                    },
                    "id": {
                        "type": "integer"
                    },
                    "pets": {
                        "type": "array",
                        "items": {}
                    }
                },
                "required": [
                    "address",
                    "city",
                    "firstName",
                    "id",
                    "lastName",
                    "pets",
                    "telephone"
                ],
                "title": "WelcomeElement"
            }
        }
    }

    # 校验
    validate(instance=resp, schema=schema_doc)