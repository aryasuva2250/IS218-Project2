import random

class RandomGenerator:

    def __init__(self):
        pass

    def random_num(self, x, y):
        return random.randrange(x, y)

    def random_seed(self, x, y, seed):
        random.seed(seed)
        return random.randrange(x, y)

    def random_list(self, x, y, n, seed):
        random.seed(seed)
        list_of_random_numbers = []
        for r in range(n):
            list_of_random_numbers.append(random.randrange(x, y))
        return list_of_random_numbers

