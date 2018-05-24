import loader as ld


def main():
    loader = ld.loader()
    data = loader.load("communities.data.csv")
    print(data[0])



if __name__ == '__main__':
    main()

