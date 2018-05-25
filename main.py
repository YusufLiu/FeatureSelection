import loader as ld
import irisLR
import cancerModel as cm


def main():
    loader = ld.loader()
    crimeData = loader.loadCrime("communities.data.csv")
    irisData = loader.loadIris("Iris.csv")
    cancerData = loader.pdLoadCancer("data.csv")


    print(len(crimeData))
    print(len(irisData))

    result = cm.KNNeighbors(cancerData)
    print("Using Knn with 5 neighbour, all features accuracy: "+str(result*100) + '%')
    result = cm.LogesticRegression(cancerData)
    print("Using Logestic Regression, all features accuracy: " + str(result * 100) + '%')








if __name__ == '__main__':
    main()

