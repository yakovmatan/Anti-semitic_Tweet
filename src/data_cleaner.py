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

     # Function that converts uppercase letters to lowercase
     def convert_to_lowercase(self):
         self.df['Text'] = self.df['Text'].astype(str).str.lower()
         return self

     #function to removing uncategorized tweets
     def removing_uncategorized_tweets(self):
         self.df = self.df[self.df['Biased'].isin([0, 1])]
         return self
