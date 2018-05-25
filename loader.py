import csv
import numpy as np
import pandas as pd


class loader(object):

    def __init__(self):
        pass


    def loadCrime(self,filename):
        result = []
        with open(filename, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                result.append((row[:127], row[127]))

        return result

    def loadIris(self,filename):
        result = []
        with open(filename, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                result.append((row[:5], row[5]))

        return result

    def loadCancer(self,filename):
        result = []
        with open(filename, 'rb') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                result.append((row[2:], row[1]))

        return result

    def pdLoadCancer(self,filename):
        result = []
        with open(filename, 'rb') as csvfile:
            datareader = pd.read_csv(csvfile)
            datareader.set_index('id')


        return datareader