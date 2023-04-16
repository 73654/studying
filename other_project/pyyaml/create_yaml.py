import yaml

# 写 pyyaml 文件
data = {
    "add": [
        [1, 2, 3],
        [4, 6, 10],
        ["文章", 3, "#$%@"]
    ]
}
with open("../data/first_yaml.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True)
