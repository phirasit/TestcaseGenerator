from config.variable.char import Char


class String(Char):

    def __init__(self, args, props):
        super().__init__(args, props)
        self.var = Char(args, props)
        assert ('length' in props)

    def generate(self):
        self.var.props = self.props
        return [self.var.generate() for _ in range(self.extract_ref(self.props['length']))]

    def display(self, data):
        return ''.join(map(lambda x: self.var.display(x), data))
