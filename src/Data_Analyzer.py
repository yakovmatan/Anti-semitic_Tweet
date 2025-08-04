from pandas import DataFrame
import pandas as pd

class DataAnalyzer:

     def __init__(self,df: DataFrame):
         self.df = df

     def tweets_per_category(self):
         tweets_per_category = self.df['Biased'].value_counts()

         antisemitic = tweets_per_category.loc[0]
         non_antisemitic = tweets_per_category.loc[1]
         total = tweets_per_category.sum()
         unspecified = total - non_antisemitic - antisemitic

         return {'antisemitic': int(antisemitic),
                 'non_antisemitic': int(non_antisemitic),
                 'total': int(total),
                 'unspecified': int(unspecified)
                 }

