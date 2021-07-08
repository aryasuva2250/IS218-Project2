from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.Median import median
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.Standard_Deviation import standard_deviation

class Statistics():
    #data = []

    def __init__(self):
        #self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result