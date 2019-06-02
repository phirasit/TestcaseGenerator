from config.logger import Logger
import sys


class SysLogger(Logger):

    def write(self, msg):
        sys.stderr.write(msg + "\n")
