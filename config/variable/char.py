import string

from config.variable import Variable


class Char(Variable):

    def __init__(self, args, props):
        super().__init__(args, props)

    def get_random_choice(self):
        if 'choice' in self.props:
            return self.props['choice']
        elif 'range' not in self.props:
            return string.ascii_letters + string.digits
        elif self.props['range'] == 'lower':
            return string.ascii_lowercase
        elif self.props['range'] == 'upper':
            return string.ascii_uppercase
        elif self.props['range'] == 'number':
            return string.digits
        elif self.props['range'] == 'hex':
            return string.hexdigits
        else:
            return string.ascii_letters + string.digits

    def generate(self):
        return self.rng.choice(self.get_random_choice())

    def display(self, value):
        return str(value)
