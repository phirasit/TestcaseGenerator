from config.variable import Variable


class Array(Variable):

    def __init__(self, args, props):
        super().__init__(args, props)
        assert ('num' in props)
        assert ('sep' in props)
        self.var = self.create_variable(self.props['data']['type'], self.props['data'])

    def generate(self):
        assert('data' in self.props)
        assert('type' in self.props['data'])
        self.var = self.create_variable(self.props['data']['type'], self.props['data'])
        return [self.var.generate() for _ in range(self.extract_ref(self.props['num']))]

    def display(self, data):
        return self.props['sep'].join(map(lambda x: self.var.display(x), data))

