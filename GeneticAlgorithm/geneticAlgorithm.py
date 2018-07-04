import cancerModel as cm
import pandas
import random
import numpy as np
import math
import gc
import copy


class GeneticAlgorithm:

    def __init__(self, data, size=None, popSize=None, maxGeneration=None, pCrossOver=None, pMutate=None, limit=None, silent=True):
        self.data = data  # data to be analyzed with column 0 being the predictor column
        self.size = size  # the total number of features to be selected
        self.popSize = popSize  # the population size
        self.maxGeneration = maxGeneration # the maximum generation to run
        self.pCrossOver = pCrossOver  # crossover probability
        self.pMutate = pMutate  # mutation probability
        self.result = None
        self.limit = limit
        self.silent = silent
        self.rankMap = {}
        if not self.size:  # Default size: number of columns in the dataframe without the predictor column
            self.size = len(data.columns) - 1
        if not self.popSize:
            self.popSize = 1000
        if not self.pCrossOver:
            self.pc = 0.7
        if not self.pMutate:
            self.pm = (1/self.popSize + 1/self.size)/2
        if not self.limit:
            self.limit = self.size
        if not self.maxGeneration:
            self.maxGeneration = 100

    # randomly select k features out of n choices to be the starting features
    # return an array of selected features with 1 representing selected features 0 for non-selected
    def randomStart(self, n=None, k=None):
        if not n:
            n = self.size
        if not k:
            k = self.limit

        featureSet = np.zeros(n)
        featureSet[:k] = 1
        np.random.shuffle(featureSet)
        return featureSet

    # uniformly randomly return an integer 0 to k-1
    def randomFlip(self, k):
        ind = random.randint(0, k - 1)
        return ind

    # initialize a population array
    def popInit(self):
        population = [self.randomStart() for i in range(self.popSize)]

        # init rank map
        weight = 0
        for i in range(self.popSize):
            for j in range(i):
                self.rankMap[weight] = i
                weight += 1

        return population

    # rank based parent selection
    def parentSelectionRanked(self, population, data):
        popScore = []
        scoreList = []
        parentPool = []
        shortCancerData = data
        rankMap = self.rankMap
        popSize = self.popSize

        # get fitness score for each parent
        for featureSetIndex in population:
            # say if no feature selected, same as random prediction
            score = 0.5
            if sum(featureSetIndex) != 0:
                features = [0]
                for i, obj in enumerate(featureSetIndex):
                    if obj:
                        features.append(i + 1)
                newSCD = shortCancerData.iloc[:, features]
                score = float(cm.LogesticRegression(newSCD))
            popScore.append((score, featureSetIndex))
            scoreList.append(score)

        # rank the parent by score
        popScore.sort(key=lambda x: x[0])
        k = int((popSize - 1)*popSize/2)

        # populated the parent pool based on rank
        for i in range(popSize):
            roll = self.randomFlip(k)
            ind = rankMap.get(roll)
            parentPool.append(copy.deepcopy(popScore[ind][1]))

        random.shuffle(parentPool)
        averageFitness = np.mean(scoreList)
        mostFitMember = popScore[-1]
        return parentPool, averageFitness, mostFitMember

    # uniform crossover
    def crossOverUniform(self, population):
        pc = self.pCrossOver
        newPop = []
        while population:
            parent1 = population.pop()
            parent2 = population.pop()
            roll = random.random()

            # if no crossover, copy over parent
            if roll > pc:
                newPop.append(parent1)
                newPop.append(parent2)
                continue

            child1 = []
            child2 = []
            for i in range(parent1.size):
                flip = random.random()
                if flip > 0.5:
                    child1.append(parent1[i])
                    child2.append(parent2[i])
                else:
                    child1.append(parent2[i])
                    child2.append(parent1[i])

            newPop.append(child1)
            newPop.append(child2)

        return newPop

    # mutation
    def mutate(self, population):
        pm = self.pMutate
        newPop = []
        while population:
            parent = population.pop()
            child = [(gene+1) % 2 if random.random < pm else gene for gene in parent]
            newPop.append(child)

        return newPop

    # main generational GA model
    def startSearch(self):
        data = self.data
        size = self.size
        currentGeneration = 0
        maxGeneration = self.maxGeneration

        shortCancerData = data
        currentSolScore = 0
        currentSolSet = []
        bestSolScore = 0
        bestSolSet = []

        # set termination conditions
        maxCounter = math.pow(2, size)
        counter = 0

        print "Started Genetic Algorithm with data size: %d,  population size: %.2f and limit: %d ... " % (size, self.popSize, self.limit)
        population = self.popInit()
        while counter < maxCounter and currentGeneration < maxGeneration:
            parentPool, averageFitness, mostFitMember = self.parentSelectionRanked(population, shortCancerData)
            childPool = self.crossOverUniform(parentPool)
            population = self.mutate(childPool)

            currentSolScore = mostFitMember[0]
            currentSolSet = mostFitMember[1]

            if bestSolScore < currentSolScore:
                bestSolScore = currentSolScore
                bestSolSet = copy.deepcopy(currentSolSet)


            if not self.silent:
                print "Generation %d complete. Current Population Average Fitness %.6f" % (currentGeneration, averageFitness)
                shortFeaturesName = list(shortCancerData.columns.values)
                selectedFeaturesName = []
                for ind, obj in enumerate(currentSolSet):
                    if obj:
                        selectedFeaturesName.append(shortFeaturesName[ind + 1])
                print "Features Selected: ",
                print selectedFeaturesName

            gc.collect()
            counter += 1
            currentGeneration += 1

        shortFeaturesName = list(shortCancerData.columns.values)

        # this is the result of the GA algorithm (local optimum)
        selectedFeaturesName = []
        for ind, obj in enumerate(currentSolSet):
            if obj:
                selectedFeaturesName.append(shortFeaturesName[ind + 1])

        # this is the result of the tracking maximum (possible global optimum)
        bestFeatureName = []
        for ind, obj in enumerate(bestSolSet):
            if obj:
                bestFeatureName.append(shortFeaturesName[ind + 1])

        self.result = [("Current", selectedFeaturesName, currentSolScore), ("Best", bestFeatureName, bestSolScore)]
        return self.result
