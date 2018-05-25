import loader as ld


def main():
    loader = ld.loader()
    crimeData = loader.loadCrime("communities.data.csv")
    irisData = loader.loadIris("Iris.csv")
    cancerData = loader.loadCancer("data.csv")


    print(len(crimeData))
    print(len(irisData))
    print(len(cancerData))

    irisColumn = irisData[0]
    print(irisData[1])

    for i in irisData[1:]:
        




if __name__ == '__main__':
    main()

