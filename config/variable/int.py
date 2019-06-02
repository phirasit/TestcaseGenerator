from config.variable import Variable


class Int(Variable):

    def __init__(self, args, props):
        if 'min' not in props:
            props['min'] = 0
        if 'max' not in props:
            props['max'] = (1 << 32) - 1
        super().__init__(args, props)

    def generate(self):
        return self.rng.int(self.props['min'], self.props['max'])

    def display(self, value):
        return str(value)


class Int8(Int):

    def __init__(self, args, props):
        props['min'] = 0
        props['max'] = (1 << 8) - 1
        super().__init__(args, props)


class Int16(Int):

    def __init__(self, args, props):
        props['min'] = 0
        props['max'] = (1 << 16) - 1
        super().__init__(args, props)


class Int64(Int):

    def __init__(self, args, props):
        props['min'] = 0
        props['max'] = (1 << 64) - 1
        super().__init__(args, props)

