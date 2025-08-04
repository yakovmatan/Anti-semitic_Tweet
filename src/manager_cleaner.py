from src.data_cleaner import DataCleaner


class ManagerCleaner:

    @staticmethod
    def clean_data(df):
        data = DataCleaner(df)
        return data.removing_punctuation_marks().convert_to_lowercase().removing_uncategorized_tweets().get_the_relevant_columns().df


    @staticmethod
    def save_to_csv(df):
        df.to_csv('../result/tweets_dataset_cleaned.csv', index=False)

