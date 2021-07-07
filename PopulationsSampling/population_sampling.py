from RandomGenerator import random_generator
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
import random

class PopulationSampling:

    def __init__(self):
        pass

    def choice(self, l, x, seed):
        random.seed(seed)
        return random.choices(l, k=x)

    def simple_random_sampling(self, l, x, y):
        # l = list
        # x = random numbers
        # y = seed
        rand = PopulationSampling()
        sample = rand.choice(self, l, x, y)
        return sample

    def confidence_interval(self, l):
        #95% confidence interval
        stats = Statistics()
        calculator = Calculator()
        standard_dev = stats.standard_deviation(l)
        x = len(l)
        m = stats.mean(l)
        margin_error = calculator.multiply(1.96, (calculator.divide(calculator.sqrt(x), standard_dev)))
        confidence_interval = [round(calculator.add(m, margin_error), 6), round(calculator.subtract(margin_error, m), 6)]
        return confidence_interval

    def margin_error(self, l):
        stats = Statistics()
        calculator = Calculator()
        standard_dev = stats.standard_deviation(l)
        x = len(l)
        margin_of_error = calculator.multiply(1.96, calculator.sqrt(calculator.divide(calculator.square(standard_dev), x)))
        return margin_of_error

