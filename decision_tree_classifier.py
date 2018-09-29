import pandas as pd


def main():
    passenger = pd.read_csv("Datasets/train.csv")
    passenger.drop(['Ticket', 'Name'], axis=1)


if __name__ == "__main__":
    main()
