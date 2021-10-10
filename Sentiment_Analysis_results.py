#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:34:56 2021

@author: luc
"""

import csv
import pandas as pd

#Creation of the function to exctract the number of positive, negative and neutral reviews 
#from the CSV files extracted for each company
def Sentiment_Analysis_Review(Company_name, CSV_path):
    df_CSV = pd.read_csv (CSV_path)

    df = pd.DataFrame(df_CSV)
    df.columns = ["Review", "Polarity", "Sentiment"]
    #print (df)


    positive_review = df[df.Sentiment == 'positive'].count()
    negative_review = df[df.Sentiment == 'negative'].count()
    neutral_review = df[df.Sentiment == 'neutral'].count()
#print("Number of positive reviews", positive_review)
#print("Number of negative reviews", negative_review)
#print("Number of neutral reviews", neutral_review)
    #it return the name of the company and the numbers of reviews for each type
    Company_Analysis = [Company_name, positive_review[1], neutral_review[1], negative_review[1]]
    return(Company_Analysis)


#List of CSV file to be read
Company_list = pd.read_csv('/Users/luc/Downloads/Company_list.csv', sep = ';',header = None)

Company_dataframe = pd.DataFrame(Company_list)


    
#print(Company_dataframe)

#We use the previous function on each csv of the list
Analysis_results = []

for i in range(len(Company_dataframe.index)):
    Company_results = Sentiment_Analysis_Review(Company_dataframe.iloc[i,0], Company_dataframe.iloc[i,1])
    Analysis_results.append(Company_results)
    
print(Analysis_results)

Analysis_dataframe = pd.DataFrame(Analysis_results, columns = ['Company', 'Positive reviews', 'Neutral reviews', 'Negative reviews'])
    
Analysis_dataframe.to_csv('Business_Analytics_Results.csv')
#We use this CSV for the illustrative graphs and to analyse the results 



    
