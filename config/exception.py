class ConfigException(Exception):

    def __init__(self, msg):
        super(ConfigException, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg


class GeneratorException(Exception):

    def __init__(self, msg):
        super(GeneratorException, self).__init__(msg)
        self.msg = msg

    def __str__(self):
        return self.msg

