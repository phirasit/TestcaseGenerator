from abc import abstractmethod, ABC


class Logger(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def write(self, msg):
        pass

