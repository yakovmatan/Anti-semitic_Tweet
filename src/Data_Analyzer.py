from pandas import DataFrame
import pandas as pd
from collections import Counter
import re

from src.Load_data import LoadData


class DataAnalyzer:

     def __init__(self,df: DataFrame):
         self.df = df

     # Function to count tweets per category
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

     # Function to find the average of words per category
     def average_tweet_length(self):
         self.df['tweet_length'] = self.df['Text'].apply(lambda x: len(str(x).split()))

         mean_length_tweet = self.df.groupby('Biased')['tweet_length'].mean()

         antisemitic = mean_length_tweet.loc[1]
         non_antisemitic = mean_length_tweet.loc[0]
         total = self.df['tweet_length'].mean()


         return {"antisemitic": float(antisemitic),
                 "non_antisemitic": float(non_antisemitic),
                 "total": float(total)
                }

     # Function to find the three longest tweets per category
     def the_longest_tweets(self):
         self.df['tweet_length_in_letters'] = self.df['Text'].apply(lambda x: len(str(x)))

         self.df.sort_values(by=['Biased','tweet_length_in_letters'], ascending=False, inplace=True)
         longest_tweets = self.df.groupby('Biased')['Text'].head(3)
         antisemitic = longest_tweets[:3]
         non_antisemitic = longest_tweets[3:]

         return {"antisemitic": antisemitic.tolist(),
                 "non_antisemitic": non_antisemitic.to_dict()}

     #function to find the 10 most common words in all tweets
     def ten_most_common_words(self):
         all_text = ' '.join(self.df['Text'].dropna().astype(str))
         cleaned_text = re.sub(r'[^\w\s]', '', all_text.lower())
         words = cleaned_text.split()
         word_counts = Counter(words)
         total = [word for word, _ in word_counts.most_common(10)]
         return {'total': total}







