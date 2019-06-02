from config.exception import *

import config.parser
import config.validator
import config.formatter


class Config:

    def __init__(self, data, parent=None):
        self.data = data

        # init some data
        if parent is not None:
            self.file_formatter = parent.file_formatter
            self.data_formatter = parent.data_formatter

        if 'file_format' in self.data:
            self.file_formatter = config.formatter.FileFormatter(self.data['file_format'])
        if 'data_format' in self.data:
            self.data_formatter = config.formatter.DataFormatter(self.data['data_format'])

    @staticmethod
    def load_data(file):
        try:
            return Config(config.parser.parse_data(file))
        except Exception as err:
            raise ConfigException(str(err))

    # list of getters
    def get_name(self):
        return self.data['name']

    def get_test_num(self):
        return self.data['test_num']

    def get_tests(self):
        return self.data['tests']

    def get_variables(self):
        return self.data['variables']

    def get_file_formatter(self):
        return self.file_formatter

    def get_data_formatter(self):
        return self.data_formatter

    def get_generate(self):
        return self.data['generate']

    def auto_fill(self):
        config.validator.fill_config(self.data)

    def validate(self):
        return config.validator.validate(self.data)


