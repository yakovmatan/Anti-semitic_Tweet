from pandas import DataFrame
import re

from src.Load_data import LoadData


class DataCleaner:

     def __init__(self,df: DataFrame):
         self.df = df


     # Function to remove punctuation marks
     def removing_punctuation_marks(self):
         self.df['Text'] = self.df['Text'].astype(str).apply(lambda x: re.sub(r'[^\w\s]', '', x))


