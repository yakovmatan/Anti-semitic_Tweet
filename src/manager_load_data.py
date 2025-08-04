from src.Load_data import LoadData


class ManagerLoadData:

    @staticmethod
    def loading_csv_data(path='../Data/tweets_dataset.csv'):
        loader = LoadData(path)
        df = loader.load()
        return df



