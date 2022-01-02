from bs4 import BeautifulSoup
import requests


def getTextFromArticle(link:str):
    req = requests.get(link).text
    soup = BeautifulSoup(req, "lxml")
    article = soup.find("article", {"class":"ssrcss-1mc1y2-ArticleWrapper e1nh2i2l6"})
    textDivs = article.find_all("div", {"data-component":"text-block"})
    returnString = ""
    for textDiv in textDivs:
        childDiv = textDiv.find_all("p")
        for x in childDiv:
            returnString+= x.get_text()
        returnString += '\n'
    
    return returnString

