import loader as ld
import pandas
import gc
import math
import cancerModel as cm
import GraphSearch.TreeGenerator as tg
import GraphSearch.featureTree as ft
import TabuSearch.tabuSearch as tbs


def main():
    loader = ld.loader()
    # crimeData = loader.loadCrime("communities.data.csv")
    # irisData = loader.loadIris("Iris.csv")
    cancerData = loader.pdLoadCancer("data.csv")

    shortLength = 20
    T = math.ceil(math.sqrt(shortLength))
    shortCancerData = cancerData.ix[:, 1:]
    tbsModel = tbs.TabuSearch(shortCancerData, t=7, limit=7, silent=False)
    tbsModel.startSearch()
    print tbsModel.result









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

