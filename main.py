import loader as ld
import cancerModel as cm
import GraphSearch.TreeGenerator as tg
import GraphSearch.featureTree as ft


def main():
    loader = ld.loader()
    crimeData = loader.loadCrime("communities.data.csv")
    irisData = loader.loadIris("Iris.csv")
    cancerData = loader.pdLoadCancer("data.csv")

    treeGenerator = tg.TreeGenerator()

    cancerTree = treeGenerator.featureToTree(cancerData)
    featureSelect,score = cancerTree.bfs(cancerTree,cancerData)
    print(featureSelect)
    print(score)


    print(cancerTree.getChildren())







    # result = cm.KNNeighbors(cancerData)
    # print("Using Knn with 5 neighbour, all features accuracy: "+str(result*100) + '%')
    # result = cm.LogesticRegression(cancerData)
    # print("Using Logestic Regression, all features accuracy: " + str(result * 100) + '%')








if __name__ == '__main__':
    main()

