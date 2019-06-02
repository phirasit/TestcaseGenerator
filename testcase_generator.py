import os
import sys
import config.generator
import config.utility.file

from config.logger.sys_logger import SysLogger
from config.logger.file_logger import FileLogger


# TODO update error message
def generate(conf_file, base_dir, logger):

    try:
        test_config = config.Config.load_data(conf_file)
    except config.ConfigException as err:
        logger.write("Cannot load configuration file")
        logger.write(str(err))
        return False

    base_dir = os.path.join(base_dir, test_config.get_name()) + '/'
    config.utility.file.create_folder(base_dir)

    try:
        logger.write("Start generating sample cases")
        config.generator.generate(test_config, base_dir, dict(), 0, logger)
    except config.GeneratorException as err:
        logger.write("Cannot generate sample cases")
        logger.write(str(err))
        return False

    logger.write("Finish generating sample cases")
    return True


def extract_argv(argv):
    assert (len(argv) >= 2)
    input_file = None
    base_dir = os.path.dirname(__file__)
    logger = SysLogger()
    i = 1
    while i < len(argv):
        if argv[i] in ['-o', '-O', '--output']:
            base_dir = argv[i+1]
            i += 1
        elif argv[i] in ['-l', '--log']:
            logger = FileLogger(argv[i+1])
            i += 1
        else:
            input_file = argv[i]
        i += 1

    if input_file is None:
        logger.write("no input file")
        raise Exception("no input file")

    return input_file, base_dir, logger


def run():
    config_file, base_dir, logger = extract_argv(sys.argv)
    generate(config_file, base_dir, logger)


if __name__ == '__main__':
    run()
