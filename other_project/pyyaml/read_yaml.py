import yaml

file_path = '../data/first_yaml.yaml'

with open(file_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
print(data, type(data))

