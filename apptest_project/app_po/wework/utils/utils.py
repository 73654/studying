import time

import yaml


class Utils:
    @classmethod
    def get_yaml_data(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return (data)

    @classmethod
    def get_current_time(cls):
        return time.strftime("%Y-%m-%d %H-%M-%S")
