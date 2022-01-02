from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import reader
import pandas as pd
from scraper import getTextFromArticle
data = requests.get('https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump').text
soup = BeautifulSoup(data, 'lxml')
titles = soup.findAll('a', class_='qa-heading-link lx-stream-post__header-link')
#links = []
for title in titles:
    link = "https://www.bbc.com"+title["href"]
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    print(getTextFromArticle(link))