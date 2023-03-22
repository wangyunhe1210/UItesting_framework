import yaml


def write_yaml(file_name, datas):
    with open(file_name, 'w', encoding='utf8') as f:
        yaml.dump(datas, f)


def read_yaml(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        res = yaml.safe_load(f)
        return res
