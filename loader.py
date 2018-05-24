import csv
import numpy as np


class loader(object):

    def __init__(self):
        pass


    def load(self,filename):
        result = []
        with open(filename, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                result.append((row[:127], row[127]))

        return result

