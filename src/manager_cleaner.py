from src.Load_data import LoadData
from src.data_cleaner import DataCleaner


class ManagerCleaner:

    @staticmethod
    def clean_data(df):
        data = DataCleaner(df)
        return data.removing_punctuation_marks().convert_to_lowercase().removing_uncategorized_tweets().get_the_relevant_columns().df


