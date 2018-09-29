def load_data(filename="Datasets/train.csv"):
    f = open(filename)
    lines = f.readlines()
    f.close()
    passengers = []
    for i, line in enumerate(lines):
        if i != 0:
            passengers.append(line.split(","))
    return passengers


def main():
    passengers = load_data()
    print("test")


if __name__ == "__main__":
    main()
