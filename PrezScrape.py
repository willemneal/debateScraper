'''Scraping Presidential debate transcripts using BeautifulSoup
Let's get all the transcript data so that we can see what topics
are being talked about by the candidates'''

#First brings out the heavy machinary
import requests
from bs4 import BeautifulSoup
import re
import nltk
import wordcloud

#Grab the first webpage that contains links to the transcripts
webpage = requests.get('http://www.presidency.ucsb.edu/debates.php')
#Soupify the request
soup = BeautifulSoup(webpage.text, 'html.parser')

#First let's gather all the urls of the 2016 debates to go through
#My list of links to scrape text from 
tags = soup.findAll('td', class_="doctext")
links = soup.find_all(href=re.compile('pid='))

#def getLinks(soup)

#for a in soup.find_all(href=re.compile('pid=')):


urls = [a.get('href') for a in soup.find_all(href=re.compile('pid='))]

	
def helpMe(func):
	''' This is the DocString it can be found at helpMe.__doc__h\n'''
	print(func.__doc__)


def getText(url):
	request = requests.get(url)
	souped = BeautifulSoup(request.text, 'html.parser')
	return souped.find_all(class_="displaytext")[0].text

Debates = [getText(url) for url in urls]
#class="displaytext"




'''
	
def filter(tags):
	_list = []
	for a in tags:
		_list.append(a.next_element.attrs['href'])	
	return _list

urls = filter(tags)



pages = [getPage(url) for url in urls]

#Get the debate text from a given page
pages = [page.find(class_="displaytext").getText() for page in pages]
for p in pages:
	print(p)

	Let's make some BeautifulSoup objects out of the pages 
responses = []
pages = []
for link in baseURLs:
	responses.append(requests.get(link))
for page in responses:
	pages.append(BeautifulSoup(page.text, 'html.parser'))

print(len(baseURLs))
print(len(responses))
print(len(pages))

docdates = soup.find_all(class_='docdate')

thisYear = soup.find_all(string='2016')

docs = soup.find_all('td', 'doctext')
'''