'''Scraping Presidential debate transcripts using BeautifulSoup
Let's get all the transcript data so that we can see what topics
are being talked about by the candidates'''

#First brings out the heavy machinary
import requests
from bs4 import BeautifulSoup
import re
import nltk
from wordcloud import WordCloud
import json
import datetime


#Grab the first webpage that contains links to the transcripts
webpage = requests.get('http://www.presidency.ucsb.edu/debates.php')
#Soupify the request
soup = BeautifulSoup(webpage.text, 'html.parser')

#First let's gather all the urls of the 2016 debates to go through
#My list of links to scrape text from

urls = [a.get('href') for a in soup.find_all(href=re.compile('pid='))]


def helpMe(func):
	''' This is the DocString it can be found at helpMe.__doc__h\n'''
	print(func.__doc__)


def getText(url):
	request = requests.get(url)
	souped = BeautifulSoup(request.text, 'html.parser')
	return (souped.title.text, souped.find(class_="docdate").text, souped.find_all(class_="displaytext")[0].text)

Debates = [getText(url) for url in urls]
debatesDict = {(title,date):debate for title, date, debate in Debates}
newDict = {"|".join(list(key)):debatesDict[key] for key in debatesDict}

with open('debates.json', 'w') as outfile:
    json.dump(newDict, outfile)
