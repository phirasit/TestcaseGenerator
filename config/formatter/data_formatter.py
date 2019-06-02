class VariableDisplay:

    def __init__(self, ref):
        self.ref = ref
        self.cache = None

    def get_ref(self):
        return self.ref

    def get_cache(self):
        return self.cache

    def set_cache(self, value):
        self.cache = value


def extract_line(line):
    idx = 0
    inside = False
    for i in range(len(line)):
        if (not inside) and (i == 0 or line[i-1] != '\\') and line[i] == '{':
            if idx < i:
                yield line[idx:i]
            idx = i
            inside = True
        if inside and line[i] == '}':
            yield VariableDisplay(line[idx+1:i])
            idx = i+1
            inside = False

    if idx+1 < len(line):
        yield line[idx+1:]


def extract_data(data):
    return list(map(lambda x: list(extract_line(x)), data))


class DataFormatter:

    def __init__(self, data_info):
        self.sep = data_info['sep']
        self.endl = data_info['endl'] if 'endl' in data_info else None
        self.data_info = extract_data(data_info['display'])
        self.var_list = {
            item.get_ref(): item
            for item_line in self.data_info
            for item in item_line
            if type(item) == VariableDisplay
        }

    def display(self, variable_index, logger):

        for var in self.var_list:
            if var not in variable_index:
                logger.write("Key `{}` is not in the variable index".format(var))
            else:
                data = variable_index[var]
                self.var_list[var].set_cache(data.display(data.get_value()))

        first = True
        for line in self.data_info:
            if not first:
                yield self.sep
            else:
                first = False

            for item in line:
                if type(item) == VariableDisplay:
                    yield item.get_cache()
                elif type(item) == str:
                    yield item
                else:
                    raise Exception("type of item ({}) is not recognized".format(type(item)))

        if self.endl is not None:
            yield self.endl
