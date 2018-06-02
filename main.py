import loader as ld
import numpy as np
import math
import pandas
import gc
import cancerModel as cm
import GraphSearch.TreeGenerator as tg
import GraphSearch.featureTree as ft


def main():
    loader = ld.loader()
    # crimeData = loader.loadCrime("communities.data.csv")
    # irisData = loader.loadIris("Iris.csv")
    cancerData = loader.pdLoadCancer("data.csv")
    shortLength = 9
    T = math.ceil(math.sqrt(shortLength))
    shortCancerData = cancerData.ix[:100, :shortLength+2]

    shortTermMemory = np.zeros(shortLength)
    longTermMemory = 0
    bestSol = []
    featureSetIndex = np.zeros(shortLength)

    # set of features
    print

    ret = False
    maxCounter = math.pow(2, shortLength)
    counter = 0
    while not ret and counter < maxCounter:
        allResults = []
        print "currentFeatureSet"
        print featureSetIndex
        for ind, obj in enumerate(featureSetIndex):
            nFeatureSetIndex = featureSetIndex[:]
            nFeatureSetIndex[ind] = (obj != 1)
            features = [0, 1]
            for i, obj in enumerate(nFeatureSetIndex):
                if obj:
                    features.append(i+2)

            newSCD = shortCancerData.iloc[:,features]
            result = cm.LogesticRegression(newSCD)
            allResults.append((result, ind))

        allResults.sort(reverse=True)
        for index, var in enumerate(allResults):
            featureRes = var[0]
            featureIndex = var[1]
            if not shortTermMemory[featureIndex]:
                featureSetIndex[featureIndex] = (featureSetIndex[featureIndex] != 1)
                shortTermMemory[:] = [x - 1 if x != 0 else x for x in shortTermMemory]
                shortTermMemory[featureIndex] = T
                longTermMemory = featureRes if featureRes > longTermMemory else longTermMemory
                bestSol = featureSetIndex if featureRes > longTermMemory else featureSetIndex
                ret = False
                break
            elif featureRes > longTermMemory:
                featureSetIndex[featureIndex] = (featureSetIndex[featureIndex] != 1)
                shortTermMemory[:] = [x - 1 if x != 0 else x for x in shortTermMemory]
                shortTermMemory[featureIndex] = T
                bestSol = featureSetIndex
                ret = False
            elif index == (len(allResults) - 1):
                ret = True

        counter += 1

    print "best features"
    print bestSol
    print "last features"
    print featureSetIndex
    print "Accuracy long term "
    print longTermMemory








    # treeGenerator = tg.TreeGenerator()
    # for i in range(20):
    # cancerTree = treeGenerator.featureToTree(cancerData,0)
    # print("Tree finish, BFS Start")
    # featureSelect,score = cancerTree.bfs(cancerTree,cancerData)

    # print(featureSelect)
    # print(score)

    # print(cancerTree.getChildren())







    # result = cm.KNNeighbors(cancerData)
    # print("Using Knn with 5 neighbour, all features accuracy: "+str(result*100) + '%')
    # result = cm.LogesticRegression(cancerData)
    # print("Using Logestic Regression, all features accuracy: " + str(result * 100) + '%')








if __name__ == '__main__':
    main()

