import json
from src.Data_Analyzer import DataAnalyzer


class manager_analyzer:

    @staticmethod
    def data_analyzed(df):
        data_analyzer = {}
        analyzer = DataAnalyzer(df)
        data_analyzer["total_tweets"] = analyzer.tweets_per_category()
        data_analyzer["average_length"] = analyzer.average_tweet_length()
        data_analyzer["common_words"] = analyzer.ten_most_common_words()
        data_analyzer["longest_three_tweets"] = analyzer.the_longest_tweets()
        data_analyzer["uppercase_words"] = analyzer.uppercase_words()
        return data_analyzer


    @staticmethod
    def save_to_json(data, path='result/data_analysis.json'):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



