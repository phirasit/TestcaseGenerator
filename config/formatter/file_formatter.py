def get_test_id(start, test_id):
    if type(start) is int:
        return str(start + test_id)
    else:
        return str(chr(ord(start[0]) + test_id))


class SingleFileFormatter:

    def __init__(self, data):
        if type(data) is not dict:
            raise Exception("the data has to be a dictionary")
        self.start = data['start'] if 'start' in data else 0
        if not (type(self.start) is int or (type(self.start) is str and len(self.start) == 1)):
            raise Exception("start symbol ({}) should be an integer or a 1-character string".format(self.start))

        self.info_folder = data['folder'] if 'folder' in data else None
        self.info_file = data['file'] if 'file' in data else '{}.in'

    def display(self, base_dir, test_id, is_folder):
        actual_test_id = get_test_id(self.start, test_id)
        description = self.info_folder if is_folder else self.info_file
        if is_folder and self.info_folder is None:
            raise Exception("no folder description")
        return base_dir + description.replace("{}", actual_test_id)


class FileFormatter:

    def __init__(self, data):
        if type(data) is not dict:
            raise Exception("the data has to be a dictionary")

        # in case of a default formatter
        if 'file' in data:
            self.default_file_formatter = SingleFileFormatter(data)
        else:
            self.default_file_formatter = None

        if 'level' in data:
            if type(data['level']) is not dict:
                raise Exception("the data in `level` has to be a dictionary")
            self.special = {key: SingleFileFormatter(value) for key, value in data['level'].items()}
        else:
            self.special = dict()

    def display(self, base_dir, test_id, level, is_folder):
        if level in self.special:
            return self.special[level].display(base_dir, test_id, is_folder)
        elif self.default_file_formatter is not None:
            # apply default formatter if no special formatter is available
            return self.default_file_formatter.display(base_dir, test_id, is_folder)
        else:
            raise Exception("No file formatter for level `{}`".format(level))

