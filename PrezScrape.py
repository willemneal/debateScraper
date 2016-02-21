import datetime
import json
import re

debateDict = {}

with open('debates.json', 'r') as infile:
	debateDict = json.load(infile)
	debateDict = {tuple(key.split("|")): value for key, value in debateDict.items()}


def getDate(dateString):
	return datetime.datetime.strptime(dateString, "%B %d, %Y").date()

sortedKeys = sorted(debateDict.keys(), key=lambda x: getDate(x[1]), reverse=True)
lastDemDebate = debateDict[sortedKeys[1]]



def makeSpeakerDic(unfilt):
	filtered = re.findall("([A-Z]+:.*?)[A-Z]+:", unfilt, re.DOTALL)
	dic = {}
	for t in filtered[1:]:
		res = re.search("[A-Z]+:", t)
		key = t[res.start():res.end()-1].lower()
		value = t[res.end():]
		if key not in dic:
			dic[key] = []
		dic[key].append(value)

	return dic

betterD = makeSpeakerDic(lastDemDebate)
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
