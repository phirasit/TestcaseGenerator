# list of variable types
from config.variable.int import Int, Int8, Int16, Int64
from config.variable.array import Array
from config.variable.char import Char
from config.variable.string import String

from config.rng import RNG


def create_new_variable(var, var_info, variable_index):
    assert (type(var_info) == dict)
    assert ('type' in var_info)
    var_type = var_info['type']
    args = {
        'ref': var,
        'rng': RNG(), # TODO add a RNG class
        'variable_index': variable_index,
        'create_variable': create_new_variable,
    }

    if var_type == 'Int':
        return Int(args, var_info)
    elif var_type == 'Int8':
        return Int8(args, var_info)
    elif var_type == 'Int16':
        return Int16(args, var_info)
    elif var_type == 'Int64':
        return Int64(args, var_info)
    elif var_type == 'Array':
        return Array(args, var_info)
    elif var_type == 'Char':
        return Char(args, var_info)
    elif var_type == 'String':
        return String(args, var_info)

    raise Exception("type ({}) is not recognized".format(var_type))


