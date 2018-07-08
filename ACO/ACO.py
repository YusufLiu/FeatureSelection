import cancerModel as cm
import pandas
import random
import numpy as np
import math
import gc
import copy

class ACO:

    def __init__(self,data,maxIteration,antNumber,cc,Q,e):
        self.data = data
        self.fp = [cc]*len(data.columns)
        self.maxIteration = maxIteration
        self.ants = []
        self.size = len(data.columns)
        self.antNumber= antNumber
        self.Q = Q
        self.bestScore = 0
        self.result=[]
        self.evaporate = e



    def constructSolution(self,ant):
        featureSetIndex = []
        for j in range(self.size):
            decision = random.random()
            if (decision < self.fp[j] / 2):
                featureSetIndex.append(1)
            else:
                featureSetIndex.append(0)

        features = [0]
        for i, obj in enumerate(featureSetIndex):
            if obj:
                features.append(i + 1)
        newdata = self.data.iloc[:, features]
        score = float(cm.LogesticRegression(newdata))
        ant.val = score
        ant.subsets = featureSetIndex
        return ant

    def ApplyLocalSearch(self):
        maxScore = 0
        maxSet = []
        for a in self.ants:
            if(maxScore < a.score):
                maxScore = a.score
                maxSet = a.subsets

        if(self.bestScore < maxScore):
            self.bestScore = maxScore
            self.result = maxSet

        return maxSet

    def UpdatePheromones(self,best):
        for i,v in enumerate(best):
            self.fp[i] = self.fp[i]*self.evaporate
            if v == 1:
                self.fp[i] = self.fp[i] + self.Q


    def simulate(self):
        for s in range(self.maxIteration):
            for i in range(self.antNumber):
                ant = Ant()
                ant = self.constructSolution(ant)
                self.ants.append(ant)
            bestSet = self.ApplyLocalSearch()
            self.UpdatePheromones(bestSet)
            self.ants = []

        return [self.bestScore,self.result]


class Ant:
    def __init__(self):
        self.subsets = []
        self.val = 0








