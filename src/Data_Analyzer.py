from pandas import DataFrame
import pandas as pd

class DataAnalyzer:

     def __init__(self,df: DataFrame):
         self.df = df

     def tweets_per_category(self):
         tweets_per_category = self.df['Biased'].value_counts()

         antisemitic = tweets_per_category.loc[1]
         non_antisemitic = tweets_per_category.loc[0]
         total = tweets_per_category.sum()
         unspecified = total - non_antisemitic - antisemitic

         return {'antisemitic': int(antisemitic),
                 'non_antisemitic': int(non_antisemitic),
                 'total': int(total),
                 'unspecified': int(unspecified)
                 }

     def average_tweet_length(self):
         if 'tweet_length' not in self.df.columns:
             self.df['tweet_length'] = self.df['Text'].apply(lambda x: len(str(x).split()))

         mean_length_tweet = self.df.groupby('Biased')['tweet_length'].mean()

         antisemitic = mean_length_tweet.loc[1]
         non_antisemitic = mean_length_tweet.loc[0]
         total = self.df['tweet_length'].mean()


         return {"antisemitic": float(antisemitic),
                 "non_antisemitic": float(non_antisemitic),
                 "total": float(total)
                }

     def the_longest_tweets(self):
         if 'tweet_length' not in self.df.columns:
             self.df['tweet_length'] = self.df['Text'].apply(lambda x: len(str(x).split()))

         self.df.sort_values(by=['Biased','tweet_length'], ascending=False, inplace=True)
         longest_tweets = self.df.groupby('Biased')['Text'].head(3)
         antisemitic = longest_tweets[:3]
         non_antisemitic = longest_tweets[3:]
         return {"antisemitic": antisemitic,
                 "non_antisemitic": non_antisemitic}


