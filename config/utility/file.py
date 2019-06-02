import shutil
import os
import sys


def write_file(file_name, content_gen, logger):
    try:
        with open(file_name, 'w') as fp:
            for data in content_gen:
                fp.write(data)
    except OSError:
        logger.write("Cannot write file: {}".format(file_name))
        return False
    return True


def read_file(file_name, logger):
    try:
        with open(file_name, 'r') as fp:
            return fp.read()
    except OSError:
        logger.write("Cannot read file: {}".format(file_name))
        return None


def copy_file(source, dest, logger):
    try:
        shutil.copy2(source, dest)
    except OSError:
        logger.write("Cannot copy file: {} to {}".format(source, dest))
        return False
    return True


def create_folder(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        sys.stderr.write("Cannot create folder: {}".format(directory))
        return False
    return True
