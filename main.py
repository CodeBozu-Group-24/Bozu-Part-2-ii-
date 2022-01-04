from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import writer
import pandas as pd
from scraper import getTextFromArticle, getMeanScores
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

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
    writingFinal = getTextFromArticle(link).encode("ascii", "ignore").decode()
    writingFinal = re.sub("\n", " ", writingFinal)
    writings.append(writingFinal)

positivity = []    
for writing in writings:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(writing)
    positivity_score = sentiment_dict['pos']*100
    positivity.append(positivity_score)

with open('details.csv', 'w') as f:
    
    writer_object = writer(f)
    writer_object.writerow(["Title", "Content", "Score"])
    for i in range(len(title_text)):
        writer_object.writerow([title_text[i], writings[i], positivity[i]])
    f.close()   
 
print("Mean score: " + str(sum(positivity)/len(positivity)))
