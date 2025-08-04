from src.manager_analyzer import ManagerAnalyzer
from src.manager_cleaner import ManagerCleaner
from src.manager_load_data import ManagerLoadData


# Operation of the mangers
data = ManagerLoadData()
analyzer = ManagerAnalyzer()
cleaner = ManagerCleaner()

#data
df = data.loading_csv_data()
df2 = df.copy()

data_analyzed = analyzer.data_analyzed(df)
analyzer.save_to_json(data_analyzed)

clean_df = cleaner.clean_data(df2)
cleaner.save_to_csv(clean_df)



