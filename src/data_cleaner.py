from pandas import DataFrame
import re

from src.Load_data import LoadData


class DataCleaner:

     def __init__(self,df: DataFrame):
         self.df = df


     # Function to remove punctuation marks
     def removing_punctuation_marks(self):
         self.df['Text'] = self.df['Text'].astype(str).apply(lambda x: re.sub(r'[^\w\s]', '', x))
         return self

     def convert_to_lowercase(self):
         self.df['Text'] = self.df['Text'].astype(str).str.lower()
         return self



if __name__ == '__main__':
    df = LoadData('../Data/tweets_dataset.csv')
    df = df.load()
    df = DataCleaner(df)
    df.removing_punctuation_marks()
    df.convert_to_lowercase()
    print(df.df['Text'])
