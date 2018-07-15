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
        self.fp = [cc]*(len(data.columns)-1)
        self.maxIteration = maxIteration
        self.ants = []
        self.size = len(data.columns)-1
        self.antNumber= antNumber
        self.Q = Q
        self.bestScore = 0
        self.result=[]
        self.evaporate = e



    def constructSolution(self,ant):
        featureSetIndex = []
        for j in range(self.size):
            decision = random.random()
            if decision < self.fp[j] / 2.0:
                featureSetIndex.append(1)
            else:
                featureSetIndex.append(0)
        features = [0]
        for i, obj in enumerate(featureSetIndex):
            if obj:
                features.append(i+1)
        newdata = self.data.iloc[:, features]
        if sum(featureSetIndex) == 0:
            score = 0.5
        else:
            score = float(cm.LogesticRegression(newdata))
        ant.val = score
        ant.subsets = copy.deepcopy(featureSetIndex)
        return ant

    def ApplyLocalSearch(self):
        maxScore = 0
        maxSet = []
        for a in self.ants:
            if maxScore < a.val or (maxScore == a.val and (maxSet and sum(a.subsets) < sum(maxSet))):
                maxScore = a.val
                maxSet = a.subsets

        if self.bestScore <= maxScore or (maxScore == self.bestScore and (self.result and sum(maxSet) < sum(self.result))):
            self.bestScore = maxScore
            self.result = maxSet

        print(maxScore)
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

        shortFeaturesName = list(self.data.columns.values)
        bestFeatureName = []
        for ind, obj in enumerate(self.result):
            if obj:
                bestFeatureName.append(shortFeaturesName[ind + 1])

        return ["Best", bestFeatureName, self.bestScore]


class Ant:
    def __init__(self):
        self.subsets = []
        self.val = 0








