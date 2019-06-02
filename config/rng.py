import random


class RNG:

    def __init__(self):
        self.random = random
        self.start_state = self.random.getstate()
        self.set_seed(0)
        self.reset_state = self.random.getstate()

    def set_seed(self, seed):
        self.random.setstate(self.start_state)
        self.random.seed(seed)
        self.reset_state = self.random.getstate()

    def int(self, range_min, range_max):
        return self.random.randrange(range_min, range_max)

    def choice(self, choice):
        return self.random.choice(choice)

    def reset(self):
        self.random.setstate(self.reset_state)