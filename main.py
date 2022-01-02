from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import writer
import pandas as pd
from scraper import getTextFromArticle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = requests.get('https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump').text
soup = BeautifulSoup(data, 'lxml')
titles = soup.findAll('a', class_='qa-heading-link lx-stream-post__header-link')
title_text = []
for title in titles:
    title_text.append(title.get_text())
#links = []
writings = []
for title in titles:
    link = "https://www.bbc.com"+title["href"]
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    writings.append(getTextFromArticle(link))

positivity = []    
for writing in writings:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(writing)
    positivity_score = sentiment_dict['pos']
    positivity.append(positivity_score)


with open('details.csv', 'a') as f:
    writer_object = writer(f)
    details = []
    for i in range(len(titles)):
        details.append(title_text[i])
        details.append(writings[i])
        details.append(positivity[i])
    writer_object.writerow(details)
    f.close()    
