from abc import abstractmethod, ABC


# variable abstract class
class Variable(ABC):

    @abstractmethod
    def __init__(self, args, props):
        assert('ref' in args)
        self.ref = args['ref']
        self.rng = args['rng']
        self.variable_index = args['variable_index']
        self.create_variable = \
            lambda var_type, var_info: args['create_variable'](var_type, var_info, self.variable_index)
        self.props = props
        self.cache = list()

    def insert_cache(self, value):
        self.cache.append(value)

    def generate_cache(self):
        self.cache.append(self.generate())

    def remove_cache(self):
        assert(len(self.cache) > 0)
        self.cache.pop()

    def get_value(self):
        assert (len(self.cache) > 0)
        return self.cache[-1]

    @abstractmethod
    def generate(self):
        return None

    @abstractmethod
    def display(self, value):
        return str(value)

    def extract_ref(self, ref):
        if type(ref) is dict and 'ref' in ref:
            return self.variable_index[ref['ref']].get_value()
        return ref
