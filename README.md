# Analyzing Antisemitic Tweets on Twitter

The goal of this mini-project is to do basic analysis and cleaning on tweets classified as anti-Semitic or non-anti-Semitic, using Python and the Pandas library.

### Data Analysis
1. Count the number of tweets per category (anti-Semitic, non-anti-Semitic, unspecified)
2. Calculate the average tweet length (in words) by category and total
3. Calculate the 3 longest tweets (by word count) in each category
4. Find the 10 most common words in all tweets
5. Count the number of words written in capital letters by category and total

### 2. Data cleaning
1. Keep only relevant columns: `text`, `biased`
2. Remove punctuation
3. Convert all text to lowercase
4. Remove tweets with undefined classification 

### 3. Export Results
1. Export the analysis results to a JSON file named: `result/results.json`
2. Save the cleaned dataset to: `result/tweets_dataset_cleaned.csv`

To run, run the main.py script.
