from config.logger import Logger


class FileLogger(Logger):

    def __init__(self, file_name):
        self.fp = open(file_name, 'a')

    def write(self, msg):
        self.fp.write(msg + "\n")
