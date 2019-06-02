import yaml


def load_file(file_name):
    with open(file_name) as stream:
        # interpret as yaml
        data = yaml.safe_load(stream)
        return data


def parse_data(file_name):
    data = load_file(file_name)
    return data

