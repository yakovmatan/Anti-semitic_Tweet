from pandas import DataFrame
from src.Load_data import LoadData
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

     def average_tweet_length(self):
         self.df['tweet_length'] = self.df['Text'].apply(lambda x: len(str(x).split()))

         mean_length_tweet = self.df.groupby('Biased')['tweet_length'].mean()

         antisemitic = mean_length_tweet.loc[0]
         non_antisemitic = mean_length_tweet.loc[1]
         total = self.df['tweet_length'].mean()


         return {"antisemitic": float(antisemitic),
                 "non_antisemitic": float(non_antisemitic),
                 "total": float(total)
                }


if __name__ == '__main__':
    l = LoadData('../Data/tweets_dataset.csv')
    m = l.load()

    d = DataAnalyzer(m)
    j = d.average_tweet_length()
    print(j)