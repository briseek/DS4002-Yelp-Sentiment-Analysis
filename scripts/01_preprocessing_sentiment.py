#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:18:19 2025

@author: ashik
"""

import pandas as pd
import json

# importing the two json file

with open('yelp_academic_dataset_review.json') as f:
    review_data = [json.loads(line) for line in f]
    
reviews_df = pd.DataFrame(review_data)


with open('yelp_academic_dataset_business.json') as g:
    business_data = [json.loads(line) for line in g]
    

business_df = pd.DataFrame(business_data)

# filtering the business dataframe to only include PA
business_df['state'].value_counts() # based on this PA has the most
business_df['city'].value_counts() # Philadelpha is the most
business_philly = business_df[business_df["city"] == "Philadelphia"]

# Taking vector of business ids
business_ids = business_philly["business_id"]

# filtering reviews data set based on vector of business ids
reviews_philly = reviews_df[reviews_df["business_id"].isin(business_ids)]

# VADER analysis
#pip install nltk
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

scores = reviews_philly["text"].apply(analyzer.polarity_scores)
scores_df = pd.DataFrame(scores)
scores_df = pd.concat([scores_df.drop(['text'], axis=1), scores_df['text'].apply(pd.Series)], axis=1)

reviews = pd.concat([reviews_philly, scores_df], axis = 1, ignore_index = False)
review_groups = reviews.groupby(['business_id'])['compound'].mean()
review_groups2 = reviews.groupby(['business_id'])['pos'].mean()
review_groups3 = reviews.groupby(['business_id'])['neg'].mean()
review_groups4 = reviews.groupby(['business_id'])['neu'].mean()
review_groups5 = reviews.groupby(['business_id'])['useful'].sum()

final_df = business_philly
final_df = final_df.merge(review_groups, on="business_id", how='inner')
final_df = final_df.merge(review_groups2, on="business_id", how='inner')
final_df = final_df.merge(review_groups3, on="business_id", how='inner')
final_df = final_df.merge(review_groups4, on="business_id", how='inner')
final_df = final_df.merge(review_groups5, on="business_id", how='inner')

# save philly dataframes so it is easier to open later on
reviews.to_csv('Philadelphia_Reviews_FINAL.csv', index=False) 
business_philly.to_csv('Philadelphia_Business.csv', index=False)
final_df.to_csv("FINAL_yelp_dataframe.csv", index = False)

# plot the values of state

import matplotlib.pyplot as plt
business_df['state'].value_counts().plot(kind='bar', color = 'green')
plt.title("Distribution of Reviews by State")
plt.xlabel("State Abbreviations")
plt.ylabel("Counts")
plt.show()

# plot the values of top 20 cities
business_df['city'].value_counts().head(20).plot(kind='bar', color = 'pink')
plt.title("Distribution of Reviews for Top 20 Popular Citites")
plt.xlabel("City Names")
plt.ylabel("Counts")
plt.show()



