import os


# fill all the implicit data
def fill_config(config):

    assert(type(config) == dict) # filling config must be a dictionary

    if 'cache' not in config:
        config['cache'] = dict()

    if 'env' not in config:
        config['env'] = {}

    if 'variables' not in config:
        config['variables'] = dict()

    if 'constraints' not in config:
        config['constraints'] = dict()

    if 'generate' not in config:
        config['generate'] = list()

    if 'seed' not in config:
        config['seed'] = os.environ['SEED'] if 'SEED' in os.environ else 0

    if 'tests' not in config:
        config['tests'] = dict()

    if 'test_num' not in config:
        config['test_num'] = max(1, len(config['tests']))


# consistency test
def validate(data):
    assert(type(data) == dict) # validating data must be a dictionary

    # test_num is invalid
    if ('test_num' not in data) or (type(data['test_num']) != int) or (data['test_num'] == 0):
        return False

    return True

