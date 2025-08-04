from src.Load_data import LoadData


class ManagerLoadData:

    @staticmethod
    def loading_csv_data():
        loader = LoadData('../Data/tweets_dataset.csv')
        df = loader.load()
        return df



