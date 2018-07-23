import loader as ld
import pandas
import gc
import math
import cancerModel as cm
import GraphSearch.TreeGenerator as tg
import GraphSearch.featureTree as ft
import SimulatedAnnealing.simAnnealing as sa

import GeneticAlgorithm.geneticAlgorithm as ga

import ACO.ACO as aco
import SaWAco.saWAco as sawaco



def main():
    loader = ld.loader()
    # crimeData = loader.loadCrime("communities.data.csv")
    # irisData = loader.loadIris("Iris.csv")
    cancerData = loader.pdLoadCancer("data.csv")

    # shortLength = 20
    # T = math.ceil(math.sqrt(shortLength))
    shortCancerData = cancerData.ix[:, 1:]

    # gaModel = ga.GeneticAlgorithm(shortCancerData, popSize=200, maxGeneration=100, limit=5, silent=False)
    # gaModel.startSearch()
    # print gaModel.result

    # saModel = sa.SimAnnealing(shortCancerData, limit=7, silent=False)
    # saModel.startSearch()
    # print saModel.result

    sawacoModel = sawaco.SaWAco(shortCancerData, limit=7, silent=False)
    sawacoModel.startSearch()
    print sawacoModel.result

    # acoModel = aco.ACO(shortCancerData,maxIteration=100,antNumber=100,cc=1,Q=0.1,e=0.95)
    # result = acoModel.simulate()
    # print(result)










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

