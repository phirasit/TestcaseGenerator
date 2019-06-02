from config import Config
import config.utility as utility
import config.variable.generator as variable_generator
import config.exception as exception


def generate_test_case(config, variable_index, file_name, logger):
    # generate a test case

    # generate the remaining information
    tmp_var = list()
    for var in variable_index:
        if len(variable_index[var].cache) == 0:
            variable_index[var].generate_cache()
            tmp_var.append(var)

    # generate output from the current formatter
    output_data = config.get_data_formatter().display(variable_index, logger)

    # write all the data down
    if not utility.write_file(file_name, output_data, logger):
        logger.write("Skipping {}".format(file_name))
    else:
        logger.write("Finish generating {}".format(file_name))

    # clear the cache
    for var in tmp_var:
        variable_index[var].remove_cache()
    del tmp_var


def update_variable(var_dict, variable_index):

    # create unknown variables
    new_var = list()
    for var in var_dict:
        var_info = var_dict[var]
        if var not in variable_index:
            variable_index[var] = variable_generator.create_new_variable(var, var_info, variable_index)
            new_var.append(var)

    # update variable_index
    restore_dict = dict()
    for var in var_dict:
        restore_dict[var] = utility.map_update(variable_index[var].props, var_dict[var], [])

    # update static value
    static_var_list = list()
    for var in var_dict:
        var_info = var_dict[var]
        if var not in variable_index:
            raise exception.GeneratorException("No `{}` in variable_index".format(var))
        if 'value' in var_info:
            static_var_list.append(var)
            variable_index[var].insert_cache(var_info['value'])

    return new_var, restore_dict, static_var_list


def restore_updated_variables(var_dict, variable_index, update_info):

    new_var, restore_dict, static_var_list = update_info

    # remove static cache
    for var in static_var_list:
        variable_index[var].remove_cache()

    # revert variable_index back
    for var in var_dict:
        utility.map_restore(variable_index[var].props, restore_dict[var])

    # remove all unused variables
    for var in new_var:
        del variable_index[var]


def generate(config, base_dir, variable_index, level, logger):

    # variable list
    var_dict = config.get_variables()

    # auto fill the information
    config.auto_fill()

    # validate the information
    if not config.validate():
        # TODO make the error more readable
        raise exception.GeneratorException("Input config is not valid")

    # update variables
    update_info = update_variable(var_dict, variable_index)

    # build variable cache
    for var in config.get_generate():
        variable_index[var].generate_cache()

    # generate all the data
    for test_id in range(config.get_test_num()):

        file_name = config.get_file_formatter().display(base_dir, test_id, level, is_folder=False)

        if test_id in config.get_tests():

            test_info = config.get_tests()[test_id]
            if 'display' in test_info:
                # write static string to the file
                if not utility.write_file(file_name, test_info['display'], logger):
                    logger.write("Skipping {}".format(file_name))
            elif 'file' in test_info:
                # use a file as the test case
                if not utility.copy_file(test_info['file'], file_name, logger):
                    logger.write("Skipping {}".format(file_name))
            elif ('test_num' not in test_info) and 'variables' in test_info:
                # update some variables
                new_config = Config(test_info, config)
                new_var_dict = new_config.get_variables()
                tmp_update_info = update_variable(new_var_dict, variable_index)
                generate_test_case(config, variable_index, file_name, logger)
                restore_updated_variables(new_var_dict, variable_index, tmp_update_info)
                del tmp_update_info
            else:
                # create a directory
                try:
                    folder_name = config.get_file_formatter().display(base_dir, test_id, level, is_folder=True)
                    logger.write("Create a folder {}".format(folder_name))
                    if utility.create_folder(folder_name):
                        # generate sub task
                        generate(Config(test_info, config), folder_name, variable_index, level+1, logger)
                    else:
                        raise Exception()
                except Exception as err:
                    logger.write("Skipping {} subtask {} {}: ".format(base_dir, test_id, str(err)))


        else:
            # generate a test file
            generate_test_case(config, variable_index, file_name, logger)

    # clear the cache
    for var in config.get_generate():
        variable_index[var].remove_cache()

    # restore variables
    restore_updated_variables(var_dict, variable_index, update_info)
    del update_info



