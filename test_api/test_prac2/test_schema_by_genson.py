from genson import SchemaBuilder


def test_schema_by_genson():
    data = {
        "greeting": "Welcome to quicktype!",
        "instructions": [
            "Type or paste JSON here",
            "Or choose a sample above",
            "quicktype will generate code in your",
            "chosen language to parse the sample data"
        ]
    }
    # 实例化jsonschem
    builder = SchemaBuilder()
    # 传入被转换的对象
    builder.add_object(data)
    # 转换成 schema 数据
    result = builder.to_schema()
    print(result)