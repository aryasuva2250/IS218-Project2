from Calculator.Calculator import Calculator
from CsvReader import CsvReader
from Statistics.Median import median
from Statistics.Mean import mean


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result
